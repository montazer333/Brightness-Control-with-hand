import mediapipe as mp
import cv2
import screen_brightness_control as sc



def load_model():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_style = mp.solutions.drawing_styles
    return mp_hands,mp_drawing




mp_hands, mp_drawing  = load_model()

hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)




cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    frame = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,
                                    hand_landmarks,
                                    mp_hands.HAND_CONNECTIONS,)
    
    
        land_mark8 = results.multi_hand_landmarks[0].landmark[8]
        land_mark12 = results.multi_hand_landmarks[0].landmark[12]
        distance = ( (land_mark8.x - land_mark12.x)**2 + (land_mark8.y - land_mark12.y)**2 + (land_mark8.z - land_mark12.z)**2)
        # print(f'fasela = {fasela}')

        if distance > 0.003:
            sc.set_brightness('+10')
        else:
            sc.set_brightness('-10')
        
    
    
    
    cv2.imshow('hand', frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()