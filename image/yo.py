import cv2
import numpy as np

def calculate_color_percentage(image_path):
    # Load the image
    image = cv2.imread(image_path)
   
    
    # Convert image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_width = 800
    new_height = 600

# Resize the image
    resized_image0= cv2.resize(image, (new_width, new_height))

    

# Save or display the resized image
    
# or
    
  
    
    # Define ranges for colors
    lower_black = np.array([0, 0, 0])   
    upper_black = np.array([0, 0, 30])
    lower_red = np.array([160, 20, 70])
    upper_red = np.array([190,255, 255])
    lower_green =  np.array([25, 50, 80])  
    upper_green = np.array([45, 255, 255]) 



    lower_white = np.array([0,0,200])
    upper_white = np.array([180,20,255])
    lower_dark_brown = np.array([10, 50, 30])   
    upper_dark_brown = np.array([30, 255, 150])
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    lower_yellow = np.array([20, 100, 100])   
    upper_yellow = np.array([30, 255, 255])
    
    # Threshold the HSV image to get only desired colors
   # mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
   # mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
   # mask_black= cv2.inRange(hsv_image, lower_black, upper_black)
   # mask_white = cv2.inRange(hsv_image,lower_white,upper_white)
    mask_yellow = cv2.inRange(hsv_image,lower_yellow,upper_yellow)
    mask_brown = cv2.inRange(hsv_image,lower_dark_brown,upper_dark_brown)

    


    #cv2.imshow('Coloured Image', mask_blue  )
    #cv2.imshow('Coloured Image2',  mask_red  )
    #cv2.imshow('Coloured Image3',mask_white )
    #cv2.imshow('color black',mask_black)
   # cv2.imshow('color green',mask_green)
    resized_image = cv2.resize(mask_yellow, (new_width, new_height))
    resized_image1 = cv2.resize(mask_brown, (new_width, new_height))
    resized_image2 = cv2.resize(mask_green,(new_width,new_height))
    cv2.imwrite('resized_image.jpg', mask_yellow)
    cv2.imwrite('resized_image.jpg', mask_brown)
    cv2.imwrite('resized_image.jpg', resized_image0)
    cv2.imwrite('resized_image.jpg', mask_green)

    cv2.imshow('brown', resized_image1)
    cv2.imshow('yellow', resized_image)
    cv2.imshow(' Image1', resized_image0)
    cv2.imshow("Green",resized_image2)
    

    
    #cv2.imshow('Coloured Image1', image  )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Calculate total number of pixels in the image
    total_pixels = image.shape[0] * image.shape[1]
    
    # Calculate percentage of each color
    #percentage_red = (cv2.countNonZero(mask_red) / total_pixels) * 100
    percentage_green = (cv2.countNonZero(mask_green) / total_pixels) * 100
    #percentage_blue = (cv2.countNonZero(mask_blue) / total_pixels) * 100
    #percentage_white = (cv2.countNonZero(mask_white) / total_pixels)*100
   # percentage_black = (cv2.countNonZero(mask_black) / total_pixels)*100
    percentage_yellow = (cv2.countNonZero(mask_yellow) / total_pixels)*100
    percentage_brown= (cv2.countNonZero(mask_brown) / total_pixels)*100
    
    return  percentage_yellow,percentage_brown,percentage_green

# Example usage
image_path = 'test2.jpg'
yellow_percantage,brown_percantage,green_percentage = calculate_color_percentage(image_path)
#print("Red percentage:", red_percentage)
#print("White percentage:", white_percentage)
#print("Blue percentage:", blue_percentage)
#print("Black percentage:", black_percantage)
print("yellow percentage:", yellow_percantage)
print('brown percentage',brown_percantage)
print("grenn percebtage",green_percentage)



