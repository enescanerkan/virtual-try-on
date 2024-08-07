"""
Author: Enes Can Erkan

Date: 25.07.2024
"""
import cv2


def get_face_landmarks(image, face_mesh):
    """
    Verilen bir resim üzerinde yüz hatlarını tespit eder.

    :param image: Yüz hatlarını tespit edilecek görüntü (np.array).
    :param face_mesh: MediaPipe FaceMesh modelini temsil eden nesne (mp.solutions.face_mesh.FaceMesh).
    :return: Tespit edilen yüz hatları (mp.framework.formats.landmark_pb2.NormalizedLandmarkList) veya None.
    """
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)
    if results.multi_face_landmarks:
        return results.multi_face_landmarks[0]
    return None
