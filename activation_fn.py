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
  
  
def softmax(data):
    """Write a softmax activation function that returns probabilities multi classification

    Args:
        data (_type_): int, list , array of multi class

    Returns:
        probabilties: return probability of each class
    """
    
    x_exp = np.exp(data)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    x_s = x_exp / x_sum 
    
    return x_s 
    
if __name__ == '__main__':
    data = np.array([1, 2, 3, 4])
    t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0 ,0]])
    sig = sigmoid(data=data)
    sof = softmax(data=t_x)
    print("*"*100)
    print(f"Sigmoid result: {sig}")
    print("*"*100)
    print(f"Softmax result: {sof}")
    print("*"*100)
        
