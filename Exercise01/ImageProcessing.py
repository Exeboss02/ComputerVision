import cv2
from IPython.display import display, Markdown

def ReadAndDisplayImage(path, title):
    image = cv2.imread(path)
    
    if image is None:
        print(f"Error: Could not read image at {path}")
        return
    
    #image = cv2.resize(image, (1280, 720))
    width, height, channels = image.shape
    type = image.dtype
    #cv2.cvtColor()

    cv2.imshow(title, image)
    sizeString = "## Size: w =" + str(width) + " h =" + str(height)
    channelsString = "## Channels: " + str(channels)
    formatString = "## Format: " + str(type)
    
    display(Markdown(sizeString))
    display(Markdown(channelsString))
    display(Markdown(formatString))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def GrayScaleImage(path, title):
    image = cv2.imread(path)
    
    if image is None:
        print(f"Error: Could not read image at {path}")
        return
    
    cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Test():
    print("--TESTING TESTING--")