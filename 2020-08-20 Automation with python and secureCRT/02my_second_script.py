commands = ["show ip int brie", "show cdp nei", "show int des"]

#run commands
for command in commands:
    crt.Screen.Send(command + "\r") 