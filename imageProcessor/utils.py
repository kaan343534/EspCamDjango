import cv2

def processImageInput(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30.30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
        
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imwrite(image_path,image)