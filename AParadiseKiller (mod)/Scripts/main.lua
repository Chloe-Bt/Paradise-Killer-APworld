print("[AParadiseKiller] loaded")

require "archipelago"

local DEBUG = false
ConsoleAr   = nil
UEHelpers   = require("UEHelpers")

if DEBUG then
    require "debug"
end


RegisterConsoleCommandHandler("/connect", function(FullCommand, userInput, Ar)
    print("Calling /connect")
    Ar:Log("Calling /connect")
    
    ConsoleAr = Ar

    Connect(FullCommand, userInput, Ar)

    ConsoleAr:Log("finished Calling /connect")
    return true
end)

RegisterConsoleCommandHandler("/disconnect", function(FullCommand, userInput, Ar)
    print("Calling /disconnect")
    Ar:Log("Calling /disconnect")

    disconnect()

    ConsoleAr:Log("finished Calling /disconnect")

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

