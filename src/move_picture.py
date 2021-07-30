import os
import shutil

class MovePictures:
    def __init__(self, directory, copy_flag):
        self.copy_flag = copy_flag
        self.new_directory = directory
        self.make_if_not_exist(directory)

    def make_if_not_exist(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def move(self, image_class):
        year      = image_class.year
        self.make_if_not_exist(self.new_directory + '/' + year)

        final_path = self.new_directory + '/' + year + '/' + image_class.converted_name
        self.file_path = image_class.file_path
        self.try_move(final_path, 0, image_class)

    def try_move(self, final_path, count, image_class):
        if(os.path.exists(final_path) == False):
            if(self.copy_flag == True):
                shutil.copy(self.file_path, final_path)
            else:
                shutil.move(self.file_path, final_path)
        else:
            print('Image name exists. Attempting new name.')
            count += 1
            self.try_move(self.new_directory + '/' + image_class.year + '/' + image_class.date_filename + '-' + str(count) + image_class.extension.lower(), count, image_class)
