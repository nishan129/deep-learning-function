import numpy as np

def reshape_img(image):
    
    """ This function reshapes the image 
    to return the flaten image shape
    """
    x = image.shape
    img = image.reshape((x[0]*x[1]*x[2],1))
    
    return img

# if __name__ == '__main__':
#     image =  np.array([[[ 0.67826139,  0.29380381],
#                      [ 0.90714982,  0.52835647],
#                      [ 0.4215251 ,  0.45017551]],

#                    [[ 0.92814219,  0.96677647],
#                     [ 0.85304703,  0.52351845],
#                     [ 0.19981397,  0.27417313]],

#                    [[ 0.60659855,  0.00533165],
#                     [ 0.10820313,  0.49978937],
#                     [ 0.34144279,  0.94630077]]])
#     reshape = reshape_img(image)
#     print(f"Image shape is {image.shape}")
#     print(f"Reshape image shape is: {reshape.shape}")