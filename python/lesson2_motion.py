import cv2 as cv
import numpy as np
import imutils

cap = cv.VideoCapture(0)

final_frame = None
initial_frame = None

width = 640
height = 480
min_area_coefficient = 0.026

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv.resize(frame, (width, height))

    # Our operations on the frame come here
    final_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    final_frame = cv.GaussianBlur(final_frame, (3, 3), 0)

    if initial_frame is not None:
        diff = cv.absdiff(initial_frame, final_frame)

        thresh = cv.threshold(diff, 24, 255, cv.THRESH_BINARY)[1]

        dial = cv.dilate(thresh, None, iterations=10)

        cnts = cv.findContours(dial, cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        bounded = dial.copy()

        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            if cv.contourArea(c) < int(min_area_coefficient * width * height):
                continue

            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv.boundingRect(c)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.rectangle(bounded, (x, y), (x + w, y + h), 255, 2)

        top = np.hstack((diff, thresh))
        bot = np.hstack((dial, bounded))
        pipeline = np.vstack((top, bot))

        cv.imshow('motion', frame)
        cv.imshow('pipeline', pipeline)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    initial_frame = final_frame

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
