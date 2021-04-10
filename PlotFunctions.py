import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

def getExampleData(data, pos):
    emotions = {0:'Angry', 1:'Disgust', 2:'Fear', 3:'Happy', 4:'Sad', 5:'Surprise', 6:'Neutral'}
    
    image = np.fromstring(data.loc[pos, 'pixels'], dtype=int, sep=' ')
    image = np.reshape(image, (48, 48)) 
    plt.imshow(image,cmap='gray')
    print("Emotion: "+emotions[data['emotion'][pos]])