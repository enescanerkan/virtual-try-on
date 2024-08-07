"""
Author: Enes Can Erkan

Date: 25.07.2024
"""
import cv2
import numpy as np


def get_hsv_values(image, landmarks, shape):
    """
    Verilen landmark'lar için HSV değerlerinin ortalamasını hesaplar.

    :param image: Görüntü (np.array).
    :param landmarks: Landmark'lar (list of mp.framework.formats.landmark_pb2.NormalizedLandmark).
    :param shape: Görüntü boyutları (tuple: yükseklik, genişlik, kanal sayısı).
    :return: HSV değerlerinin ortalaması (np.array).
    """
    height, width = shape[:2]
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_values = []

    for landmark in landmarks:
        x, y = int(landmark.x * width), int(landmark.y * height)
        x = max(0, min(x, width - 1))
        y = max(0, min(y, height - 1))
        hsv_values.append(hsv_image[y, x])

    return np.mean(hsv_values, axis=0)


def show_color_sample(color_bgr):
    """
    Örnek renk kodunu gösterir.

    :param color_bgr: Renk kodu (BGR formatında np.array veya list).
    """
    color_sample = np.zeros((100, 100, 3), dtype=np.uint8)
    color_sample[:] = color_bgr
    cv2.imshow('Color Sample', color_sample)