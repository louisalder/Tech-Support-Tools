import tkinter
import customtkinter
import os
import DevProject
import webbrowser
from PIL import Image


# This file uses customTKinter as a package to design the gui.
# Inspiration was taken from the creator of the customTkinter package and specifically the complex example. This was modified to fit my requirements.
# The package can be downloaded here: https://github.com/TomSchimansky/CustomTkinter
# The complex example can be found here: https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/complex_example.py




customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

path = os.path.dirname(os.path.realpath(__file__))

osFilePath = os.path.join(path, 'output.txt')

information = "Welcome to the Diagnostic Tool \n \nThis tool was designed to gather information from your machine to speed up the process of support cases. It uses read only, and will not make any modifications to the machine\n \nTo run the tool, simply click the below button. Once completed, a popup will appear, where you can open the output.txt file. \n \n File Path for output: \n" + osFilePath + "\n \nUpload the output.txt file to the Secure FTP site provided \n \n If you have any problems, please contact the Support Engineer who is assisting you with the case."


def runDiagnostic():
        """
        A function to run the diagnostic tool when called
        
        """
        tool = DevProject.diagnostic_tool(True)
        completeDiagnostic()



        

def openWebsite():

    """
    A function to open a specific user website with button
    
    """
    webbrowser.open("https://github.com/louisalder/TechSupport-Tools/")


def openOutputfile():

    """

    A function to open the output.txt file, if it exists when called

    """

    try:
        os.startfile("output.txt")
    except FileNotFoundError:
        print("Error", "Output not found")


def appearance_mode(selected_theme):

    """

    A function to change the appearance mode via the dropdown box in the menu bar

    """

    customtkinter.set_appearance_mode(selected_theme)

class versionPopup(customtkinter.CTkToplevel):
    def __init__(gui, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """
        
        A class to create a popup window when the version button is clicked
        
        
        """
        gui.grid_columnconfigure(0, weight=1)
        gui.grid_columnconfigure(1, weight=1)

        gui.popup_frame = customtkinter.CTkFrame(gui)
        gui.popup_frame.grid(row=0, column=0, rowspan=1, columnspan=2, sticky="nsew")

        gui.popup_frame.grid_columnconfigure(0, weight=1)
        gui.popup_frame.grid_rowconfigure(0, weight=1)

        gui.label = customtkinter.CTkLabel(gui.popup_frame, text="Version: 3.0")
        gui.label.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        gui.closebutton = customtkinter.CTkButton(gui.popup_frame, text="close", command=gui.destroy)
        gui.closebutton.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        gui.geometry("200x200")
        gui.title("Version")




class completeDiagnostic(customtkinter.CTkToplevel):
    def __init__(gui, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #create the gui
        gui.grid_columnconfigure(0, weight=1)
        gui.grid_columnconfigure(1, weight=1)

        #create a frame
        gui.popup_frame = customtkinter.CTkFrame(gui)
        gui.popup_frame.pack()

        gui.popup_frame.grid_columnconfigure(0, weight=1)
        gui.popup_frame.grid_rowconfigure(0, weight=0)
        gui.popup_frame.grid_rowconfigure(1, weight=1)
        gui.popup_frame.grid_rowconfigure(2, weight=0)

        # add the label
        gui.popup_label = customtkinter.CTkLabel(gui.popup_frame, text="Complete!", font=("TkDefaultFont", 14, "bold"), pady=10)
        gui.popup_label.grid(row=0, column=0, sticky="nsew")

        location = os.path.join(path, 'output.txt')

        gui.title("Diagnostic Complete")

        #create a button to open the file
        gui.openfile = customtkinter.CTkButton(gui.popup_frame, text="Open File", command=openOutputfile)
        gui.openfile.grid(row=1, column=0, padx=20, pady=20)

        gui.closebutton = customtkinter.CTkButton(gui.popup_frame, text="Close", command=gui.destroy)
        gui.closebutton.grid(row=2, column=0, padx=20, pady=20)

        gui.geometry("200x200")



class App(customtkinter.CTk):




    def __init__(gui, *args, **kwargs):
        super().__init__(*args, **kwargs)


        

        gui.toplevel_window = None   
        gui.appearance_mode = customtkinter.get_appearance_mode()

        # configure window
        gui.title("Info gatherer & Diagnostic tool")
        gui.geometry(f"{800}x{400}")

         #Insert custom icon with below code
         # gui.wm_iconbitmap("icon.ico")


        
        # configures a 4x4 grid layout for the entire app
        gui.grid_columnconfigure(1, weight=1)
        gui.grid_columnconfigure((2, 3), weight=0)
        gui.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        gui.sidebar_frame = customtkinter.CTkFrame(gui, width=200, corner_radius=0)
        gui.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        gui.sidebar_frame.grid_rowconfigure(4, weight=1)

        # label for sidebar
        gui.menu_label = customtkinter.CTkLabel(gui.sidebar_frame, text="Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        gui.menu_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # button for version
        gui.sidebar_button_1 = customtkinter.CTkButton(gui.sidebar_frame, text="Version", command=gui.open_toplevel)
        gui.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        # button for T&C
        gui.sidebar_button_2 = customtkinter.CTkButton(gui.sidebar_frame, text="Terms & Conditions", command=gui.openTCfile)
        gui.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # button for help
        gui.sidebar_button_3 = customtkinter.CTkButton(gui.sidebar_frame, text="Help", command=gui.openHelpfile)
        gui.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # appearance mode settings
        gui.appearance_mode_label = customtkinter.CTkLabel(gui.sidebar_frame, text="Appearance Mode:", anchor="w")
        gui.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        gui.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(gui.sidebar_frame, values=["System", "Light", "Dark"],  command=lambda selected_theme: appearance_mode(selected_theme))


        gui.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        # scaling mode settings
        gui.scaling_label = customtkinter.CTkLabel(gui.sidebar_frame, text="UI Scaling:", anchor="w")
        gui.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        gui.scaling_optionemenu = customtkinter.CTkOptionMenu(gui.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=gui.scaling)
        gui.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        gui.scaling_optionemenu.set("100%")

        # creating main UI frame which consumes the rest of the window


        paddingx =20
        paddingy = 10 


        # add the image button
        path = os.path.dirname(os.path.realpath(__file__))
        light_imagepath = os.path.join(path, 'light.png')
        dark_imagepath = os.path.join(path, 'dark.png')
        getIcon = os.path.join(path, 'icon.ico')


        gui.main_frame = customtkinter.CTkFrame(gui, corner_radius=10)

        gui.main_frame.grid(row=0, column=1, rowspan=5, columnspan=3, sticky="nsew", padx=20, pady=10)


        def update_main_frame_width(event):

            """
            A function which updates the frame in real time as the window is resized. This modifies the image on the button and its size so tht it looks correct
            """
            main_frame_width = event.width
            #displays the smallest logo if the width is less than 1075
            if main_frame_width < 1075:
                
                my_image = customtkinter.CTkImage(light_image=Image.open(getIcon), dark_image=Image.open(getIcon), size=(50, 50))
                button = customtkinter.CTkButton(gui.main_frame, image=my_image, text='Solutions', compound='right', font=('Helvetica', 30, 'italic'), bg_color='transparent', command=openWebsite, width=493, height=90)
                button.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

            #if the width is between 1075 and 1350, the image will be smaller
            elif main_frame_width >= 1075 and main_frame_width < 1350:

                my_image = customtkinter.CTkImage(light_image=Image.open(light_imagepath), dark_image=Image.open(dark_imagepath), size=(542, 99))
                button = customtkinter.CTkButton(gui.main_frame, image=my_image, text=None, fg_color='transparent', bg_color='transparent', command=openWebsite)
                button.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
            # if the width is greater than 1350, the image will go bigger
            else:
                my_image = customtkinter.CTkImage(light_image=Image.open(light_imagepath), dark_image=Image.open(dark_imagepath), size=(721, 132))
                button = customtkinter.CTkButton(gui.main_frame, image=my_image, text=None, fg_color='transparent', bg_color='transparent', command=openWebsite)
                button.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")


        
        gui.main_frame.bind("<Configure>", update_main_frame_width)

        # configure main_frame grid layout
        for i in range(5):
            gui.main_frame.grid_rowconfigure(i, weight=1)
        for i in range(3):
            gui.main_frame.grid_columnconfigure(i, weight=1)






        # adds the text box containing the program information, file path for output, etc. 
        gui.main_textbox = customtkinter.CTkTextbox(gui.main_frame, wrap='word')
        gui.main_textbox.grid(row=1, column=0, rowspan=3, columnspan=3, sticky="nsew", padx=10)
        gui.main_textbox.insert(customtkinter.END, information)

        # add the run diagnostic button
        gui.main_button = customtkinter.CTkButton(gui.main_frame, text="Run Diagnostic", command=runDiagnostic)
        gui.main_button.grid(row=4, column=0, columnspan=3, padx=paddingx, pady=10, sticky="nsew")






    def scaling(gui, picked_scaling: str):

        """

        A method which can be used to modify UI scaling. This is used by the option box in the gui

        :param picked_scaling: The value which has been picked by the user

        """

        new_scaling_float = int(picked_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def open_toplevel(gui):
        if gui.toplevel_window is None or not gui.toplevel_window.winfo_exists():
            gui.toplevel_window = versionPopup(gui)  # create window 
        else:
            gui.toplevel_window.focus()  





    def openHelpfile(gui):

        """

        A method which opens the help files. It uses a try catch block in case the file is missing

        
        """

        try:
            os.startfile("help.html")
        except FileNotFoundError:
            print("Error", "Helpfile not found")



    def openTCfile(gui):

        """
        A method which opens the product terms. Similar to the helpfile button. It will throw an error if the file can't be found as it is surrounded with a try catch

        """
        try:
            os.startfile("TC.html")
        except FileNotFoundError:
            print("Error", "Helpfile not found")

    







if __name__ == "__main__":
    app = App()
    app.mainloop()

