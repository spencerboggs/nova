import cv2
import mediapipe as mp

def get_finger_coordinates():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Initialize MediaPipe Hands
    with mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5) as hands:
        # Start video capture
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Unable to receive frame")
                break

            # Convert the image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the image
            results = hands.process(image)

            # If hand landmarks are detected
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    # Get the coordinates of the index finger tip
                    index_finger_x = int(index_finger_landmark.x * frame.shape[1])
                    index_finger_y = int(index_finger_landmark.y * frame.shape[0])
                    # Draw a circle at the tip of the index finger
                    cv2.circle(frame, (index_finger_x, index_finger_y), 5, (0, 255, 0), -1)
                    # Display the coordinates
                    cv2.putText(frame, f"({index_finger_x}, {index_finger_y})", (index_finger_x, index_finger_y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Display the frame
            cv2.imshow('Hand Tracking', cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

def main():
    get_finger_coordinates()