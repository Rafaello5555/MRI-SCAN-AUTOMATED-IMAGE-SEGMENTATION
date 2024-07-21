


import numpy as np
zip_file_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/o_kRuP_Bk_Pa2xvo1ly63w/data.zip'



#Neural networks often perform better and converge faster when the input data is normalized.
#Normalization involves scaling the pixel values to a standard range, usually between 0 and 1.

"""

#A pixel value of 0 usually represents black, and 255 represents white.
#We normalize image because  pixel values are typically integers ranging from 0 to 255.

*Benefits of Normalization:
Normalization makes the optimization process more stable during training. It helps prevent issues like vanishing or exploding gradients.
It ensures that the features have a similar scale, which can be important for certain optimization algorithms.

*Effect on Neural Network Training:
Neural networks often use activation functions that are most effective when the input values are in a certain range (e.g., the sigmoid or tanh functions).
By normalizing input pixel values to the [0, 1] range, you ensure that the input to the neural network falls within a suitable range for these activation functions.

"""

def normalize(image):

    """Normalize image to be in  range 0 to 1

       Args:
       image: input image

       Returns:
       Normalized image

    """
    return  np.array(image)/255.0


def center_crop(image, output_size):
    """
    Crop the image  from the center 

    Args:
    image: input image
    output_size: The size of output image

    Returns:
    the cropped image
    
    """
    image = np.array(image)
    start_y_coordinate = (image.shape[0] - output_size.shape[0]) // 2    #Remove  leftover space by rows and  crop image on center 
    start_x_coordinate = (image.shape[1] - output_size.shape[1]) // 2. # Remove space by column  and crop image on center


    crop_img = image[]
    















