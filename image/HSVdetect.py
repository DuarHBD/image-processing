import cv2
import numpy as np
import matplotlib.pyplot as plt 

def calculate_color_percentage(image_path,):
    # Load the image
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    new_width = 600
    new_height = 400
 # Define ranges for colors
    lower_black = np.array([0, 0, 0])   
    upper_black = np.array([179, 50, 50])
    lower_red = np.array([160, 20, 70])
    upper_red = np.array([190,255, 255])
    lower_green =  np.array([25, 50, 80])  
    upper_green = np.array([45, 255, 255]) 



    lower_white = np.array([0, 0, 150])
    upper_white = np.array([179, 50, 255])
    lower_dark_brown = np.array([0, 0, 00])   
    upper_dark_brown = np.array([180, 255, 150])
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    lower_yellow = np.array([17, 60, 80])   
    upper_yellow = np.array([30, 255, 255])
    
 
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
   
    mask_white = cv2.inRange(hsv_image,lower_white,upper_white)
    mask_yellow = cv2.inRange(hsv_image,lower_yellow,upper_yellow)
    mask_brown = cv2.inRange(hsv_image,lower_dark_brown,upper_dark_brown)
    resized_image0= cv2.resize(image, (new_width, new_height))
    resized_image1 = cv2.resize(mask_brown, (new_width, new_height))
    resized_image2 = cv2.resize(mask_white,(new_width,new_height))
    resized_image3 = cv2.resize(mask_yellow,(new_width,new_height))
    resized_image4= cv2.resize(mask_green,(new_width,new_height))
   
    total_pixels = image.shape[0] * image.shape[1]
    
    # Calculate percentage of each color
    #percentage_red = (cv2.countNonZero(mask_red) / total_pixels) * 100
    percentage_green = (cv2.countNonZero(mask_green) / total_pixels) * 100
    #percentage_blue = (cv2.countNonZero(mask_blue) / total_pixels) * 100
    percentage_white = (cv2.countNonZero(mask_white) / total_pixels)*100
    #percentage_black = (cv2.countNonZero(mask_black) / total_pixels)*100
    percentage_yellow = (cv2.countNonZero(mask_yellow) / total_pixels)*100
    percentage_brown= (cv2.countNonZero(mask_brown) / total_pixels)*100
    Total =percentage_brown+percentage_yellow+percentage_white+percentage_green
    cv2.putText(resized_image0,f"percent of brownig:    {(percentage_brown/Total)*100:.2f}%",(8,20),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),2)
    cv2.putText(resized_image1,"Detect Brown Color",(8,20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
    cv2.putText(resized_image2,f"Detect white Color:    {percentage_white/Total*100:2f}%",(8,20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
    cv2.putText(resized_image3,"Detect yellow Color",(8,20),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
    images = [resized_image0, resized_image1, resized_image2, resized_image3,resized_image4]
    titles = ['Original Image', 'Brown Color', 'White Color', 'Yellow Color',"Green color"]

    plt.figure(figsize=(10, 10)) 

    for i in range(len(images)):  
        plt.subplot(3, 2, i + 1)  
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  
        plt.title(titles[i])  
        plt.axis('off')  
   
    plt.tight_layout() 
    plt.savefig('color_analysis_result.png')
    plt.show()

    
    return  percentage_brown,percentage_yellow,percentage_white,percentage_green

# Example usage
image_path = 'img/D10/10.png'
brown_percantage, yellow_percantage,white_percentag ,green_percen= calculate_color_percentage(image_path)
Total =brown_percantage+yellow_percantage+white_percentag+green_percen
print("White percentage:", white_percentag/Total*100)
print("yellow percentage:", yellow_percantage/Total*100)
print('brown percentage',brown_percantage/Total*100)
print('green percentage',green_percen/Total*100)

percent=((brown_percantage+white_percentag)/Total)*100
print("percent of browing",percent,"%")




