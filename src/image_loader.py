"""
Author: Enes Can Erkan

Date: 05.08.2024
"""
import cv2


# Görüntü dosyalarının yolları
IMAGE_PATHS = {
    "image1": r'C:\Users\Monster\PycharmProjects\pythonProject\virtual-try-on\assets\result_image.jpg',
    "image2": r'C:\Users\Monster\PycharmProjects\pythonProject\virtual-try-on\assets\1.jpg'
}


def load_images():
    """
    Belirtilen dosya yollarından görüntüleri yükler.

    :return: Yüklenen görüntülerin bir sözlüğü (dict).
    """
    images = {}
    for name, path in IMAGE_PATHS.items():
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"Görüntü yüklenemedi: {path}")
        images[name] = image
    return images

