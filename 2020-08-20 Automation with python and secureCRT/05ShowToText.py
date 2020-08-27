

path = "C:\\Users\\Magnus\\Desktop\\"





def main():
    command = crt.Dialog.Prompt ("Which  command shall I run for you Magnus")
    #check user input
    if len(command) < 4:
        crt.Dialog.MessageBox("Not a valid command")
        return


    #Get hostname
    prompt = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 80)
    hostname = prompt.split("#")[0]

    #send commands
    crt.Screen.Send("terminal length 0"+"\r") #Send command
    crt.Screen.Send(command+"\r") #Send command
    crt.Screen.WaitForString(command) #Wait for the command is sent
    strResults = crt.Screen.ReadString(hostname +"#") #Save the output to a variabel
    crt.Screen.Synchronous = False
    

    #save to output to a file
    text_file = open(path + hostname +"-" + command +".txt", "wb")
    text_file.write(strResults)
    text_file.close()    


main()