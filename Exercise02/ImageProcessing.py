import cv2
from IPython.display import display, Markdown

def ReadAndDisplayImage(path, title, reasonableResize):
    image = cv2.imread(path)
    
    if image is None:
        print(f"Error: Could not read image at {path}")
        return
    
    width, height, channels = image.shape
    type = image.dtype
    #cv2.cvtColor()
    
    if reasonableResize:
        image = cv2.resize(image, (int(width / 4), int(height / 4)))

    cv2.imshow(title, image)
    sizeString = "## Size: w =" + str(width) + " h =" + str(height)
    channelsString = "## Channels: " + str(channels)
    formatString = "## Format: " + str(type)
    
    display(Markdown(sizeString))
    display(Markdown(channelsString))
    display(Markdown(formatString))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image
    
def GrayScaleImage(path, title, reasonableResize):
    image = cv2.imread(path)
    width, height, channels = image.shape
    
    if image is None:
        print(f"Error: Could not read image at {path}")
        return
    
    if reasonableResize:
        image = cv2.resize(image, (int(width / 4), int(height / 4)))
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image

def HSVImage(path, title, reasonableResize):
    image = cv2.imread(path)
    width, height, channels = image.shape
    
    if image is None:
        print(f"Error: Could not read image at {path}")
        return
    
    if reasonableResize:
        image = cv2.resize(image, (int(width / 4), int(height / 4)))
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return image
    
def DisplayImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def Test():
    print("--TESTING TESTING--")