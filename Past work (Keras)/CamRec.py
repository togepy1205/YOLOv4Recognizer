# By cam

def cam_recognizer(register_id):
    import cv2
    import numpy as np
    from PIL import Image
    from keras import models
    import customerinfo

    # customer ID
    # UID = customerinfo.check_register(register_id)
    UID = 'afsdfasdm1155'
    
    # Cart Container
    cart = []
    result = [UID]

    # MOG2
    bs = cv2.createBackgroundSubtractorMOG2()

    #Load the saved model
    model = models.load_model('CNN_model_ABCD_well_1.h5')
    product = {0:'Apple', 1:'Banana', 2:'Chocolate', 3:'Doritos'}

    # open cam
    cap = cv2.VideoCapture(0)
    ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    WIDTH = 400
    HEIGHT = int(WIDTH / ratio)


    while(cap.isOpened()):     # 以迴圈從影片檔案讀取影格，並顯示出來
        ret, frame = cap.read()
        frame = cv2.resize(frame, (WIDTH, HEIGHT))
    #     frame = cv2.flip(frame, 1) # 水平翻轉畫面

        gray = bs.apply(frame)   # 演算法中自動會進行灰階和模糊化
        mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=10)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in contours:
            if cv2.contourArea(c) < 200:
                continue

            cv2.drawContours(frame, contours, -1, (0, 255, 255), 2)   # 畫出輪廓
            (x, y, w, h) = cv2.boundingRect(c)                       # 畫出矩型
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

            #Convert the captured frame into RGB
            img = Image.fromarray(frame, 'RGB')

            #Resizing into 128x128 because we trained the model with this image size.
            img = img.resize((150,150))
            img_array = np.array(img)

            #Our keras model used a 4D tensor, (images x height x width x channel)
            #So changing dimension 128x128x3 into 1x128x128x3 
            img_array = np.expand_dims(img_array, axis=0)
            predict = model.predict(img_array)
            predict = np.argmax(predict,axis=1)
            predict = np.ndarray.item(predict)
            output = product[predict]
    #         print(output)
    #         print(type(output))

            cv2.putText(frame, output, (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 255, 255), 1, cv2.LINE_AA) # 標示結果         

            # 將結果放進 list
            if output in cart:
                pass
            else:
                cart.append(output)
#                 print(cart)
                result = result+cart
                print(result)
                break

        cv2.imshow("Scanner", frame)
        return result

        key=cv2.waitKey(1)
        if key == 27:
                break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main()__':
    cam_recognizer(register_id)