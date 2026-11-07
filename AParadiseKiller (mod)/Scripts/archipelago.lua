local AP  = require("lua-apclientpp")
local game_name = "Paradise Killer"
local items_handling = 7

---@type APClient
local ap = nil
local checked_locations = {}
local lastIndex = -1
local goal = nil
local goal_requirement = 0
local goal_counter = 0

-- General AP stuff
function connect(server, slot, password)
    function on_socket_connected()
        LogToConsole("[AP] Socket connected")
    end

    function on_socket_error(msg)
        LogToConsole("[AP] Socket error: " .. tostring(msg))
    end

    function on_socket_disconnected()
        LogToConsole("[AP] Socket disconnected")

        UnregisterDeathlink()
        UnregisterInventory()
        lastIndex = -1
    end

    function on_room_info()
        LogToConsole("[AP] Room info collected")

        ap:ConnectSlot(slot, password, items_handling, {"Lua-APClientPP"}, client_version)
    end

    function on_slot_connected(slot_data)
        LogToConsole("[AP] Slot connected")
        
        goal = slot_data.goal
        if goal == 0 then
            goal_requirement = slot_data.number_nebula_drinks
        elseif goal == 1 then
            goal_requirement = slot_data.number_whisky_bottles
        end

        ap:ConnectUpdate(nil, {"Lua-APClientPP"})

        ChangeDialogueName(ap:get_slot())
        RegisterDeathlink()
        BuildInventoryItemDataLookup()
    end

    function on_slot_refused(reasons)
        LogToConsole("[AP] Slot refused: " .. table.concat(reasons, ", "))
    end

    function on_items_received(items)
        local player = FindFirstOf("YMKCharacter")
        local inventory = player.InventoryComponent:Get()
        local knowledge = player.KnowledgeComponent:Get()

        UnregisterInventory()

        for _, item in ipairs(items) do
            if item.index > lastIndex then
                lastIndex = item.index
                
                if goal == 0 and item.item >= 101 and item.item <= 123 then
                    goal_counter = goal_counter + 1
                elseif goal == 1 and item.item >= 201 and item.item <= 213 then
                    goal_counter = goal_counter + 1
                end

                if goal_counter >= goal_requirement then
                    ap:StatusUpdate(30)
                end

                local handler = ItemHandlers[item.item]
                if handler then
                    handler(item, inventory, knowledge)
                else
                    LogToConsole("[AP] [bug] Unhandled item: " .. item.item)
                end
            end
        end

        RegisterInventory()
    end

    function on_location_info(items)
        
    end

    function on_location_checked(locations)
        for _, LocationID in ipairs(locations) do
            checked_locations[LocationID] = true
        end
    end

    function on_data_package_changed(data_package)
        LogToConsole("[AP] Data package changed")
    end

    function on_print(msg)
        LogToConsole(tostring(msg))
    end

    function on_print_json(msg, extra)
        LogToConsole(ap:render_json(msg, AP.RenderFormat.TEXT))
    end

    function on_bounced(bounce)
        LogToConsole("[AP] Bounced")
        if bounce.tags and table.concat(bounce.tags, " "):find("DeathLink") then
            LogToConsole("[AP] Deathlink Received")

            TriggerDeath()
        end
    end

    function on_retrieved(map, keys, extra)
        LogToConsole("[AP] Retrieved:")
        for _, key in ipairs(keys) do
            LogToConsole("  " .. key .. ": " .. tostring(map[key]))
        end
        
        LogToConsole("[AP] Extra:")
        for key, value in pairs(extra) do
            LogToConsole("  " .. key .. ": " .. tostring(value))
        end
    end

    function on_set_reply(message)
        LogToConsole("[AP] Set Reply:")
        for key, value in pairs(message) do
            LogToConsole("  " .. key .. ": " .. tostring(value))
            if key == "value" and type(value) == "table" then
                for subkey, subvalue in pairs(value) do
                    LogToConsole("    " .. subkey .. ": " .. tostring(subvalue))
                end
            end
        end
    end

    local uuid = ""
    ap = AP(uuid, game_name, server);
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
    ExecuteAsync(function()
        connect(host, slot, password)
        RegisterInventory()
        while ap do
            ap:poll()
        end
    end)
end

function disconnect()
    LogToConsole("[AP] Disconnected")
    
    checked_locations = {}
    ap = nil
    collectgarbage("collect")

    UnregisterDeathlink()
    UnregisterInventory()
    lastIndex = -1
end

function SendLocation(locationID)
    local player    = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local knowledge = player.KnowledgeComponent:Get()

    local APitem    = GAME_LOCATION_ID_TO_NAME[locationID]

    if APitem then
        if KnowledgeItemIDs[GAME_ITEM_ID_TO_NAME[GAME_LOCATION_ID_TO_NAME[locationID]]] then
            knowledge:LoseKnowledge(FName(APitem))
        else
            inventory:RemoveItem(FName(APitem), 1)
        end
    else
        LogToConsole("[AP] [bug] Impossible location to send: " .. tostring(locationID) .. tostring(APitem))
    end

    ap:LocationChecks({tonumber(locationID)})
end

function IsLocationChecked(locationID)
    if checked_locations == nil then
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
    if #ScoutLocations > 0 then
        ap:LocationScouts(ScoutLocations, 0)
    end
end

function SendMessage(message)
    ap:Say(message)
end



-- Inventory Management
--- Both of these are technical debt from the manual days, and this inventory/itemID system will be changed during the first mayor update.
local ArchipelagoList    = require("ArchipelagoList") 
local GameList           = require("GameList")

GAME_ITEM_ID_TO_NAME     = GameList.item_id_to_game_name

GAME_LOCATION_NAME_TO_ID = GameList.location_name_to_ap_id
GAME_LOCATION_ID_TO_NAME = {}
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

        if not name or name == "" then
            return
        end

        local itemData = GetInventoryItemData(name)

        if itemData then
            itemData:SetPropertyValue("MaximumNumberThatCanBeOwned", 2)
        else
            LogToConsole("[AP] Impossible item to change property (MaximumNumberThatCanBeOwned) for: " .. tostring(name))
        end 

        if not inventory:DoesOwnItem(FName(name)) then
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
        end
    end
end

registerKnowledgeItems({ 405, 406, 407 })

for _, id in ipairs({ 601, 602, 603, 604, 605 }) do
    registerCrestItem(id)
end

for id, _ in pairs(GAME_ITEM_ID_TO_NAME) do
    if not ItemHandlers[id] then
        registerNormalItem(id)
    end
end

InventoryItemDataByName = {}
function BuildInventoryItemDataLookup()
    local objects = FindAllOf("InventoryItemData")
    objects = TableConcat(objects, FindAllOf("VendingMachineItemData"))
    objects = TableConcat(objects, FindAllOf("MusicTrackItemData"))
    
    local count = 0
    for _, obj in pairs(objects) do
        local ok, name = pcall(function()
            return obj:GetFName():ToString()
        end)

        if ok and name then
            InventoryItemDataByName[name] = obj
            count = count + 1
        else
            ConsoleLog("Failed to get object name: " .. tostring(obj))
        end
    end
end
function GetInventoryItemData(itemName)
    return InventoryItemDataByName[itemName]
end

local preIDIM  = 0
local postIDIM = 0
function RegisterInventory()
    preIDIM, postIDIM = RegisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
        function(Context, affectedActor, itemId)
            local itemName = itemId:get():ToString()
            local locationID = GetAPLocationIDfromName(itemName)
            if locationID and not IsLocationChecked(locationID) then
                SendLocation(locationID)
            end
        end
    )
end
function UnregisterInventory()
    UnregisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
        preIDIM,
        postIDIM
    )
end



-- Cosmetic changes
function ChangeDialogueName(slotname)
    local char = StaticFindObject("/Game/Assets/Characters/ItemData/PlayerCharacterData.PlayerCharacterData")
    char.CharacterName = FText(slotname)

    local char = StaticFindObject(
    "/Game/Assets/Characters/ItemData/WhiskyDrinker1CharacterData.WhiskyDrinker1CharacterData")
    char.CharacterName = FText("Moth")
end



-- Deathlink system
local deathlinkSuppressed, incomingDeath, deathlinkEnabled = false, false, false
local preDLFO, postDLFO, preDLFI, postDLFI = 0, 0, 0, 0
function RegisterDeathlink()
    preDLFO, postDLFO = RegisterHook(
        "Function /Script/ParadiseKiller.PlayerRespawnComponent:FadeOutComplete_Callback",
        function(Context)
            if deathlinkEnabled and not deathlinkSuppressed then
                ap:Bounce(
                    {
                        time = ap:get_server_time(),
                        source = ap:get_slot(),
                        cause = ap:get_slot() .. " died on Paradise Island 24."
                    },
                    nil,
                    nil,
                    {"DeathLink"}
                )
            end
        end
    )
    preDLFI, postDLFI = RegisterHook(
        "Function /Script/ParadiseKiller.PlayerRespawnComponent:FadeInComplete_Callback",
        function(Context)
            if deathlinkEnabled and incomingDeath then
                local player = FindFirstOf("YMKCharacter")
                local component = player.PlayerRespawnComponent:Get()

                component:SetPropertyValue(
                    "StartRespawnIfLowerThan",
                    -550.0
                )

                incomingDeath = false
                deathlinkSuppressed = false
            end
        end
    )
end
function UnregisterDeathlink()
    UnregisterHook(
        "Function /Script/ParadiseKiller.PlayerRespawnComponent:FadeOutComplete_Callback",
        preDLFO,
        postDLFO
    )
    UnregisterHook(
        "Function /Script/ParadiseKiller.PlayerRespawnComponent:FadeInComplete_Callback",
        preDLFI,
        postDLFI
    )    
end
function TriggerDeath()
    if not incomingDeath then
        incomingDeath = true
        deathlinkSuppressed = true

        local player = FindFirstOf("YMKCharacter")
        local component = player.PlayerRespawnComponent:Get()

        component:SetPropertyValue(
            "StartRespawnIfLowerThan",
            999999.0
        )
    end
end
function ToggleDeathlink()
    deathlinkEnabled = not deathlinkEnabled
    local tags = nil
    if deathlinkEnabled then
        tags = {"Lua-APClientPP", "DeathLink"}
    else
        tags = {"Lua-APClientPP"}
    end

    ap:ConnectUpdate(nil, tags)
end



-- Textclient onzin
RegisterConsoleCommandHandler("/log", function(FullCommand, userInput, Ar)
    local message = tostring(FullCommand:sub(6))
    Ar:Log(message)
    print(message)
    
    return true
end)
function LogToConsole(Message)
    local Kismet = StaticFindObject("/Script/Engine.Default__KismetSystemLibrary")
    local pc = FindFirstOf("PlayerController")
    local world = FindFirstOf("World")

    Kismet:ExecuteConsoleCommand(world, "/log " .. Message, pc)
end
