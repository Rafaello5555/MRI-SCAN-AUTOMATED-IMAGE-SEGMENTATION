
import numpy as np
zip_file_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/o_kRuP_Bk_Pa2xvo1ly63w/data.zip'



#We normalize image because 

def normalize(image):

    """Normalize image to be in  range 0 to 1

       Args:
       image: input image

       Returns:
       Normalized image

    """
    return  np.array(image)/255.0
