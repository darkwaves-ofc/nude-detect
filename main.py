from nudenet import NudeDetector
from better_profanity import profanity
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np
profanity.load_censor_words()
classifier = NudeDetector()
image_path = ''
isAdultContent = False
isNudeContent = False
prop = classifier.detect(image_path)
print(prop)


def check_Nude_Content(detections, threshold=0.1):
    exposed_parts = [
        "FEMALE_BREAST_EXPOSED",
        "MALE_GENITALIA_EXPOSED",
        "FEMALE_GENITALIA_EXPOSED",
        "BUTTOCKS_EXPOSED",
        "ANUS_EXPOSED",
        "FEET_EXPOSED",
    ]

    for detection in detections:
        if detection['class'] in exposed_parts and detection['score'] > threshold:
            return True
    return False


def check_Adult_Content(image_path):
    img = cv2.imread(image_path)

    # instance text detector
    reader = easyocr.Reader(['en'], gpu=False)

    # detect text on image
    text_ = reader.readtext(img)

    threshold = 0.25
    # draw bbox and text
    for t_, t in enumerate(text_):
        print(t[1])
        if profanity.contains_profanity(t[1]):
            return True


isNudeContent = check_Nude_Content(prop)
print("isNudeContent:", isNudeContent)

isAdultContent = check_Adult_Content(image_path)
print("isAdultContent:", isAdultContent)


# print(profanity.contains_profanity("Have a merry day! :)"))

# batch_size is optional; defaults to 4
# prop = classifier.classify(['path_to_image_1', 'path_to_image_2'], batch_size=BATCH_SIZE)
# print(prop)
# Returns {'path_to_image_1': {'safe': PROBABILITY, 'unsafe': PROBABILITY},
# 'path_to_image_2': {'safe': PROBABILITY, 'unsafe': PROBABILITY}}
