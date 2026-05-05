---@diagnostic disable: lowercase-global
---@diagnostic disable: undefined-global
---@diagnostic disable: undefined-field

require "ArchipelagoLists"

local AP = require "lua-apclientpp"

-- global to this mod
local game_name = "Paradise Killer"
local items_handling = 7  -- full remote
local client_version = {0, 6, 6}  -- optional, defaults to lib version
local message_format = AP.RenderFormat.TEXT

---@type APClient
local ap = nil
local checked_locations = {}
Goal = nil

-- TODO: user input
local host = "localhost"
local slot = "Player1"
local password = ""
local lastIndex = -1

function connect(server, slot, password)
    print("we are calling archipelago.lua connect")
    function on_socket_connected()
        print("Socket connected")
    end

    function on_socket_error(msg)
        print("Socket error: " .. msg)
    end

    function on_socket_disconnected()
        print("Socket disconnected")
    end

    function on_room_info()
        print("Room info")
        ap:ConnectSlot(slot, password, items_handling, {"Lua-APClientPP", "DeathLink"}, client_version)
    end

    function on_slot_connected(slot_data)
        print("Slot connected")
        print(tostring(slot_data))
        --print("missing locations: " .. table.concat(ap.missing_locations, ", "))
        --print("checked locations: " .. table.concat(ap.checked_locations, ", "))
        ap:Bounce({name="test"}, {game_name})
        ap:ConnectUpdate(nil, {"Lua-APClientPP", "DeathLink"})
        print(tostring(ap:get_slot()))
        ChangeDialogueName(ap:get_slot())
    end

    function on_slot_refused(reasons)
        print("Slot refused: " .. table.concat(reasons, ", "))
    end

    function on_items_received(items)
        print("Items received:")

        local player    = FindFirstOf("YMKCharacter")
        local inventory = player.InventoryComponent:Get()
        local knowledge = player.KnowledgeComponent:Get()

        UnregisterInventory()
        for _, item in ipairs(items) do
            if item.index > lastIndex then
                lastIndex = item.index
                
                local APitem = APItemIdToName[item.item]
                --print("Owns: " .. APitem .. " - " .. tostring(inventory:DoesOwnItem(FName(APitem))))
                
                if APitem ~= nil then
                    print("item test" .. tostring(item.item) .. tostring(knowledgeID[item.item]))
                    if knowledgeID[item.item] then
                        if not knowledge:DoesHaveKnowledge(FName(APitem)) then
                            knowledge:GainKnowledge(FName(APitem))
                        end
                    else
                        if not inventory:DoesOwnItem(FName(APitem)) then
                            inventory:GiveItem(FName(APitem), 1)
                        end
                    end
                end
            end
        end
        RegisterInventory()
    end

    function on_location_info(items)
        print("Locations scouted:")
    end
    
    function on_location_checked(locations)
        print("calling location checked")
        --print("Locations checked:" .. table.concat(locations, ", "))
        --print("Checked locations: " .. table.concat(ap.checked_locations, ", "))
        for _, LocationID in ipairs(locations) do
            checked_locations[LocationID] = true
        end
    end

    function on_data_package_changed(data_package)
        print("Data package changed")
    end

    function on_print(msg)
        print(tostring(msg))
    end

    function on_print_json(msg, extra)
        print(ap:render_json(msg, message_format))
        for key, value in pairs(extra) do
            -- print("  " .. key .. ": " .. tostring(value))
        end
    end

    function on_bounced(bounce)
        print("Bounced")
        if bounce.tags and table.concat(bounce.tags, " "):find("DeathLink") then
            print("Received DeathLink!")

            local now = os.time()

            -- Prevent infinite death loops
            if now - lastDeathTime < 5 then
                print("Ignoring DeathLink (cooldown)")
                return
            end

            lastDeathTime = now

            TriggerDeath()
        end
    end

    function on_retrieved(map, keys, extra)
        print("Retrieved:")
        -- since lua tables won't contain nil values, we can use keys array
        for _, key in ipairs(keys) do
            print("  " .. key .. ": " .. tostring(map[key]))
        end
        -- extra will include extra fields from Get
        print("Extra:")
        for key, value in pairs(extra) do
            print("  " .. key .. ": " .. tostring(value))
        end
        -- both keys and extra are optional
    end

    function on_set_reply(message)
        print("Set Reply:")
        for key, value in pairs(message) do
            print("  " .. key .. ": " .. tostring(value))
            if key == "value" and type(value) == "table" then
                for subkey, subvalue in pairs(value) do
                    print("    " .. subkey .. ": " .. tostring(subvalue))
                end
            end
        end
    end


    local uuid = ""
    ap = AP(uuid, game_name, server);
    print("Connecting to " .. server .. " ...")
    ap:set_socket_connected_handler(on_socket_connected)
    ap:set_socket_error_handler(on_socket_error)
    ap:set_socket_disconnected_handler(on_socket_disconnected)
    ap:set_room_info_handler(on_room_info)
    ap:set_slot_connected_handler(on_slot_connected)
    ap:set_slot_refused_handler(on_slot_refused)
    ap:set_items_received_handler(on_items_received)
    ap:set_location_info_handler(on_location_info)
    ap:set_location_checked_handler(on_location_checked)
    ap:set_data_package_changed_handler(on_data_package_changed)
    ap:set_print_handler(on_print)
    ap:set_print_json_handler(on_print_json)
    ap:set_bounced_handler(on_bounced)
    ap:set_retrieved_handler(on_retrieved)
    ap:set_set_reply_handler(on_set_reply)
end

function connectToAp(host, slot, password)
    ExecuteAsync(function ()
        connect(host, slot, password)
        RegisterInventory()
        while ap do
            ap:poll()
        end
    end)
end

function disconnect()
---@diagnostic disable-next-line: cast-local-type
    checked_locations = {}
---@diagnostic disable-next-line: cast-local-type
    ap = nil
    collectgarbage("collect")
end

function SendLocation(locationID)
    if ap == nil then
        print("AP client not connected, cannot send location")
        return
    end
    print("Sending location ID: " .. locationID)

    local player    = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local knowledge = player.KnowledgeComponent:Get()

    APitem = APLocationIdToName[locationID] 

    if knowledgeID[locationID] then
        knowledge:LoseKnowledge(FName(APitem))
    else
        inventory:RemoveItem(FName(APitem), 1)
    end

    inventory:RemoveItem(FName(APLocationIdToName[locationID]), 1)
    print("ITEM TO REMOVE: " .. tostring(APLocationIdToName[locationID]))
    ap:LocationChecks({tonumber(locationID)})
end

function IsLocationChecked(locationID)
    if checked_locations==nil then
        return nil
    end
    return checked_locations[locationID] ~= nil
end

function SendLocationFromName(locationName)
    local locationID = GetAPLocationIDfromName(locationName)
    if ap == nil then
        print("AP client not connected, cannot send location")
        return
    end

    if locationID == nil then
        print("Location name:"..locationName.."Is not valid.")
        return
    end
    print("Sending location name: "..locationName)

    ap:LocationChecks({tonumber(locationID)})
end


function GetAPLocationIDfromName(locationName)
    return LocationNameToAPId[locationName]
end

function GetAPNamefromLocationID(locationID)
    return APLocationIdToName[locationID]
end

function GetAPItemIDfromName(itemName)
    return ItemNameToAPId[itemName]
end

function GetItemNamefromAPItemID(itemID)
    return APItemIdToName[itemID]
end

function ChestNamefromID(ChestID)
    return ChestIDToName[ChestID]
end

function ChestFilenameFromChestID(ChestID)
    return ChestIDToFilename[ChestID]
end

function GetAPCheckedLocations()
    return ap.checked_locations
end

function GetAPMissingLocations()
    return ap.missing_locations
end

function ScoutLocations(ScoutLocations)
    if #ScoutLocations>0 then
        ap:LocationScouts(ScoutLocations,0)
    end
end

function SendMessage(message)
    ap:Say(message)
end



--[[
Process Inventory Management
]]
preID  = 0
postID = 0

local knowledgeList = {405, 406, 407}
knowledgeID = {}

for _, id in ipairs(knowledgeList) do
    knowledgeID[id] = true
end

function RegisterInventory()
    preID, postID = RegisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
            function(Context, affectedActor, itemId)
                SendLocation(GetAPLocationIDfromName(itemId:get():ToString()))
            end
    )
end

function UnregisterInventory()
    UnregisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
        preID,
        postID
    )
end

function ChangeDialogueName(slotname)
    local char = StaticFindObject("/Game/Assets/Characters/ItemData/PlayerCharacterData.PlayerCharacterData")
    char.CharacterName = FText(slotname)

    local char = StaticFindObject("/Game/Assets/Characters/ItemData/WhiskyDrinker1CharacterData.WhiskyDrinker1CharacterData")
    char.CharacterName = FText("Caffeinated Moth")
end

function TriggerDeath()
    local player = FindFirstOf("YMKCharacter")
    player:OnRespawnPressed()
end