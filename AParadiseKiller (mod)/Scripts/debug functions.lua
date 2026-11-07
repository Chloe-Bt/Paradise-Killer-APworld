UEHelpers       = require("UEHelpers")

RegisterKeyBind(Key.ONE, { ModifierKey.CONTROL }, function()
    print("[AParadiseKiller] activated")

    if not active then
        active = true
    end
end)

RegisterKeyBind(Key.TWO, { ModifierKey.CONTROL }, function()
    local player = FindFirstOf("YMKCharacter")
    local component = player.PlayerRespawnComponent:Get()
    component:SetPropertyValue("StartRespawnIfLowerThan", 999999.0)
    print("[Respawn] StartRespawnIfLowerThan updated")
    ExecuteWithDelay(50, function()
        component:SetPropertyValue("StartRespawnIfLowerThan", -550.0)
        print("[Respawn] Restored default threshold")
    end)
end)

RegisterKeyBind(Key.EIGHT, { ModifierKey.CONTROL }, function()
    local item = StaticFindObject(
    "/Game/Assets/Inventory/ItemData/Collectables/Collectable_RottenEgg.Collectable_RottenEgg")

    item.ItemName = FText("Archipelago Item")
    print(item.ItemName:ToString())

    item.ItemDescription = FText("This is a test for an Archipelago item!")
    print(item.ItemDescription:ToString())

    local player = FindFirstOf("YMKCharacter")
end)

RegisterKeyBind(Key.NINE, { ModifierKey.CONTROL }, function()
    print('jippie')
    local player = FindFirstOf("YMKCharacter")

    local inventory = player.InventoryComponent:Get()
    local itemData = StaticFindObject("/Game/Assets/Inventory/ItemData/Phone/Starlight.Starlight")
    print(itemData:GetPropertyValue("MaximumNumberThatCanBeOwned"))
    itemData:SetPropertyValue("MaximumNumberThatCanBeOwned", 5)
    print(itemData:GetPropertyValue("MaximumNumberThatCanBeOwned"))

    -- inventory:RemoveItem(FName("Collectable_PyramidCharm"), 1)
    -- inventory:GiveItem(FName("Collectable_PyramidCharm"), 1)
    
    inventory:GiveItem(FName("GoldCoin_117"), 1)
    --[[
    inventory:GiveItem(FName("SymbolSDCard_SKY"), 1)
    inventory:GiveItem(FName("SymbolSDCard_Pyramids"), 1)
    inventory:GiveItem(FName("SymbolSDCard_Worship_FromVending"), 1)
    ]]
    local knowledge = player.KnowledgeComponent:Get()
    local infoData = StaticFindObject("/Game/Assets/CaseFiles/SealFirst/SuppotingData/Lydia_Knife.Lydia_Knife")
    --print('infomax' .. infoData:GetPropertyValue("MaximumNumberThatCanBeOwned"))
    --infoData:SetPropertyValue("MaximumNumberThatCanBeOwned", 2)
    --print('infomax' .. infoData:GetPropertyValue("MaximumNumberThatCanBeOwned"))

    knowledge:GainKnowledge(FName("NewGhost_ZealousCarving"))
    knowledge:GainKnowledge(FName("UnlockedFastTravel"))
    knowledge:GainKnowledge(FName("DoubleJumpKnowledge"))
    knowledge:GainKnowledge(FName("DashKnowledge"))
    knowledge:GainKnowledge(FName("MeditationKnowledge"))
    
end)

RegisterKeyBind(Key.THREE, { ModifierKey.CONTROL }, function()
    RegisterHook(
        "/Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
        function(Context, affectedActor, itemId)
            ConsoleLog(
                "[AP] Awarded item ID: " ..
                tostring(itemId:get():ToString())
            )
        end
    )
    RegisterHook(
        "/Script/ParadiseKiller.InventoryComponent:CanPickUpItem",
        function(Context, ItemData)
            ConsoleLog("[AP] CanPickUpItem PRE")
        end,
        function(Context, ItemData)
            ConsoleLog("[AP] CanPickUpItem POST")
        end
    )
    -- Diagnostic: inspect the item-data object passed to CanPickUpItem.
    local hookId = RegisterHook(
        "/Script/ParadiseKiller.InventoryComponent:CanPickUpItem",
        function(Context, ItemData)
            local itemData = ItemData:get()

            if not itemData or not itemData:IsValid() then
                ConsoleLog("[AP] CanPickUpItem: invalid ItemData")
                return
            end

            ConsoleLog("=== CanPickUpItem ===")
            ConsoleLog("ItemData: " .. itemData:GetFullName())

            local ok, itemName = pcall(function()
                return itemData:GetItemName()
            end)

            if ok and itemName then
                ConsoleLog("GetItemName: " .. tostring(itemName))
            else
                ConsoleLog("GetItemName unavailable")
            end

            local okCategory, category = pcall(function()
                return itemData:GetItemCategory()
            end)

            if okCategory and category then
                ConsoleLog("Category: " .. tostring(category))
            end

            local okClass, itemClass = pcall(function()
                return itemData:GetPropertyValue("InventoryItem")
            end)

            if okClass and itemClass then
                ConsoleLog("InventoryItem property: " .. tostring(itemClass))
            end
        end
    )

    ConsoleLog("[AP] CanPickUpItem diagnostic hook registered: " .. tostring(hookId))

    preID, postID = RegisterHook(
        "Function /Script/ParadiseKiller.ItemMonitorComponent:OnInventoryItemGained",
        function(Context, affectedActor, itemId)
            local actor = affectedActor:get()

            ConsoleLog("=== Inventory item gained ===")
            ConsoleLog("Item ID: " .. itemId:get():ToString())

            if actor ~= nil then
                ConsoleLog("Affected actor: " .. actor:GetFullName())
                ConsoleLog("Affected class: " .. actor:GetClass():GetFullName())
            else
                ConsoleLog("Affected actor: nil")
            end
        end
    )
    
    RegisterHook(
        "/Game/Assets/Blueprints/Blueprints_Pickups/Blueprint_Pickup_Parent.Blueprint_Pickup_Parent_C:OnRemovedItemFromWorld",
        function(Context)
            local actor = Context:get()

            ConsoleLog("=== Pickup removed from world ===")
            ConsoleLog("Actor: " .. actor:GetFullName())
            ConsoleLog("Class: " .. actor:GetClass():GetFullName())

            local itemData = actor:GetPropertyValue("InventoryItemData")
            if itemData ~= nil then
                ConsoleLog("Item data: " .. itemData:GetFullName())
            end
        end
    )

    local spawnPreID, spawnPostID = RegisterHook(
        "Function /Game/Assets/Blueprints/Blueprints_Pickups/Blueprint_Pickup_Parent.Blueprint_Pickup_Parent_C:OnItemSpawnedBySpawnComponent",
        function(Context, ...)
            local actor = Context:get()
            local level = actor:GetLevel()
            local world = actor:GetWorld()
            local outer = actor:GetOuter()
            ConsoleLog("=== Pickup identity ===")
            ConsoleLog("Actor: " .. actor:GetFullName())
            ConsoleLog("Class: " .. actor:GetClass():GetFullName())

            local itemData = actor:GetPropertyValue("InventoryItemData")
            if itemData ~= nil then
                ConsoleLog("Item data: " .. itemData:GetFullName())
            end

            ConsoleLog("=== Actor hierarchy ===")
            ConsoleLog("Actor: " .. actor:GetFullName())

            if level ~= nil then
                ConsoleLog("Level: " .. level:GetFullName())
            end

            if world ~= nil then
                ConsoleLog("World: " .. world:GetFullName())
            end

            if outer ~= nil then
                ConsoleLog("Outer: " .. outer:GetFullName())
                local outer2 = outer:GetOuter()
                if outer2 ~= nil then
                    ConsoleLog("Outer's outer: " .. outer2:GetFullName())
                end
            end

            ConsoleLog("Actor: " .. actor:GetFullName())
            ConsoleLog("Level: " .. tostring(level))
            ConsoleLog("World: " .. tostring(world))
            local original = actor:GetPropertyValue("InventoryItemData")

            ConsoleLog("Before: " .. original:GetFullName())

            local dummyItemData = StaticFindObject(
                "/Game/Assets/Inventory/ItemData/Collectables/Collectable_DoomJazzWine.Collectable_DoomJazzWine"
            )

            ConsoleLog("Dummy found: " .. tostring(dummyItemData))

            if dummyItemData ~= nil then
                actor:SetPropertyValue("InventoryItemData", dummyItemData)

                local updated = actor:GetPropertyValue("InventoryItemData")
                ConsoleLog("After: " .. updated:GetFullName())
            end

        end

        
    )
    print("Spawn hook IDs: " .. tostring(spawnPreID) .. ", " .. tostring(spawnPostID))
end)