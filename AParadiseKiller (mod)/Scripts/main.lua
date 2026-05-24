print("[AParadiseKiller] loaded")


require "archipelago"

local UEHelpers = require("UEHelpers")
local DEBUG_KEYBIND = true

if DEBUG_KEYBIND then 
    RegisterKeyBind(Key.ONE, { ModifierKey.CONTROL }, function()
        print("[AParadiseKiller] activated")

        if not active then
            active = true
        end
    end)

    RegisterKeyBind(Key.TWO, { ModifierKey.CONTROL }, function()
        RegisterHook(
            "Function /Game/Assets/Blueprints/Blueprints_Pickups/Blueprint_Pickup_Parent.Blueprint_Pickup_Parent_C:ExecuteUbergraph_Blueprint_Pickup_Parent",
            function(Context)
                local actor = Context:get()
                if not actor then return end

                local fullname = actor:GetFullName()
                if not fullname then return end

                local className = string.match(fullname, "^[^%s]+")
                if not className then return end

                className = string.gsub(className, "^Blueprint_", "")
                className = string.gsub(className, "_C$", "")

                print("[Location Collected]: " .. className)
            end
        )
        RegisterHook(
        "function /Game/Assets/Blueprints/Blueprints_Pickups/Blueprint_Pickup_Parent_Crest.Blueprint_Pickup_Parent_Crest_C:ExecuteUbergraph_Blueprint_Pickup_Parent_Crest",
            function(Context)
                if not Context then
                    print("[Hook] Context is nil")
                    return false
                end

                print("[Blocked Pickup Attempt] Item:", Context:GetName())

                -- Block original
                return true
            end
        )
        RegisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
            function(Context, affectedActor, itemId)
                print("[Inventory Added] Fstring: " .. tostring(itemId:get()))
                print("[Inventory Added] ItemId: " .. itemId:get():ToString())
            end
        )
        local actors = FindAllOf("Actor")

        for _, actor in pairs(actors) do
            if actor and actor:IsValid() then
                local class = actor:GetClass()
                if class and string.find(class:GetFullName(), "") then

                    local loc = actor:K2_GetActorLocation()

                    print(string.format(
                        "%s | X=%.2f Y=%.2f Z=%.2f",
                        actor:GetFullName(),
                        loc.X, loc.Y, loc.Z
                    ))

                end
            end
        end
    end)

    RegisterKeyBind(Key.THREE, { ModifierKey.CONTROL }, function()
        for _, obj in pairs(FindAllOf("InventoryItemData")) do
            local name = obj:GetFullName()
            if string.find(name, "Item") then
                print(name)
            end
        end
    end)

    RegisterKeyBind(Key.EIGHT, { ModifierKey.CONTROL }, function()
        local item = StaticFindObject("/Game/Assets/Inventory/ItemData/Collectables/Collectable_RottenEgg.Collectable_RottenEgg")
        
        item.ItemName = FText("Archipelago Item")
        print(item.ItemName:ToString())

        item.ItemDescription = FText("This is a test for an Archipelago item!")
        print(item.ItemDescription:ToString())

        local player = FindFirstOf("YMKCharacter")
        player:OnRespawnPressed()
    end)

    RegisterKeyBind(Key.NINE, { ModifierKey.CONTROL }, function()
        print('jippie')
        local player = FindFirstOf("YMKCharacter")
        
        local inventory = player.InventoryComponent:Get()
        local item = ""
        inventory:GiveItem(FName("Crest_ApartmentStatue_01"), 1)
        --inventory:RemoveItem(FName("Crest_ApartmentStatue_01"), 1)
        --[[
        inventory:GiveItem(FName("Starlight"), 1)
        inventory:GiveItem(FName("SymbolSDCard_SKY"), 1)
        inventory:GiveItem(FName("SymbolSDCard_Pyramids"), 1)
        inventory:GiveItem(FName("SymbolSDCard_Worship_FromVending"), 1)
        ]]
        local knowledge = player.KnowledgeComponent:Get()
        local info = ""
        knowledge:GainKnowledge(FName("SkippedIntro"))
        knowledge:GainKnowledge(FName("UnlockedFastTravel"))
        knowledge:GainKnowledge(FName("DoubleJumpKnowledge"))
        knowledge:GainKnowledge(FName("DashKnowledge"))
        knowledge:GainKnowledge(FName("MeditationKnowledge"))

        RegisterHook(
            "Function /Game/Assets/Blueprints/Blueprints_Pickups/Blueprint_Pickup_Parent.Blueprint_Pickup_Parent_C:ExecuteUbergraph_Blueprint_Pickup_Parent",
            function(Context)
                local actor = Context:get()
                if not actor then return end

                local fullname = actor:GetFullName()
                if not fullname then return end

                -- Extract class name
                local className = string.match(fullname, "^[^%s]+")
                if not className then return end

                className = string.gsub(className, "^Blueprint_", "")
                className = string.gsub(className, "_C$", "")

                print("[trigger]: " .. fullname)
            end
        )
    end)

    RegisterKeyBind(Key.THREE, { ModifierKey.CONTROL }, function()
        RegisterHook(
            "Function /Script/ParadiseKiller.PickupItem:OnRemovedItemFromWorld",
            function(Context)
                print("A")
            end
        )
        RegisterHook(
            "Function /Script/ParadiseKiller.InventoryComponent:GiveItem",
            function(Context)
                print("B")
            end
        )
        RegisterHook(
            "/Script/ParadiseKiller.InventoryLibrary:AddItemToPlayerInventory",
            function(Context, WorldContext, InventoryItem, AmountToGive)

                print("Item pickup detected:", InventoryItem:GetFullName())

            end
        )
    end)
end

RegisterConsoleCommandHandler("/connect", function(FullCommand, userInput, Ar)
    print("Calling /connect")
    Ar:Log("Calling /connect")

    Connect(FullCommand, userInput, Ar)
    return true
end)

RegisterConsoleCommandHandler("/disconnect", function(FullCommand, userInput, Ar)
    print("Calling /disconnect")
    Ar:Log("Calling /disconnect")

    disconnect()
    return true
end)

RegisterConsoleCommandHandler("/message", function(FullCommand, userInput, Ar)
    print("Sending message")
    Ar:Log("Sending message")
    
    SendMessage(userInput)
    return true
end)

RegisterConsoleCommandHandler("/exile", function(FullCommand, userInput, Ar)
    print("Sending you back to exile.")
    Ar:Log("Sending you back to exile.")
    
    local player = FindFirstOf("YMKCharacter")
    local loc = player:K2_GetActorLocation()
    loc.X = -70813.0
    loc.Y = 8788.0
    loc.Z = 73152.2734375
    player:K2_SetActorLocation(loc, false, {}, false)

    return true
end)

RegisterConsoleCommandHandler("/blood", function(FullCommand, userInput, Ar)
    print("Here, have a blood offering.")
    Ar:Log("Here, have a blood offering.")
    
    local player = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local item = "GoldCoin_001"
    inventory:GiveItem(FName(item), tonumber(userInput[1]))
    inventory:RemoveItem(FName(item), 1)

    return true
end)

function Connect(commandName, userInput, Ar)
    local command = commandName
    local host, slot, password = command:match('/connect%s+(%S+)%s+"(.-)"%s+"(.-)"')

    if not host or not slot then
        host, slot =
            command:match('/connect%s+(%S+)%s+"(.-)"')

        password = ""
    end

    if not host or not slot then
        print("Usage: /connect <host> \"<slot>\" [\"password\"]")
        Ar:Log("Usage: /connect <host> \"<slot>\" [\"password\"]")
        return
    end

    password = password or ""

    print("Trying to connect to " .. host .. " with slot " .. slot .. " and password " .. password)

    Ar:Log("Trying to connect to " .. host .. " with slot " .. slot .. " and password " .. password)

    connectToAp(host, slot, password)
end