import os.path
from PIL import Image
from PIL.ExifTags import TAGS

class ImageClass:
    # Variables
    # file_path     : Full path to the image
    # date          : Raw date extracted from file
    # year          : Year of creation
    # date_filename : Date in a format to be used in the filename
    # extension     : File extension

    def __init__(self, file_path):
        self.file_path = file_path

    def start(self):
        if(self.error_check(self.check_file_exists()) == 1):
            return 1
        if(self.error_check(self.set_date()) == 1):
            return 1
        if(self.error_check(self.refine_date()) == 1):
            return 1
        self.create_extension()
        self.create_date_filename()
        self.create_converted_name()
        return 0

    def check_file_exists(self):
        if os.path.isfile(self.file_path):
            return 0
        else:
            return self.file_path + " does not exist."

    def set_date(self):
        try:
            self.date = Image.open(self.file_path).getexif().get(306)
            return 0
        except:
            self.date = "Unknown"
            return "Cannot find date in " + self.file_path

    def refine_date(self):
        try:
            temp = self.date[:4]
        except:
            return "Could not refine date for " + self.file_path

        if(str(temp).isnumeric() == True and int(temp) > 0):
            self.year = temp
            return 0
        else:
            return "Could not refine date for " + self.file_path
    
    def create_extension(self):
        self.extension = os.path.splitext(self.file_path)[-1]

    def create_date_filename(self):
        self.date_filename = self.date.replace(':', '').replace(' ', '-')

    def create_converted_name(self):
        self.converted_name = self.date_filename + self.extension.lower()

    def error_check(self, return_value):
        if(return_value == 0):
            return 0
        else:
            print("Error: " + return_value)
            return 1
