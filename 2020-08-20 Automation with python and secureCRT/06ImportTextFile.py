import glob
import os

path = "C:\\Users\\Magnus\\Desktop\\"




def RunCommands(commands):
    #Errorhandling
    if len(commands) < 1:
        #crt.Dialog.MessageBox("no config found")
        return
    
    #Run commands
    for command in commands:
        crt.Screen.Send(command+"\r")
        crt.Screen.WaitForString(command) #Wait for the command is sent



#Open the txt file and as a list
def OpenConfigFile(filename):
    text_file = open(path+filename, "r")
    text_file = text_file.read().splitlines()
    #crt.Dialog.MessageBox(str(text_file))
    return text_file



def main():

    #Get hostname
    prompt = crt.Screen.Get(crt.Screen.CurrentRow, 1, crt.Screen.CurrentRow, 80)
    hostname = prompt.split("#")[0]
    
    #Get a list of txt 
    ListOfFiles = glob.glob(path+ "*.txt")
    #crt.Dialog.MessageBox(str(path))
    
    #Mismatch Counter
    mismatchCounter = 0
    #If hostname match txt file with <hostname>-Input.txt RunCommands
    for file in ListOfFiles:
        file = file.split("\\")[-1]
        if  file.split("-Input.txt")[0] == hostname:    
            #If host matich with filename Exicuted RunCommands with the Config as a list 
            RunCommands(OpenConfigFile(file))
            #Rename the file from -Input to -Exicuted
            #os.rename(file, file.split("-Input.txt")[0]+"-Executed.txt")
        else:
            mismatchCounter += 1

    #crt.Dialog.MessageBox(str(ListOfFiles[0].split("\\")[-1]))
    #crt.Dialog.MessageBox(str(missmatchCounter))
    #crt.Dialog.MessageBox(str(len(ListOfFiles)))

    if len(ListOfFiles) == mismatchCounter:
        crt.Dialog.MessageBox("None file match with "+ hostname + "-Input.txt Found")
        return


main()



