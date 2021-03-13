import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def main():
    
    # Read main image
    img = "beach.jpg"
    img = cv2.imread(img)
    
    # Create figure of set size
    figure = plt.figure(figsize=(7, 7))
    
    # Make array with indexes of figure subplots
    arr = [1, 2, 3, 4]
    
    # Iterate to move images around the figure
    while True:
        
        tmp = arr[len(arr) - 1]
        
        for i in reversed(range(0, len(arr))):
            
            if i is 0:
                break
        
            arr[i] = arr[i - 1]
        
        arr[0] = tmp
        
        iterate(img, arr, figure)

# Creates new images at different indexes and
# clears the plot in between
def iterate(img, arr, figure):

    # Conversions from img to different formats
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_HLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    img_GRAY = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2GRAY)

    # Add subplot and show an image at given index
    figure.add_subplot(2, 2, arr[0])
    plt.imshow(img_RGB)
    plt.title("RGB")
    
    # Add subplot and show an image at given index
    figure.add_subplot(2, 2, arr[1])
    plt.imshow(img_HSV)
    plt.title("HSV")

    # Add subplot and show an image at given index
    figure.add_subplot(2, 2, arr[2])
    plt.imshow(img_HLS)
    plt.title("HLS")

    # Add subplot and show an image at given index
    figure.add_subplot(2, 2, arr[3])
    plt.imshow(img_GRAY)
    plt.title("GRAY")
    
    # Pause specified time
    plt.pause(0.1)
    
    # Clear the plot to start over
    plt.cla()
   
if __name__ == "__main__":
    main()