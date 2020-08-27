from datetime import datetime


def main():
    #Run commands and save output to strResults
    crt.Screen.Send("terminal length 0"+"\r") #Send command
    crt.Screen.Send("terminal pager 0"+"\r") #Send command
    crt.Screen.Send("show run"+"\r") #Send command
    crt.Screen.WaitForString("show run") #Wait for the command is sent
    strResults = crt.Screen.ReadString("#") #Save the output to a variabel
    
    
    #Get datetime object containing current date and time
    now = datetime.now()
    #Format the time dd-mm-YY-H-M-S
    dateTime = now.strftime("%d-%m-%Y-%H-%M-%S")

    #Get hostname
    prompt = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 80)
    hostname = prompt.split("#")[0]
    
    #Path
    path = "C:\\Users\\Magnus\\OneDrive - Atea\\SecureCRT\\Backup\\"
    
    
    #save to output to a file
    text_file = open(path + hostname + "-Backup-" + dateTime + ".txt", "w")
    text_file.write(strResults.replace('\n', ''))
    text_file.close()


main()

