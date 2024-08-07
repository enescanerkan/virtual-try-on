"""
Author: Enes Can Erkan

Date: 25.07.2024
"""
import numpy as np


def get_landmarks_array(landmarks, image_shape):
    """
    Yüz hatlarını 2D koordinatlara dönüştürür.

    :param landmarks: Yüz hatları (mp.framework.formats.landmark_pb2.NormalizedLandmarkList).
    :param image_shape: Görüntü boyutları (tuple: yükseklik, genişlik, kanal sayısı).
    :return: Landmark'ların 2D koordinatları (np.array).
    """
    height, width, _ = image_shape
    points = [(int(lm.x * width), int(lm.y * height)) for lm in landmarks.landmark]
    return np.array(points, dtype=np.int32)


def get_under_eye_landmarks(landmarks):
    """
    Göz altı bölgelerindeki landmark'ları döndürür.

    :param landmarks: Yüz hatları (mp.framework.formats.landmark_pb2.NormalizedLandmarkList).
    :return: Göz altı bölgelerindeki landmark'ların listesi (list of mp.framework.formats.landmark_pb2.NormalizedLandmark).
    """
    under_eye_indices = [101, 102, 103, 104, 105, 331, 332, 333, 334, 335]
    return [landmarks.landmark[i] for i in under_eye_indices]
