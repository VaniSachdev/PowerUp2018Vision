import GlobalVariables
import Functions as functions
import cv2

#test
functions.setHSVLimits(GlobalVariables.lower_limit, GlobalVariables.upper_limit)
while(1):
    # setHSVLimits(GlobalVariables.lower_limit, GlobalVariables.upper_limit)
    # HSVColorDetection()
    functions.CannyEdgeDetection(150,250)
    if cv2.waitKey(5) & 0xFF == ord('a'):
        break
    # if cv2.waitKey(5) & 0xFF == ord('a'):
    #     HSVColorDetection()
    # elif cv2.waitKey(5) & 0xFF == ord('b'):
    #     CannyEdgeDetection(100,200)
    # elif cv2.waitKey(5) & 0xFF == ord('c'):
    #     break

cv2.destroyAllWindows()
