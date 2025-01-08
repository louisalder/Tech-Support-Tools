# TechSupport-Tools

## About

The software is used to speed up the gathering information element of a technical support ticket. The software extracts machine information such as OS version info, machine specs, installed software, etc. See the below section for full functionality.

The program uses a mix of python libraries, and embedded poweshell scripts to gather the information.

The program was created in 2022 as a project for university. This is no longer being maintained and is provided here as part of my portfolio to showcase a python project. Feel free to explore the code, but please note that it may not be up-to-date with the latest technologies or practices.


### What does the software gather? 

The software currently enables the user to easily gather the following quickly:

1. Hardware info, RAM, CPU, etc.
2. OS Version, build etc.
3. Their port configuration.
4. IP configuration: Network Interface Cards, interface metric etc.
5. Hostname
6. Hosts file info (for systems without DNS)
7. Product versions

The information gathered can be tweaked for your use case and extra functionality can be added in.

Regarding product versions, these are gathered through the use of a powershell script. You can add on additional programs for the tool to scan within the DevProject.py document:

`command = "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object {$_.DisplayName -like '*Python*' -or $_.DisplayName -like '*SQL*' -or $_.DisplayName -like '*.NET*'} | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize"`

For example, you could add the following into the command: `'$_.DisplayName -like '*DaVinci Resolve*'`



## Commandline Vs. Graphical user interface version

The app has a commandline version and a graphical user interface (GUI) version.
The GUI version was created with CustomTKinter, which easily allowed a light and dark mode, and scaling. Credit to TomSchimansky for the package:
https://github.com/TomSchimansky/CustomTkinter

### Commandline version example
<img width="608" alt="image" src="https://github.com/user-attachments/assets/831b7044-f4e4-4371-99b1-c23be5184edc" />

## GUI version example:
## Light mode:
<img width="804" alt="Screenshot 2025-01-08 at 18 35 55" src="https://github.com/user-attachments/assets/b14d8cce-a335-4d6e-bbe9-1283f3b371ca" />

## Dark mode:
<img width="808" alt="image" src="https://github.com/user-attachments/assets/08581776-6ef1-4308-8330-f42bc76f34ed" />

You can customize the GUI by adding in your own images into the application directory, replacing the existing 'light.png' and 'dark.png'.

For a custom icon, add a .ico file to the application directory, go into the MyGUI.py and uncomment the following code:
`gui.wm_iconbitmap("icon.ico")`

# Pre-Requisites:
1. Windows Operating System
2. Tested with Python 3.10
3. The following PIP Packages: PIL, customtkinter, psutil

Please note: The program may need to be ran as an administrator user if anti-virus software is enabled.

# To compile to EXE:
I previously compiled this code to an executable using auto-py-to-exe. This compiles all the packages which are used with the program. Install it with the below link:
https://pypi.org/project/auto-py-to-exe/


## Instructions to end user

End user instructions are contained in the product help file. There is a button available to open this in the GUI version of the app.

### End User guide for the commandline interface:

1. Open the program as an administrator
2. When the command prompt opens, type in 1 to initilise the program
3. Check the application directory and look for the config.txt file
4. Copy the file onto a machine with internet connection if the machine you are using doesn't have access, and send to relevent techsupport team 



### End User guide for the Desktop application:

1. Open the program as an administrator
2. Click on the "Start" button
3. Check the application directory and look for the config.txt file
4. Copy the file onto a machine with internet connection if the machine you are using doesn't have access
5. Open the secure FTP link provided by the engineer at SolutionsPT. If this has not been created yet, contact the engineer who is working on the support case and get them to set this up
6. Enter the provided password
7. Drop and drag, or select the 'upload' button and locate the config.txt file
8. If you have any problems with any of the above steps, please contact the engineer who is working on your support case.

### OS Compatibility:

Windows Server 2016
Windows Server 2019
Windows Server 2022
Windows 10 Enterprise / Professional
Windows 11 Enterprise / Professional
NOTE: The software will not work on Windows 10 Home Edition, as registry keys in this version differ to Enterprise versions of Windows


# Bugs 🪲
Currently, the following methods are commented out as they don't work as expected:
1. Test for IPV6
2. Test for Windows Defender
3. Test for Firewall

# Proposed new features 🔧
1. Support for cross OS
2. Better formatted output file support, i.e., excel spreadsheet with nicely formatted information

# Feedback and Contributions
If you have ideas or find bugs, feel free to open an issue or contribute with a pull request!
