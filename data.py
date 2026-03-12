import cv2
import numpy as np

# ------------------------
# Settings: Track a colored object (e.g., green pen or glove)
# ------------------------
lower_color = np.array([40, 70, 70])   # HSV lower bound
upper_color = np.array([80, 255, 255]) # HSV upper bound

brush_color = (255, 255, 255)  # white
brush_thickness = 5
canvas = None
prev_x, prev_y = None, None
save_count = 0

# ------------------------
# Start webcam
# ------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        x, y = int(x), int(y)

        if radius > 5:
            cv2.circle(frame, (x, y), int(radius), (0, 255, 255), 2)

            if prev_x is None:
                prev_x, prev_y = x, y

            cv2.line(canvas, (prev_x, prev_y), (x, y), brush_color, brush_thickness)
            prev_x, prev_y = x, y
    else:
        prev_x, prev_y = None, None

    # Overlay canvas
    gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, mask_canvas = cv2.threshold(gray_canvas, 20, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask_canvas)
    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    canvas_fg = cv2.bitwise_and(canvas, canvas, mask=mask_canvas)
    frame = cv2.add(frame_bg, canvas_fg)

    # Instructions
    cv2.putText(frame, "C: Clear | S: Save | ESC: Exit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Air Writing - OpenCV", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('s'):
        save_count += 1
        cv2.imwrite(f"air_drawing_{save_count}.png", canvas)
        print(f"Saved air_drawing_{save_count}.png")
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()