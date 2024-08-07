"""
Author: Enes Can Erkan

Date: 25.07.2024
"""
import cv2
import numpy as np


def apply_affine_transform(src, src_tri, dst_tri, size):
    """
    Affine dönüşüm uygular.

    :param src: Kaynak görüntü (np.array).
    :param src_tri: Kaynak üçgen köşe noktaları (list of tuple).
    :param dst_tri: Hedef üçgen köşe noktaları (list of tuple).
    :param size: Çıktı görüntüsünün boyutları (tuple: genişlik, yükseklik).
    :return: Dönüştürülmüş görüntü (np.array).
    """
    warp_mat = cv2.getAffineTransform(np.float32(src_tri), np.float32(dst_tri))
    return cv2.warpAffine(src, warp_mat, (size[0], size[1]), None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)


def warp_triangle(src_img, dst_img, t_src, t_dst):
    """
    Bir üçgenin kaynak görüntüden hedef görüntüye doğru şekilde dönüştürülmesini sağlar.

    :param src_img: Kaynak görüntü (np.array).
    :param dst_img: Hedef görüntü (np.array).
    :param t_src: Kaynak üçgen köşe noktaları (list of tuple).
    :param t_dst: Hedef üçgen köşe noktaları (list of tuple).
    """
    r1 = cv2.boundingRect(np.float32([t_src]))
    r2 = cv2.boundingRect(np.float32([t_dst]))

    t1_rect = []
    t2_rect = []
    t2_rect_int = []

    for i in range(3):
        t1_rect.append(((t_src[i][0] - r1[0]), (t_src[i][1] - r1[1])))
        t2_rect.append(((t_dst[i][0] - r2[0]), (t_dst[i][1] - r2[1])))
        t2_rect_int.append(((t_dst[i][0] - r2[0]), (t_dst[i][1] - r2[1])))

    mask = np.zeros((r2[3], r2[2], 3), dtype=np.float32)
    cv2.fillConvexPoly(mask, np.int32(t2_rect_int), (1.0, 1.0, 1.0), 16, 0)

    img1_rect = src_img[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]
    size = (r2[2], r2[3])
    img2_rect = apply_affine_transform(img1_rect, t1_rect, t2_rect, size)

    dst_img[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] = dst_img[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]] * (1 - mask) + img2_rect * mask


def create_face_mask(points, shape):
    """
    Yüz bölgesini içeren bir maske oluşturur.

    :param points: Yüz hatlarının 2D koordinatları (np.array).
    :param shape: Görüntü boyutları (tuple: yükseklik, genişlik, kanal sayısı).
    :return: Yüz bölgesini temsil eden maske (np.array).
    """
    mask = np.zeros(shape[:2], dtype=np.uint8)
    hull = cv2.convexHull(points)
    cv2.fillConvexPoly(mask, hull, 255)
    return mask
