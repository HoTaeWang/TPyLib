import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not (cap.isOpened()):
	print("Could not open video device")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Display the resulting frame
	cv2.imshow('Training', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

