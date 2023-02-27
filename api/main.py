import matplotlib.pyplot as plt
from fastapi import FastAPI
import cv2 as cv
import base64
import numpy as np

app=FastAPI()

@app.get("/")
def root():
    # Passing path of image as parameter
    img = cv.imread('/content/gfg.png')
    
    # If the extension of our image was 
    # '.jpg' then we have passed it as 
    # argument instead of '.png'.
    img_encode = cv.imencode('.png', img)[1]
    
    # Converting the image into numpy array
    data_encode = np.array(img_encode)
    
    # Converting the array to bytes.
    byte_encode = data_encode.tobytes()
    
    print(byte_encode)

def create_graph(x=[1,2,3,4,5],y=[5,4,3,2,1]):
    plt.figure(figsize=(4,4))
    plt.plot(x,y)
    plt.savefig("./api/graph.png")
    plt.show()

if __name__=='__main__':
    create_graph()