---@diagnostic disable: lowercase-global
---@diagnostic disable: undefined-global
---@diagnostic disable: undefined-field

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

        local player = FindFirstOf("YMKCharacter")
        local inventory = player.InventoryComponent:Get()
        local knowledge = player.KnowledgeComponent:Get()

        UnregisterInventory()

        for _, item in ipairs(items) do
            if item.index > lastIndex then
                lastIndex = item.index

                local handler = ItemHandlers[item.item]

                if handler then
                    handler(item, inventory, knowledge)
                else
                    print("Unhandled item: " .. tostring(item.item))
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
        print(msg)
    end

    function on_print_json(msg, extra)
        print(ap:render_json(msg, message_format))
        for key, value in pairs(extra) do
            print("  " .. key .. ": " .. tostring(value))
        end
    end

    function on_bounced(bounce)
        print("Bounced")
        if bounce.tags and table.concat(bounce.tags, " "):find("DeathLink") then
            print("Received DeathLink!")
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

    print("Sending location ID: " .. tostring(locationID))

    local player    = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local knowledge = player.KnowledgeComponent:Get()

    local APitem    = GAME_LOCATION_ID_TO_NAME[locationID]
    --print("string: " .. APitem.tostring())

    if KnowledgeItemIDs[GAME_ITEM_ID_TO_NAME[GAME_LOCATION_ID_TO_NAME[locationID]]] then
        knowledge:LoseKnowledge(FName(APitem))
    else
        inventory:RemoveItem(FName(APitem), 1)
    end

    print("Removed item:", itemName)
    ap:LocationChecks({ tonumber(locationID) })
    --ap:StatusUpdate(30)
end

function IsLocationChecked(locationID)
    if checked_locations==nil then
        return nil
    end
    return checked_locations[locationID] ~= nil
end

function GetAPLocationIDfromName(locationName)
    return GAME_LOCATION_NAME_TO_ID[locationName]
end

function GetAPNamefromLocationID(locationID)
    return AP_LOCATION_ID_TO_NAME[locationID]
end

function GetAPItemIDfromName(itemName)
    return AP_ITEM_NAME_TO_ID[itemName]
end

function GetItemNamefromAPItemID(itemID)
    return AP_ITEM_ID_TO_NAME[itemID]
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



-- Process Inventory Management
local ArchipelagoList = require("ArchipelagoList")
local GameList = require("GameList")

GAME_ITEM_ID_TO_NAME      = GameList.item_id_to_game_name

GAME_LOCATION_NAME_TO_ID  = GameList.location_name_to_ap_id
GAME_LOCATION_ID_TO_NAME  = {}
for name, id in pairs(GAME_LOCATION_NAME_TO_ID) do
    GAME_LOCATION_ID_TO_NAME[id] = name
end

ItemHandlers = {}
crestProgress = {}
KnowledgeItemIDs = {}

function registerKnowledgeItems(list)
    for _, id in ipairs(list) do
        KnowledgeItemIDs[id] = true
        ItemHandlers[id] = function(item, inventory, knowledge)
            local name = GAME_ITEM_ID_TO_NAME[id]
            if name and not knowledge:DoesHaveKnowledge(FName(name)) then
                knowledge:GainKnowledge(FName(name))
            end
        end
    end
end

function registerNormalItem(id)
    ItemHandlers[id] = function(item, inventory, knowledge)
        local name = GAME_ITEM_ID_TO_NAME[id]
        if name and not inventory:DoesOwnItem(FName(name)) then
            inventory:GiveItem(FName(name), 1)
        end
    end
end

function registerCrestItem(id)
    ItemHandlers[id] = function(item, inventory, knowledge)
        local locations = GAME_ITEM_ID_TO_NAME[id]
        if not locations then return end

        crestProgress[id] = crestProgress[id] or 0
        crestProgress[id] = crestProgress[id] + 1
        local loc = locations[crestProgress[id]]

        if loc then
            if not inventory:DoesOwnItem(FName(loc)) then
                inventory:GiveItem(FName(loc), 1)
            end
        else
            --print("Extra crest received for AP item:", id)
        end
    end
end

registerKnowledgeItems({405, 406, 407})

for _, id in ipairs({601, 602, 603, 604, 605}) do
    registerCrestItem(id)
end

for id, _ in pairs(GAME_ITEM_ID_TO_NAME) do
    if not ItemHandlers[id] then
        registerNormalItem(id)
    end
end

preID  = 0
postID = 0

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
    char.CharacterName = FText("Moth")
end

function TriggerDeath()
    local player = FindFirstOf("YMKCharacter")
    player:OnRespawnPressed()
end