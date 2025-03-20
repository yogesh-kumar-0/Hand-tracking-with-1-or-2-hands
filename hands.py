#It uses 1 or both hands depend on reqiurement reponse. With 1 hand 30 different actions can be performed and 60+ with both hands.
#It has 4 modes 0 for using all commands to perform.
#1 for ppt mode.
#2 for media player mode.
#3 for using youtube video.

import mediapipe as mp
import cv2
import pyautogui
import time
#import gtts
import playsound

a = eval(input("Enter a number of hands: "))
mode = eval(input(
    "Enter 0 for simple mode \n Enter 1 for ppt mode \n Enter 2 for media player mode \n Enter 3 for youtube video mode : "))


def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 2

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 3

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 4


    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 5

    if (lst.landmark[5].y * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 16

    if (lst.landmark[5].y * (-100) - lst.landmark[4].y * (-100)) > 6:
        cnt += 27

    if (lst.landmark[5].x * (-100) - lst.landmark[4].x * (-100)) > 6:
        cnt += 38


    if (lst.landmark[5].y * (-100) - lst.landmark[8].y * (-100)) > thresh:
        cnt += 1

    if (lst.landmark[9].y * (-100) - lst.landmark[12].y * (-100)) > thresh:
        cnt += 2

    if (lst.landmark[13].y * (-100) - lst.landmark[16].y * (-100)) > thresh:
        cnt += 3

    if (lst.landmark[17].y * (-100) - lst.landmark[20].y * (-100)) > thresh:
        cnt += 4


    if (lst.landmark[5].x * (-100) - lst.landmark[8].x * (-100)) > thresh:
        cnt += 1

    if (lst.landmark[9].x * (-100) - lst.landmark[12].x * (-100)) > thresh:
        cnt += 2

    if (lst.landmark[13].x * (-100) - lst.landmark[16].x * (-100)) > thresh:
        cnt += 3

    if (lst.landmark[17].x * (-100) - lst.landmark[20].x * (-100)) > thresh:
        cnt += 4


    if (lst.landmark[5].x * 100 - lst.landmark[8].x * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].x * 100 - lst.landmark[12].x * 100) > thresh:
        cnt += 2

    if (lst.landmark[13].x * 100 - lst.landmark[16].x * 100) > thresh:
        cnt += 3

    if (lst.landmark[17].x * 100 - lst.landmark[20].x * 100) > thresh:
        cnt += 4
    return cnt

if a == 2:

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)

    start_init = False

    prev = -1

    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        while True:
            end_time = time.time()
            _, frm = cap.read()
            frm = cv2.flip(frm, 1)

            res = hands.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

            if res.multi_hand_landmarks:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):

                            pyautogui.press("right")

                        elif (cnt == 2):
                            pyautogui.press("left")

                        elif (cnt == 3):
                            pyautogui.press("up")

                        elif (cnt == 4):
                            pyautogui.press("down")

                        elif (cnt == 5):
                            pyautogui.press("space")

                        elif (cnt == 6):
                            pyautogui.press("enter")

                        elif (cnt == 7):
                            pyautogui.press("a")

                        elif (cnt == 8):
                            pyautogui.press("b")

                        elif (cnt == 9):
                            pyautogui.press("l")
                            pyautogui.press("o")
                            pyautogui.press("v")
                            pyautogui.press("e")


                        elif (cnt == 10):
                            pyautogui.press("d")

                        elif (cnt == 11):
                            pyautogui.press("e")

                        elif (cnt == 12):
                            pyautogui.press("f")

                        elif (cnt == 13):
                            pyautogui.press("g")

                        elif (cnt == 14):
                            pyautogui.press("h")

                        elif (cnt == 15):
                            pyautogui.press("i")

                        elif (cnt == 16):
                            pyautogui.press("j")

                        elif (cnt == 17):
                            pyautogui.press("k")

                        elif (cnt == 18):
                            pyautogui.press("l")

                        elif (cnt == 19):
                            pyautogui.press("m")

                        elif (cnt == 20):
                            pyautogui.press("n")

                        elif (cnt == 21):
                            pyautogui.press("o")

                        elif (cnt == 22):
                            pyautogui.press("p")

                        elif (cnt == 23):
                            pyautogui.press("q")

                        elif (cnt == 24):
                            pyautogui.press("r")

                        elif (cnt == 25):
                            pyautogui.press("s")

                        elif (cnt == 26):
                            pyautogui.press("t")

                        elif (cnt == 27):
                            pyautogui.press("u")

                        elif (cnt == 28):
                            pyautogui.press("v")

                        elif (cnt == 29):
                            pyautogui.press("w")

                        elif (cnt == 30):
                            pyautogui.press("x")

                        prev = cnt
                        start_init = False

                mp_drawing.draw_landmarks(frm, hand_keyPoints, mp_hands.HAND_CONNECTIONS)

            image = frm

            image.flags.writeable = False

            image.flags.writeable = True

            if res.multi_hand_landmarks:
                for num, hand in enumerate(res.multi_hand_landmarks):
                    mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                              mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2,
                                                                     circle_radius=2),
                                              )
            cv2.imshow('Hand Tracking', image)

            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                cap.release()
                break
if a == 1:


    cap = cv2.VideoCapture(0)

    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=1)

    start_init = False

    prev = -1

    while True:
        end_time = time.time()
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:

            if mode == 0:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):
                            pyautogui.press("right")

                        elif (cnt == 2):
                            pyautogui.press("left")

                        elif (cnt == 3):
                            pyautogui.press("up")

                        elif (cnt == 4):
                            pyautogui.press("down")

                        elif (cnt == 5):
                            pyautogui.press("space")

                        elif (cnt == 6):
                            pyautogui.press("enter")

                        elif (cnt == 7):
                            pyautogui.press("a")

                        elif (cnt == 8):
                            pyautogui.press("b")

                        elif (cnt == 9):
                            pyautogui.press("l")
                            pyautogui.press("o")
                            pyautogui.press("v")
                            pyautogui.press("e")


                        elif (cnt == 10):
                            pyautogui.press("d")

                        elif (cnt == 11):
                            pyautogui.press("e")

                        elif (cnt == 12):
                            pyautogui.press("f")

                        elif (cnt == 13):
                            pyautogui.press("g")

                        elif (cnt == 14):
                            pyautogui.press("h")

                        elif (cnt == 15):
                            pyautogui.press("i")

                        prev = cnt
                        start_init = False

            if mode == 2:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):
                            pyautogui.press("right")

                        elif (cnt == 3):
                            pyautogui.press("left")

                        elif (cnt == 6):
                            pyautogui.press("up")

                        elif (cnt == 10):
                            pyautogui.press("down")

                        elif (cnt == 15):
                            pyautogui.press("space")
                        prev = cnt
                        start_init = False

            if mode == 3:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):
                            pyautogui.press("right")

                        elif (cnt == 3):
                            pyautogui.press("left")

                        elif (cnt == 6):
                            pyautogui.press("up")

                        elif (cnt == 10):
                            pyautogui.press("down")

                        elif (cnt == 15):
                            pyautogui.press("space")
                        prev = cnt
                        start_init = False

            if mode == 1:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not (prev == cnt):
                    if not (start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time - start_time) > 0.2:
                        if (cnt == 1):
                            pyautogui.press("right")
                            playsound.playsound("apne right kiya hai")


                        elif (cnt == 3):
                            pyautogui.press("left")

                        elif (cnt == 15):
                            pyautogui.press("escape")
                        prev = cnt
                        start_init = False

            drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

        cv2.imshow("window", frm)

        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break



else:
    # print("chutiye 2 se jayeda tera hath bhi nhi loodde")
    print("ERROR Number of hands exceed!!!")
