import os
from json_class import ConvertJsonsFile
from csv_class import ConvertCsvFile


# the program is staring from run_file.py

# class to get user input and check if is valid
class CheckUserInput:
    def __init__(self):
        self.input_name = input("Please enter the name of input file: ")
        self.output_name = input("Please enter the name of output file: ")

    # method to check user input if is with extension csv or json and if the file is existing
    def check_user_input(self):
        if ".json" in self.input_name or ".csv" in self.input_name:
            if os.path.isfile(self.input_name):
                return self.input_name
            else:
                print(f"Sorry , there is no file associated with name {self.input_name}")
        else:
            print("Please choose .csv or .json file extension for input file!")

    # method to check user output file
    def check_user_output(self):
        if ".json" in self.output_name or ".csv" in self.output_name:
            return self.input_name

        return print("Please choose .csv or .json file extension for output file!")


check = CheckUserInput()
CheckUserInput.check_user_input(check)
CheckUserInput.check_user_output(check)

if ".json" in check.input_name:
    json_obj = ConvertJsonsFile(check.input_name, check.output_name)
    ConvertJsonsFile.convert_file(json_obj)
elif ".csv" in check.input_name:
    csv_obj = ConvertCsvFile(check.input_name, check.output_name)
    ConvertCsvFile.convert_file(csv_obj)
