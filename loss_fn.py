import numpy as np

def l1_loss(y, yhat):
    """ retun the loss function

    Args:
        y (np.array): it is a true value 
        yhat (array): it is a prediction valiue
    """
    loss = np.mean(np.abs(y - yhat))
    
    return loss

def l2_loss(y, yhat):
    """ retun the squar of l1 loss function

    Args:
        y (array): it is a true value  
        yhat (array): it is a prediction value
    """
    
    loss = np.dot((y-yhat),(y-yhat))
    
    return loss

if __name__ == '__main__':
    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    
    l1 = l1_loss(y, yhat)
    l2 = l2_loss(y, yhat)
    
    print(f"L1 Loss : {l1}")
    print(f"L2 loss : {l2}")