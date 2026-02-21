print("[AParadiseKiller] loaded")

local active = false

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

            -- Extract class name
            local className = string.match(fullname, "^[^%s]+")
            if not className then return end

            className = string.gsub(className, "^Blueprint_", "")
            className = string.gsub(className, "_C$", "")

            print("[Location Collected]: " .. className)
        end
    )
end)

RegisterKeyBind(Key.THREE, { ModifierKey.CONTROL }, function()
    RegisterHook(
        "Function /Script/ParadiseKiller.InventoryComponent:PickupItemById",
        function(Context)

            local inv = Context:get()
            if not inv then return end

            local params = Context:get_params()
            if not params then return end

            local itemId = params.ItemId
            print("[BLOCKED PICKUP]:", itemId)

            -- Cancel the function
            return false
        end
    )
end)

ExecuteInGameThread(function()

    local player = FindFirstOf("YMKCharacter")
    if not player then
        print("No player")
        return
    end

    local inventoryWeak = player.InventoryComponent
    if not inventoryWeak then
        print("No inventory weak ptr")
        return
    end

    local inventory = inventoryWeak:Get()
    if not inventory then
        print("Inventory invalid")
        return
    end

    print("Calling GiveItem safely...")

    inventory:GiveItem(FName("Collectable_OLK_Watch"), 1)

end)