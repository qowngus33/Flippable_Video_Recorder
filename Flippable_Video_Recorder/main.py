import cv2 as cv
print(cv.__version__)

webcam = cv.VideoCapture(0)

if not webcam.isOpened():
    print("Could not open webcam")
    exit()

idx = 0
do_flip = False

while webcam.isOpened():
    status, frame = webcam.read()

    if not status:
        print("Could not open webcam")
        break

    if do_flip:
        frame = cv.flip(frame, 1)
    text = "Press the Space Bar to Start Record or ESC to Exit ...\n Press 'F' to apply left-right inversion"
    cv.putText(frame, text, (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv.imshow("Webcam", frame)

    width = int(webcam.get(3))
    height = int(webcam.get(4))
    fps = webcam.get(cv.CAP_PROP_FPS)
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')

    k = cv.waitKey(1)
    if k == 32:
        out = cv.VideoWriter(f'SaveVideo{idx}.mp4', fourcc, 20.0, (width, height))
        print(f'Recording in progress... Video Number {idx}')
        while True:
            stat, f = webcam.read()

            if do_flip:
                f = cv.flip(f, 1)
            out.write(f)

            text = "Recording.. Press the Space Bar to Stop and Save"
            cv.putText(f,text,(70,100),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            cv.circle(f, (50,90), 10, (0, 0, 255), 3)
            cv.imshow("Webcam", f)

            k = cv.waitKey(1)
            if k == 32:
                print('Recording Finished')
                out.release()
                idx+=1
                break

    elif k == ord('f'):
        do_flip = ~do_flip

    elif k == 27:
        webcam.release()
        cv.destroyAllWindows()
        break
