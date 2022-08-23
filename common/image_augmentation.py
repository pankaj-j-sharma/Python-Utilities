# example of horizontal shift image augmentation
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os 
import cv2


class ImageAugmentation:

    def __init__(self , input_dir=os.getcwd() , save_dir = os.path.join(os.getcwd(),'augmented')) :
          self.input_dir = input_dir
          self.save_dir = save_dir
          self.image_list = []


    def fetch_images(self):
        for dir,_,files in os.walk(self.input_dir):
            for file in files:
                self.image_list.append(os.path.join(dir,file))


    def load_images(self):
        for img in self.image_list:
            loadedimg = load_img(img)
            data = img_to_array(loadedimg)
            yield {'name':os.path.split(img)[-1],'data':data}


    def run_hor_vert_shift_aug(self,no_of_samples=5):
        datagen = ImageDataGenerator(width_shift_range=[-200,200])
        for result in self.load_images():
            samples = expand_dims(result['data'], 0)
            it = datagen.flow(samples, batch_size=1)
            for i in range(no_of_samples):
                batch = it.next()
                img_path = os.path.join(self.save_dir,result['name'])
                print(img_path,'\n')
                cv2.imwrite(img_path,batch)


# # load the image
# img = load_img('bird.jpg')
# # convert to numpy array
# data = img_to_array(img)
# # expand dimension to one sample
# samples = expand_dims(data, 0)
# # create image data augmentation generator
# datagen = ImageDataGenerator(width_shift_range=[-200,200])
# # prepare iterator
# it = datagen.flow(samples, batch_size=1)
# # generate samples and plot
# for i in range(9):
# 	# define subplot
# 	pyplot.subplot(330 + 1 + i)
# 	# generate batch of images
# 	batch = it.next()
# 	# convert to unsigned integers for viewing
# 	image = batch[0].astype('uint8')
# 	# plot raw pixel data
# 	pyplot.imshow(image)
# # show the figure
# pyplot.show()

imgaug = ImageAugmentation(input_dir='D:\POC\ComputerVisionSolution\Datasets\TML Radiator\Whatsapp-Shared')
imgaug.fetch_images()
imgaug.run_hor_vert_shift_aug()