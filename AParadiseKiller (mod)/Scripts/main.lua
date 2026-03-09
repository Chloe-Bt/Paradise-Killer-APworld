print("[AParadiseKiller] loaded")

local UEHelpers = require("UEHelpers")
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
            if class and string.find(class:GetFullName(), "Pickup") then

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







RegisterKeyBind(Key.NINE, { ModifierKey.CONTROL }, function()
    local player = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local item = "Collectable_RottenEgg"
    inventory:GiveItem(FName(item), 100)
    inventory:RemoveItem(FName(item), 100)

    --local knowledge = player.KnowledgeComponent:Get()
    --local info = "Shinji_SweetCheeks"
    --knowledge:GainKnowledge(FName(info))
    --knowledge:LoseKnowledge(FName(info))

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

