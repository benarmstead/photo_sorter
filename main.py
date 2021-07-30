import image_class as ic
import get_images as gi
import move_picture as mp

direc = gi.GetImages("/home/ben/Pictures/")
pictures = direc.get_pictures()

move_class = mp.MovePictures("/home/ben/Pictures/new/")
for i in pictures:
    image_class = ic.ImageClass(i)
    if(image_class.start() == 0):
        move_class.move(image_class)
    image_class.create_extension()
