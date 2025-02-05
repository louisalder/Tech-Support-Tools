
import os
import sys
import platform
import socket
import subprocess
import psutil
import re
from io import StringIO
from datetime import datetime


''' 
Some methods such as windows defender and firewall methods are not currently working as required, and are therefore commented out.

'''

def run():
    tool = diagnostic_tool()



class diagnostic_tool:



    def __init__(self, gui):

        """

        Method which allows the gui to be passed to the diagnostic tool class

        :param gui: the gui object


        """

        self.gui = gui
    

    
    def createOutput(self):    

        """
        A method to check if output.txt exists, and delete it if it does and then recreates it
                    
        
        """
        if os.path.exists("output.txt"):
            os.remove("output.txt")
            open("output.txt", "w+")
        else:
            open("output.txt", "w+")

    def write_output(self, machineinfo):

        """
        A method to write to output.txt if it exists, if it doesn't exist it will print an error message

        :param machineinfo: machine information to be written to the file
                    
        
        """

        try:
            with open('output.txt', 'a') as f:
                f.write(machineinfo)

        except FileNotFoundError:
            print("File not found: output.txt")



    
    def storage(self):

        """
        
        A method to get the total storage of the machine in gigabytes
        
        
        """
        storage = psutil.disk_usage('/').total/(2**30)
        print(f"HDD Storage: {storage} Gigabytes")



    
    def powerShellFunction(self, function):

        """
        A method to dynamically run powershell functions. It then prints an output to the console

        ::param function: a list containing the name of the function and the command
        
        """
        
        print(function[0] + os.popen(function[1]).read())



    def dateTime(self):
            
            """
            A method to get the date and time of the machine and print it to the console. it formats it yyyy/mm/dd hh:mm:ss
            
            """
            #get date and time

              
            currentTime = datetime.now()

            formatted_time = currentTime.strftime('%Y/%m/%d %H:%M:%S')

            # Print the formatted date and time
            print('Diagnostic ran at',formatted_time)



    def ram(self):

        '''
        A method to check the ram of the machine. It converts from bytes to megabytes
        
        '''

        # Get total RAM in megabytes
        total_ram = round(psutil.virtual_memory().total/1048576, 1)

        # Get available RAM in megabytes
        available_ram = round(psutil.virtual_memory().available/1048576, 1)

        # Print RAM information
        print(f"Total RAM: {total_ram} Megabytes")
        print(f"Available RAM: {available_ram} Megabytes")


    def architecture(self):

        '''
        A method to find out if the machine is 64 bit or 32 bit

        '''

        # Get the architecture of the machine
        architecture = platform.architecture()

        # Print the architecture
        print(f"Architecture: {architecture}")


    def openOutput(self):



        path = os.path.dirname(os.path.realpath(__file__))

        # Define the locations of the images
        location = os.path.join(path, 'output.txt')

        '''

        A function to open the output.txt file, if it exists when called

        '''

        try:
            print("File Path: " + location)
            os.startfile("output.txt")
            


        except FileNotFoundError:
            print("Error", "Output not found")


    def programs(self):

        '''

        A method which runs a powershell script to get the installed programs - including .NET, SQL, etc. 
        Modify powershell script with added: $_.DisplayName -like '*EXAMPLE PROGRAM*' 

        '''


        command = "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object {$_.DisplayName -like '*Python*' -or $_.DisplayName -like '*SQL*' -or $_.DisplayName -like '*.NET*'} | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize"

        process = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True,
            text=True
        )

        pattern = re.compile(r'SQL|\.NET')

        output = process.stdout

        for line in output.split('\n'):
            if pattern.search(line):
                print(line)



    def ports(self):

        '''
        A method to check the ports using 'netstat -aon' powershell script. This prints it too

        '''
        output = subprocess.check_output(["netstat", "-aon"])
        print(output.decode())



    def hostname(self):

        '''
        A method to check the hostname using socket.gethostname(). This prints it too
        
        '''

        hostname = socket.gethostname()
        print("Hostname: " + hostname)


    def create_text_output(self):

        '''

        A method to create a file called diagnostic.txt and allow the user to write to it

        '''

        with open("Diagnostic.txt", "w") as file:
            file.write("Diagnostic Test ")
            print('File created')

    def hostsfile(self):

        '''
        A method to check the hosts file. It should skip any lines that are commented out of the hosts file with '#' at the start.
        
        '''
        print("Hostsfile: \n")
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

        with open(hosts_path, "r") as hosts_file:
            for line in hosts_file:
                if line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) > 1:
                    ip_address = parts[0]
                    hostnames = parts[1:]
                    print(
                        f"IP address: {ip_address}, Hostnames: {', '.join(hostnames)}")
                elif len(parts) <1 :
                    print("No hostnames found")

    #method which checks if ipv6 is enabled
    def ipv6(self):
        '''
        A method to check if IPv6 is enabled using the socket.has_ipv6 attribute. It will print whether it is enabled or not depending on if the value is true or false.
        
        '''

        isEnabled = socket.has_ipv6
        if isEnabled == True:
            print("IPv6 is enabled")
        else:
            print("IPv6 is not enabled")

    # method which gets the number of cores on the 
    def cores(self):

        '''
        A method to detect the number of cores via the psutil library. It will print the number of cores & Physical cores too
        
        '''

        print(f"Number of cores: {psutil.cpu_count()}")
        print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")


    def os_version(self):

        '''
        A method to check the specicic OS build, version, release and name. It will print all of these.
        
        
        '''

        os_name = platform.system()
        os_release = platform.release()
        os_version = platform.version()
        os_build = platform.platform()

        print('Windows Version details:')
        print(f"OS name: {os_name}")
        print(f"OS release: {os_release}")
        print(f"OS version: {os_version}")
        print(f"OS build: {os_build}")




  
    def internet(self):

        '''
        A method which checks if the machine is connected to the internet. It does this by creating a connection to google with the socket library. It prints the internet status
        
        '''
        try:
           
            socket.create_connection(("www.google.com", 80))
            print("Internet connected.")
        except OSError:
            pass
            print("Internet not connected.")



   
     #def firewall(self):

        #This method doesn't properly work and needs tweaking
    #  try:
     #        output = subprocess.check_output(
       #          "netsh advfirewall show allprofiles state", shell=True)
       #      if "State ON" in output.decode():
       #          print("Windows firewall is enabled.")
        #     else:
        #         print("Windows firewall is disabled.")
        # except subprocess.CalledProcessError:
        #     print("Failed to check the Windows firewall status.")

    


    def openHelpfile(self):

        """

        A method which opens the help files. It uses a try catch block in case the file is missing
        
        """
        try:
            os.startfile("help.html")
        except FileNotFoundError:
            print("Error", "Helpfile not found")


    # a method which opens a local file surrounded by a try/catch block
    # if the file is not found, it will display an error message
    # if the file is found, it will open the file


    def openTCfile(self):

        """
        A method which opens the product terms. Similar to the helpfile method. It will throw an error if the file can't be found as it is surrounded with a try catch

        """
        try:
            os.startfile("TC.html")
        except FileNotFoundError:
            print("Error", "Helpfile not found")


    def storeString(self, string):

        '''

        A method which stores a string in a variable. This is used in the program to store the output to the console into a string. It then is written to the txt file.

        '''

        self.string = string
        return string

    def __init__(self, gui):

        # some powershell scripts stored in strings
        interface = 'interface metric: \n', 'netsh interface ipv4 show interface'
        cpu = 'CPU ', 'wmic cpu get Name'
        user = 'Logged in user: ', 'whoami'
        user_groups = 'User Groups: ', 'whoami /groups'
        ip = 'IP Address: ', 'ipconfig'
        taskList = 'TaskLists & PIDs', 'tasklist'



        # an ascii logo which is displayed at the top of the command interface. Just to make it look cool
        logo = """ ___        __          ____       _   _                        
|_ _|_ __  / _| ___    / ___| __ _| |_| |__   ___ _ __ ___ _ __ 
 | || '_ \| |_ / _ \  | |  _ / _` | __| '_ \ / _ \ '__/ _ \ '__|
 | || | | |  _| (_) | | |_| | (_| | |_| | | |  __/ | |  __/ |   
|___|_| |_|_|  \___/   \____|\__,_|\__|_| |_|\___|_|  \___|_|   
  __ _ _ __   __| |                                             
 / _` | '_ \ / _` |                                             
| (_| | | | | (_| |                                             
 \__,_|_| |_|\__,_|                                             """

        programName = """  ____  _                             _   _        _              _ 
 |  _ \(_) __ _  __ _ _ __   ___  ___| |_(_) ___  | |_ ___   ___ | |
 | | | | |/ _` |/ _` | '_ \ / _ \/ __| __| |/ __| | __/ _ \ / _ \| |
 | |_| | | (_| | (_| | | | | (_) \__ | |_| | (__  | || (_) | (_) | |
 |____/|_|\__,_|\__, |_| |_|\___/|___/\__|_|\___|  \__\___/ \___/|_|
                |___/                                               """
        


        version = 3.0




        if gui:
            # code to run if gui is true
            print("GUI mode")

            self.createOutput()

            print("Running Diagnostic ...")
            # Save the original stdout
            original_stdout = sys.stdout

            # Create a StringIO object to capture the output
            output = StringIO()
            sys.stdout = output

            # Print something to the console
            
            #machine specific information
            self.dateTime()
            self.hostname()
            self.ram()
            self.powerShellFunction(cpu)
            self.cores()
            self.architecture()
            self.storage()
            self.internet()

            print('\n')
            self.os_version()
            print('\n')


            #installed programs
            print('\nInstalled Programs: \n')
            self.programs()

            #user information
            self.powerShellFunction(user)
            self.powerShellFunction(user_groups)
        


            #Networking methods
            #self.firewall()            
            self.powerShellFunction(interface)
            self.powerShellFunction(ip)

            self.ipv6()

            self.ports()
            self.powerShellFunction(taskList)
            

            self.hostsfile()


            sys.stdout = original_stdout
            output_string = output.getvalue()

            print(output_string)
            self.storeString(output_string)
            self.write_output(output_string)


        

        else:

            # code to run if commandline program runs


            print(logo)
            print(programName)
            print("Welcome to the Info Gatherer and Diagnostic Tool")
            print('version:', str(version))


            print('By using the software, you are agreeing to the terms and conditions')
            pass 
            while True:
                # Print menu options
                print("Select an option by entering a value from 1-4: \n")
                print("1. Run Diagnostic")
                print("2. Open Helpfiles")
                print("3. Open Terms and Conditions")
                print("4. Close Program")

                # Get user input
                choice = input("\n Enter choice: \n")

                # Use if statements to execute chosen option
                if choice == "1":

                    print("Running Diagnostic ...")
                
                    # Save the original stdout
                    original_stdout = sys.stdout

                    # Create a StringIO object to capture the output
                    output = StringIO()
                    sys.stdout = output

                    # Print something to the console
                    
                    
                    #machine specific information
                    self.dateTime()
                    self.hostname()
                    self.ram()
                    self.powerShellFunction(cpu)
                    self.cores()
                    self.architecture()
                    self.storage()
                    self.internet()

                    #user information
                    self.powerShellFunction(user)
                    self.powerShellFunction(user_groups)
                


                    #Networking methods
                    #windows_defender()
                    #self.firewall()            
                    self.powerShellFunction(interface)
                    self.powerShellFunction(ip)

                    self.ipv6()

                    self.ports()
                    self.powerShellFunction(taskList)
                    


                    #installed programs
                    self.programs()
                    #self.windows_defender()
                    self.uac()
                    self.hostsfile()

                    # Restore the original stdout and get the output as a string
                    sys.stdout = original_stdout
                    output_string = output.getvalue()

                    print(output_string)
                    self.write_output(output_string)

                    print("Diagnostic complete")
                    print("Output saved to output.txt")
                    print('Opening output.txt...')
                    self.openOutput()
                    




                elif choice == "2":
                    print("Opening helpfile")
                    self.openHelpfile()

                elif choice == "3":
                    print("Opening Terms and conditions")
                    self.openTCfile()

                elif choice == "4":
                    print("Closing program...")
                    break

                else:
                    print("Invalid input")
                pass
        
        
    def close(self):
       
        '''
        A method which terminates the program if the user selects to close the program with option 4
        
        '''

        pass

       
