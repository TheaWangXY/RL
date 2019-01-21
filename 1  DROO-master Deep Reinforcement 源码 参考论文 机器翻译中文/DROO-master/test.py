
import numpy as np
list =  np.array([[1,2],[3,4],[7,8]],dtype='int16')
print(list.shape)
print(list[np.newaxis,:].shape)
print(list[:,np.newaxis].shape)