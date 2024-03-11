import numpy as np


    
def sigmoid(data):
    
    """ Write a sigmoid activation function that returns probabilities of -10 to 10

    Args:
        data (_type_): is a list array of a int
            
    Returns:
        the probability
        formula of sigmoid
        1/(1 + e^x)
        """
    s = 1/(1 + np.exp(data))
        
    return s 
    
    
if __name__ == '__main__':
    data = np.array([1, 2, 3, 4])
    
    sig = sigmoid(data=data)
    print(sig)
        
