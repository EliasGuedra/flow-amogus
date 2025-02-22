# importing the module 
import cv2 


# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
    global points, img  # Declare points and img as global
    if not points:
        points = 0
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
        # displaying the coordinates 
        # on the Shell 
        print(f"[{x},{y}]")
        points += 1
        # displaying the coordinates 
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, f"{points} ({x},{y})", (x + 20, y + 20), font, 
                    1, (0, 0, 255), 2)
        cv2.circle(img, (x, y), 10, (0, 0, 255), 1) 
        cv2.imshow('image', img) 
  

# driver function
if __name__=="__main__": 
    
    points = 0
    # reading the image 
    img = cv2.imread('filename_0.png', 1) 
  
    # displaying the image 
    cv2.imshow('image', img) 
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 

    cv2.imwrite("calibration_images/api52_calibrated.jpeg", img)
  
    # close the window 
    cv2.destroyAllWindows() 