import sys
import image_class as ic
import get_images as gi
import move_picture as mp

def start_moving(directory, copy_flag):
    direc = gi.GetImages(directory)
    pictures = direc.get_pictures()

    move_class = mp.MovePictures(directory + "new/", copy_flag)
    i = 0
    for i in pictures:
        image_class = ic.ImageClass(i)
        if(image_class.start() == 0):
            move_class.move(image_class)
        image_class.create_extension()

def main():
    arg_len = len(sys.argv)
    print(arg_len)
    if(arg_len < 2):
        print("You must enter a directory!")
        exit()
    copy_flag = False
    for i in range(len(sys.argv)):
        if(sys.argv[i] == "-c"):
            copy_flag = True
    start_moving(sys.argv[1], copy_flag)
main()
