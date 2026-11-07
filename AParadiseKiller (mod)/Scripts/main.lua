print("[AP] mod loaded")
require("archipelago")

local DEBUG     = false
UEHelpers       = require("UEHelpers")
ConsoleAr       = nil

if DEBUG then
    require("debug functions")
end

RegisterConsoleCommandHandler("/connect", function(FullCommand, userInput, Ar)
    local host, slot, password = FullCommand:match('/connect%s+(%S+)%s+"(.-)"%s+"(.-)"')

    if not host or not slot then
        host, slot =
            FullCommand:match('/connect%s+(%S+)%s+"(.-)"')
        password = ""
    end

    if not host or not slot then
        LogToConsole("Usage: /connect <host> \"<slot>\" [\"password\"]")
        return
    end
    password = password or ""

    LogToConsole("[AP] Trying to connect to " .. host .. " with slot " .. slot .. " and password " .. password)
    connectToAp(host, slot, password)
    
    return true
end)

RegisterConsoleCommandHandler("/disconnect", function(FullCommand, userInput, Ar)
    disconnect()

    return true
end)

RegisterConsoleCommandHandler("/message", function(FullCommand, userInput, Ar)
    SendMessage(tostring(FullCommand:sub(10)))

    return true
end)
RegisterConsoleCommandHandler("/say", function(FullCommand, userInput, Ar)
    SendMessage(tostring(FullCommand:sub(6)))

    return true
end)

RegisterConsoleCommandHandler("/exile", function(FullCommand, userInput, Ar)
    LogToConsole("[AP] Sending you back to exile.")

    local player = FindFirstOf("YMKCharacter")
    local loc = player:K2_GetActorLocation()
    
    loc.X = -70813.0
    loc.Y = 8788.0
    loc.Z = 73152.2734375

    player:K2_SetActorLocation(loc, false, {}, false)

    return true
end)

RegisterConsoleCommandHandler("/blood", function(FullCommand, userInput, Ar)
    LogToConsole("Here, have a blood offering.")

    local player = FindFirstOf("YMKCharacter")
    local inventory = player.InventoryComponent:Get()
    local item = "GoldCoin_001"

    inventory:RemoveItem(FName(item), 1)
    inventory:GiveItem(FName(item), tonumber(userInput[1]))
    inventory:RemoveItem(FName(item), 1)

    return true
end)

RegisterConsoleCommandHandler("/deathlink", function(FullCommand, userInput, Ar)
    ToggleDeathlink()

    return true
end)