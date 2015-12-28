import cv2
 
def main():
    cap = cv2.VideoCapture(0)
    while True:
       ret, im = cap.read()                                
       temp = cv2.imread("ms_kosakiface.jpg",0)                          
       gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)                  
       w, h = temp.shape[::-1]                                     
       res = cv2.matchTemplate(gray,temp,eval("cv2.TM_CCOEFF"))    
       min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)     
       top_left = max_loc
       bottom_right = (top_left[0] + w, top_left[1] + h)
       cv2.rectangle(im,top_left, bottom_right, (0,0,255), 2)      
       cv2.imshow("Template Matching",im)
       if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break

if(__name__=="__main__"):
    main()
