

def main():
    #user input
    command = crt.Dialog.Prompt ("Which command shall I run for you Magnus")
    
    #promt user input
    crt.Dialog.MessageBox(command)

    #Get hostname
    prompt = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 80)
    hostname = prompt.split("#")[0]

    #promt user hostname
    crt.Dialog.MessageBox(hostname)

    #promt session data
    szSessionOption = crt.Session.Config.GetOption("hostname")
    crt.Dialog.MessageBox(szSessionOption)

main()

