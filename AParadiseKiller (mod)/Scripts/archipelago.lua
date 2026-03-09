---@diagnostic disable: lowercase-global
---@diagnostic disable: undefined-global
---@diagnostic disable: undefined-field

local AP = require "lua-apclientpp"

-- global to this mod
local game_name = "Paradise Killer"
local items_handling = 7  -- full remote
local client_version = {0, 5, 1}  -- optional, defaults to lib version
local message_format = AP.RenderFormat.TEXT

---@type APClient
local ap = nil
local checked_locations = {}
Goal = nil

-- TODO: user input
local host = "localhost"
local slot = "Player1"
local password = ""

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
        ap:ConnectSlot(slot, password, items_handling, {"Lua-APClientPP"}, client_version)
    end

    function on_slot_connected(slot_data)
        print("Slot connected")
        ap:Say("Hello World!")
        ap:Bounce({name="test"}, {game_name})
        ap:ConnectUpdate(nil, {"Lua-APClientPP"})
        --ap:LocationChecks({0x88888888})
        local StartingCharacterToName = {
            "Osvald","Castti","Temenos","Ochette","Partitio","Agnea","Hikari"
        }
        StartingCharacter = StartingCharacterToName[slot_data["StartingCharacter"]]
        StartingChapter = StartingCharacter.." Chapter1 Unlock"
        Goal              = slot_data["Goal"]
        
        Characters[StartingCharacter] = true
        local locations_to_scout = {}
        for locationName, locationID in pairs(LocationNameToAPId) do
            table.insert(locations_to_scout,locationID)
        end
        ap:LocationScouts(locations_to_scout, false)
        --SetInterruptedStoryFlags()
        SetStartingCharacterIcons()
    end


    function on_slot_refused(reasons)
        print("Slot refused: " .. table.concat(reasons, ", "))
    end

    function on_items_received(items)
        print("Items received:")
        for _, item in ipairs(items) do
            if item.index > GetIndex() then
                ApItemName = APItemIdToName[item.item]
                print(APItemIdToName[item.item].." from "..ap:get_player_alias(item.player))
                if ChapterUnlocks[ApItemName] == false then
                    ChapterUnlocks[ApItemName] = true
                elseif Characters[ApItemName]==false then
                    Characters[ApItemName] = true
                else
                    OnItemRecieve(ApItemName,ap:get_player_alias(item.player))
                end

                SetIndex(item.index)
            else
                print("item is out of index")
            end
        end
    end

    function on_location_info(items)
        print("Locations scouted:")
        for _, item in ipairs(items) do
            if ScoutedLocations[item.location]==nil then
                print("placing item "..ap:get_item_name(item.item,ap:get_player_game(item.player)).." in location"..item.location)
                print("apnamelength "..#APNameToChestID)
                local APLocationName = APLocationIdToName[item.location]
                if APLocationName == nil then
                    print("we sajdklajskl")
                end
                local chestID = APNameToChestID[APLocationName]
                if chestID==nil then
                    print("we have messed up")
                    break
                end
                ScoutedLocations[chestID] = {["ItemName"] = ap:get_item_name(item.item,ap:get_player_game(item.player)),["PlayerName"] = ap:get_player_alias(item.player)}
            end
        end
    end
    
    function on_location_checked(locations)
        print("calling location checked")
        print("Locations checked:" .. table.concat(locations, ", "))
        print("Checked locations: " .. table.concat(ap.checked_locations, ", "))
        for _, LocationID in ipairs(locations) do
            checked_locations[LocationID] = true
        end
    end

    function on_data_package_changed(data_package)
        print("Data package changed:")
        print(data_package)
    end

    function on_print(msg)
        print(msg)
    end

    function on_print_json(msg, extra)
        print(ap:render_json(msg, message_format))
        for key, value in pairs(extra) do
            -- print("  " .. key .. ": " .. tostring(value))
        end
    end

    function on_bounced(bounce)
        print("Bounced:")
        print(bounce)
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
    connect(host, slot, "")

    PopupQueue = {}
    --RegisterHook( function(Context)
    --    Conext.PlayerCharaId = 1
    --
    --end)
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
    print("Sending location ID: "..locationID)
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



function FillScoutedLocations()
    local AllLodadedChests = GetAllChests()
    local TextDB = GetGameTextDB()
    if AllLodadedChests==nil or TextDB==nil then
        return
    end

    for _, Chest in ipairs(AllLodadedChests) do
        if ScoutedLocations[Chest.ObjectData.ID] ~= nil and Chest.ObjectData.HaveItemLabel:ToString() ~= "APItem".._ and Chest.IsOpenFlag == false then
            if Chest.ObjectData.IsMoney == true then
            ---@diagnostic disable-next-line: inject-field
                Chest.ObjectData.IsMoney = false
            end
            local ScoutedLocationV = ScoutedLocations[Chest.ObjectData.ID]
            print(ScoutedLocationV["ItemName"].." for "..ScoutedLocationV["PlayerName"])
            
            Chest.ObjectData.HaveItemLabel = FName("APItem".._)
            TextDB:FindRow("APItemText".._).Text = FText(ScoutedLocationV["ItemName"].." for "..ScoutedLocationV["PlayerName"])

        end
    end
end

function GetIndex()
    local SaveGame = GetSaveGame()
    if SaveGame~=nil then
        print_debug("getting index rawhp")
        return SaveGame.PlayerMember[35].RawHP
    end
    return nil
end

function SetIndex(newIndex)
    local SaveGame = GetSaveGame()
    print("Setting Index: "..newIndex)
    if SaveGame~=nil then
        SaveGame.PlayerMember[35].RawHP = newIndex
    end
end

function VerifyCharacters()
    if StartingCharacter==nil then
        return
    end
    --print_debug("calling verifty character")
    for CharName, CharBool in pairs(Characters) do
        print("charname "..CharName)
        local HasCharReturn = HasCharacter(CharName)
        if HasCharReturn==nil then
            return
        end
        print("has char return is not nil")
        if CharBool~=HasCharReturn["HasCharacter"] then
            print("giving character "..CharName)
            print("HasCharReturn ")
            print(HasCharReturn["HasCharacter"])
            if CharBool then
                GiveCharacter(CharName)
            else 
                RemoveCharacter(HasCharReturn["PartyType"],HasCharReturn["Index"])
            end
        end
    end
end

function TitleScreenObjection()
    local TitleScrrenPlayerSelect = GetTitlePlayerSelect()
    if TitleScrrenPlayerSelect==nil then
        print_debug("")
        return
    end
    local SaveGames = GetSaveGames()
    for _, SaveGame in ipairs(SaveGames) do
        if SaveGame.FirstSelectCharacterID==0 then
            print_debug("SaveGame.FirstSelectCharacterID==0 setting PlayerCharaID to be 1")
            TitleScrrenPlayerSelect.SelectingCharacter = 1
        end
    end
end

function HasCharacter(CharacterName)
    --print_debug("calling HasCharacter")
    --print("charactername: " ..CharacterName)
    local CharacterID = EPlayableCharacterID[CharacterName] - 1
    local SaveGame = GetSaveGame()
    if SaveGame==nil then
        return nil
    end
    local PlayerParty = SaveGame.PlayerParty
    if PlayerParty==nil then
        print("player party is nil")
        return nil
    end
    --local SubPlayerParty = SaveGame.SubMemberID
    for i = 1,4 do
        --print("has character i "..tostring(i))
        if PlayerParty.MainMemberID[i] == CharacterID then
            return {["HasCharacter"] = true,["Index"] = i,["PartyType"]="MainMember"}
        end
    end
    for i = 1,8 do
        --print("has character2 i "..tostring(i))
        if PlayerParty.SubMemberID[i] == CharacterID then
            return {["HasCharacter"] = true,["Index"] = i,["PartyType"]="SubMember"}
        end
    end

    return {["HasCharacter"] = false}
end

function VerifyStoryFlags()
    --print_debug("calling Verify Story Flags")
    if StartingCharacter==nil then
        print_debug("StartingCharacter is nil in Verify Story Flags")
        return
    end
    local SaveGame = GetSaveGame()
    if SaveGame==nil then
        print_debug("SaveGame is nil in Verify Story Flags")
        return
    end
    
    for ChapterName, StoryInfo in pairs(CharacterChapterToStoryID) do
        if SaveGame.MainStoryData[StoryInfo["index"]].StoryID ~= StoryInfo["StoryID"] then
            SaveGame.MainStoryData[StoryInfo["index"]].StoryID = StoryInfo["storyID"]
            SaveGame.MainStoryData[StoryInfo["index"]].CurrentTaskID = 0
            SaveGame.MainStoryData[StoryInfo["index"]].State = 7
            SaveGame.MainStoryData[StoryInfo["index"]].ConfirmedFlag = false
        end

        if ChapterUnlocks[ChapterName] == true and ChapterName ~= StartingChapter then
            if SaveGame.MainStoryData[StoryInfo["index"]].StoryID == StoryInfo["storyID"] and SaveGame.MainStoryData[StoryInfo["index"]].State == 7 then
                SaveGame.MainStoryData[StoryInfo["index"]].StoryID = StoryInfo["storyID"]
                SaveGame.MainStoryData[StoryInfo["index"]].CurrentTaskID = 0
                SaveGame.MainStoryData[StoryInfo["index"]].State = 1
                SaveGame.MainStoryData[StoryInfo["index"]].ConfirmedFlag = false
            end  
        else --ChapterUnlocks[ChapterName] == false
            if SaveGame.MainStoryData[StoryInfo["index"]].StoryID == StoryInfo["storyID"] and SaveGame.MainStoryData[StoryInfo["index"]].State ~= 7 then
                print("removing story flag "..StoryInfo["storyID"])
                SaveGame.MainStoryData[StoryInfo["index"]].StoryID = StoryInfo["storyID"]
                SaveGame.MainStoryData[StoryInfo["index"]].CurrentTaskID = 0
                SaveGame.MainStoryData[StoryInfo["index"]].State = 7
                SaveGame.MainStoryData[StoryInfo["index"]].ConfirmedFlag = false
            end  
        end
    end
end 

function SetInterruptedStoryFlags()
    if StartingCharacter==nil then
        return
    end
    local SaveGame = GetSaveGame()
    if SaveGame==nil then
        return
    end

    
    for ChapterName, StoryInfo in pairs(CharacterChapterToStoryID) do
        if ChapterName~=CharacterChapterFNameToAPName[StartingCharacter..1] and SaveGame.MainStoryData[StoryInfo["index"]].StoryID ~= StoryInfo["storyID"] and SaveGame.MainStoryData[StoryInfo["index"]].State ~= 7 then
            print("setting no story data for "..ChapterName)
            SaveGame.MainStoryData[StoryInfo["index"]].StoryID = StoryInfo["storyID"]
            SaveGame.MainStoryData[StoryInfo["index"]].CurrentTaskID = 0
            SaveGame.MainStoryData[StoryInfo["index"]].State = 7
            SaveGame.MainStoryData[StoryInfo["index"]].ConfirmedFlag = false
        end 
    end

end

function SetStartingCharacterIcons()
    if ChangeStartingCharIcon == false and StartingCharacter~=nil then
        local CharacterIcons = GetTitlePlayerIcons()
        if CharacterIcons==nil then
            if #GetSaveGames()==1 then
                ChangeStartingCharIcon = true    
            end
            return
        end
        for _, CharacterIcon in ipairs(CharacterIcons) do
            if CharacterIcon.m_WorldMapDataLabel:ToString() ~= CharNameToMap[StartingCharacter] then
                CharacterIcon:SetWorldMapData(FName(CharNameToMap[StartingCharacter]))
            end
        end
        ChangeStartingCharIcon = true
    end
end

function IsChapterFinshed(index)
    local SaveGame = GetSaveGame()
    if SaveGame==nil then
        return nil
    end
    if SaveGame.MainStoryData[index].State == 5 then
        -- finished first chapter update all story flags and remove/give characters
        return true
    end
        return false

end

function IsStartingChapterFinished()
    -- on the title screen there are 2 dummy save games while in game there is only 1
    if FinshsedStartingChapter==false and #GetSaveGames()==1 then
        local SaveGame = GetSaveGame()
        if SaveGame==nil then
            return false
        end

        if SaveGame.PlayerMember[35].RawMP == 1 then
            return true
        end

        if SaveGame.MainStoryData[1].StoryID % 100 == 0 and SaveGame.MainStoryData[1].State == 5 then
            FinshsedStartingChapter = true
            SaveGame.PlayerMember[35].RawMP = 1
        end
    end
    return FinshsedStartingChapter
end