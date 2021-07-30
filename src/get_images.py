import glob

class GetImages:
    def __init__(self, directory):
        self.directory = directory
        self.find_pictures()
    
    def find_pictures(self):
        picture_extensions = [
            'jpg', 
            'JPG',
            'png',
            'jpeg',
            'webp',
            'tiff',
            'gif',
            'psd',
            'raw',
            'bmp',
            'heif',
            'svg',]
        self.pictures = []
        [self.pictures.extend(glob.glob(self.directory + '**/*.' + i)) for i in picture_extensions]

    def get_pictures(self):
        if (len(self.pictures) > 0):
            return self.pictures
        else:
            return 1

    def print_data(self):
        print(self.directory)
        print(self.pictures)
