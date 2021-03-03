# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with pickle and exceptions
#              When the program starts, load each "row" of data
# ChangeLog (Who,When,What):
# Kevin Scales 3.1.2021,Created script
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
lines = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strStatus = ""  # Captures the status of an processing functions

import pickle

class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file_regular(file_name, lines):
        """ Reads data from a file
        """
        try:
            file = open(file_name, "r")
            lines = file.read()
            file.close()
            return lines, 'Success'
        except (FileNotFoundError):
            return lines, 'Fail'
        return lines, 'BadFail'

    @staticmethod
    def read_data_from_file_encrpyted(file_name, lines):
        """ Reads data from a file
        """

        lines.clear()  # clear current data
        file = open(file_name, "rb")
        lines = pickle.load(file)
        file.close()
        return lines, 'Success'

    @staticmethod
    def write_data_to_file(file_name, lines):

        file = open(file_name, "w")
        for row in lines:
            file.writelines(row)
        file.close()
        return

    @staticmethod
    def add_data_to_list(data, lines):
        lines = lines + "\n" + data
        return lines

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Display a text file
        2) Load and Display a decrypted file
        3) Save a text file 
        4) Encrypt and Save a file
        5) Add a line to current block
        6) Exit Program
        ''')

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')
        print()

    @staticmethod
    def input_new_line():

        #pass

        newdata = input("Newest line of data?: ")
        IO.input_press_to_continue(strStatus)
        return newdata


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
# Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':
        # Basic minimal function. Get the data and send it all to the function.


        text_file_name = input("What is the filename to read, unencrypted? ")
        lines, flag = Processor.read_data_from_file_regular(text_file_name, lines)
        if flag == 'Success':
            print(lines)
        elif flag == 'Fail':
            print("There is no such file")
        else:
            print("Something went really wrong, continue at your own risk.")

        continue  # to show the menu

    elif strChoice == '2':
        pickle_file_name = input("What is the filename to read, encrypted? ")
        file = open(pickle_file_name, "rb")
        lines = pickle.load(file)
        print("encrypted file loaded and extracted\n")
        print(lines)
        file.close()

        continue  # to show the menu

    elif strChoice == '3':  # Save Data to regular text file
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            try:
                text_file_name = input("What is the filename to write? ")
                Processor.write_data_to_file(text_file_name, lines)
                print("File created")
            except(NameError):
                print("There is nothing to save.")
            #except:
             #   print("Something went really wrong, continue at your own risk.")

            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Pickle it
        #Pickle is already its own function. Writing a function to call it seems redundant.
        print(lines)
        pickle_file_name = input("What is the filename to encrypt? ")
        file = open(pickle_file_name, "wb")
        pickle.dump(lines, file)
        print("Consider it pickled.")
        file.close()

        continue  # to show the menu

    elif strChoice == '5': # Add some more data
        data = IO.input_new_line()
        lines = Processor.add_data_to_list(data, lines)

        continue  # to show the menu


    elif strChoice == '6':  # Exit Program
        print("Goodbye!")
        break  # and Exit
