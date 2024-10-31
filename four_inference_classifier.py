import pickle
import cv2
import mediapipe as mp
import numpy as np
from labels_dict import labels_dict
from flask import Flask, render_template, Response

app = Flask(__name__, template_folder='./Template')

class GestureClassifier:
    def __init__(self):
        self.model_dict = pickle.load(open("./model.p", "rb"))
        self.model = self.model_dict["model"]

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

        # Using dynamic image mode for better gesture tracking across frames
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,  # Switching to dynamic mode for video
            max_num_hands=2,  # Optionally allow detection of multiple hands
            min_detection_confidence=0.5,  # Higher confidence for more accurate detection
            min_tracking_confidence=0.5  # Improve gesture tracking across frames
        )

    def predict(self, frame):
        data_aux = []
        x_ = []
        y_ = []

        try:
            # Optimize the frame size by resizing to reduce processing load
            frame = cv2.resize(frame, (640, 480))  # Resize for performance
            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = self.hands.process(frame_rgb)
            predicted_character = None  # Initialize to None

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style(),
                    )

                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10

                x2 = int(max(x_) * W) - 10
                y2 = int(max(y_) * H) - 10

                # Prediction with zero padding for the input length
                prediction = self.model.predict(
                    [np.asarray(data_aux + [0] * (84 - len(data_aux)))]
                )
                predicted_character = labels_dict[prediction[0]]

                # Draw the bounding box around the hand
                cv2.putText(
                    frame,
                    f"{predicted_character}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA
                )
            else:
                # Handle the case where no hands are detected
                cv2.putText(frame, "", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        except Exception as e:
            print(f"Error processing frame: {e}")
            cv2.putText(frame, predicted_character, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        return predicted_character, frame

# Flask routes and app configuration remain unchanged
