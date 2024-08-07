"""
Author: Enes Can Erkan

Date: 25.07.2024
"""
import cv2
import numpy as np
import time
from scipy.spatial import Delaunay
import mediapipe as mp
from face_detection import get_face_landmarks
from image_processing import warp_triangle, create_face_mask
from landmark_utils import get_landmarks_array, get_under_eye_landmarks
from color_utils import get_hsv_values, show_color_sample
from image_loader import load_images  # Görüntüleri yüklemek için import


def resize_image(image, width=None, height=None):
    """
    Görüntüyü belirtilen genişlik veya yüksekliğe yeniden boyutlandırır.

    :param image: Yeniden boyutlandırılacak görüntü (np.array).
    :param width: Hedef genişlik (int veya None).
    :param height: Hedef yükseklik (int veya None).
    :return: Yeniden boyutlandırılmış görüntü (np.array).
    """
    dimensions = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dimensions = (int(w * r), height)
    else:
        r = width / float(w)
        dimensions = (width, int(h * r))

    return cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)


def main():
    """
    Ana işlem akışını yürütür:
    - Yüz hatlarını tespit eder.
    - Yüzü hedef resme uygulamak için görüntüleri hizalar.
    - Sonuçları gösterir ve kaydeder.
    """
    start = time.time()

    # MediaPipe yüz tespiti modeli
    mp_face_mesh = mp.solutions.face_mesh
    mp_drawing = mp.solutions.drawing_utils
    drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

    # Görüntüleri yükle
    images = load_images()
    image = images["image1"]
    new_image = images["image2"]

    # İlk fotoğrafı yükle ve yüzü tespit et
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.9) as face_mesh:
        face_landmarks = get_face_landmarks(image, face_mesh)
        if face_landmarks is None:
            raise ValueError("Yüz tespit edilemedi.")

    # İlk fotoğraftaki göz altı noktalarını al ve HSV ortalama değerlerini hesapla
    under_eye_landmarks = get_under_eye_landmarks(face_landmarks)
    color_sample_hsv = get_hsv_values(image, under_eye_landmarks, image.shape)
    color_sample_bgr = cv2.cvtColor(np.uint8([[color_sample_hsv]]), cv2.COLOR_HSV2BGR)[0][0]
    print(f"Ortalama HSV: {color_sample_hsv}, Ortalama BGR: {color_sample_bgr}")

    # Renk örneğini göster
    show_color_sample(color_sample_bgr)

    # Diğer fotoğrafı yükle ve yüzü tespit et
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, min_detection_confidence=0.9) as face_mesh:
        new_face_landmarks = get_face_landmarks(new_image, face_mesh)
        if new_face_landmarks is None:
            raise ValueError("Yeni fotoğrafta yüz tespit edilemedi.")

    # İlk fotoğrafın landmarklarını ve ikinci fotoğrafın landmarklarını al
    src_points = get_landmarks_array(face_landmarks, image.shape)
    dst_points = get_landmarks_array(new_face_landmarks, new_image.shape)

    # Delaunay triangulation
    delaunay_tri = Delaunay(dst_points)
    triangles = delaunay_tri.simplices

    # Boş bir canvas üzerinde ilk fotoğrafı ikinci fotoğrafın üzerine uydurma
    aligned_image = np.zeros_like(new_image)
    for tri in triangles:
        t_src = [src_points[tri[i]] for i in range(3)]
        t_dst = [dst_points[tri[i]] for i in range(3)]
        warp_triangle(image, aligned_image, t_src, t_dst)

    # Yüz bölgesini hedef resme yerleştirme
    face_mask = create_face_mask(dst_points, new_image.shape)
    center = (int(dst_points[:, 0].mean()), int(dst_points[:, 1].mean()))
    result_image = cv2.seamlessClone(aligned_image, new_image, face_mask, center, cv2.NORMAL_CLONE)

    # Yüz hatlarını ve noktaları çiz
    annotated_image = result_image.copy()
    mp_drawing.draw_landmarks(
        image=annotated_image,
        landmark_list=new_face_landmarks,
        connections=mp_face_mesh.FACEMESH_TESSELATION,
        landmark_drawing_spec=drawing_spec,
        connection_drawing_spec=drawing_spec)

    # Sonuçları göster ve kaydet
    resized_original = resize_image(image, height=300, width=300)
    cv2.imshow("Original Image", resized_original)
    cv2.imshow('Aligned Image', aligned_image)
    cv2.imshow('Result Image', result_image)
    cv2.imshow('Face with Landmarks', annotated_image)
    cv2.imwrite(r'C:\Users\Monster\PycharmProjects\pythonProject\virtual-try-on\assets\aligned_image.jpg',
                aligned_image)
    cv2.imwrite(r'C:\Users\Monster\PycharmProjects\pythonProject\virtual-try-on\assets\result_image.jpg',
                result_image)
    cv2.imwrite(r'C:\Users\Monster\PycharmProjects\pythonProject\virtual-try-on\assets\face_with_landmarks.jpg',
                annotated_image)

    finish = time.time()
    gecen_sure = finish - start
    print(f"**********{gecen_sure:.3f} saniyede işlem yapıldı.******************")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
