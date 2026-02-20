print("[AParadiseKiller] loaded")

local active = false

RegisterKeyBind(Key.ONE, { ModifierKey.CONTROL }, function()
    print("[AParadiseKiller] activated")

    if not active then
        active = true

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
    end
end)
