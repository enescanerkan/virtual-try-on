# Project Title: Virtual Try-On
(Proje Başlığı: Sanal Deneme)

Author: Enes Can Erkan

Date: 7.08.2024

## Description
(Tanım)

This project, named "Virtual Try-On," involves detecting facial landmarks, sampling colors from under-eye regions, and applying face alignment techniques. The implementation uses MediaPipe Face Mesh for facial landmark detection and OpenCV for image processing tasks. On a standard CPU, the processing time for each image is approximately 0.3 seconds.
(Bu proje, "Virtual Try-On" olarak adlandırılan yüz hatlarının tespit edilmesi, göz altı bölgelerinden renklerin örneklenmesi ve yüz hizalama tekniklerinin uygulanmasını içerir. Uygulama, yüz hatlarını tespit etmek için MediaPipe Face Mesh'i ve görüntü işleme görevleri için OpenCV'yi kullanır. Standart bir CPU'da, her görüntünün işlenme süresi yaklaşık olarak 0.3 saniyedir.)

## Features
(Özellikler)

Face Landmark Detection: Detects and extracts facial landmarks from an image.
(Yüz Hatları Tespiti: Bir görüntüden yüz hatlarını tespit eder ve çıkarır.)

Under-eye Color Sampling: Samples the color from the under-eye region of a face and calculates the average HSV values.
(Göz Altı Renk Örnekleme: Bir yüzün göz altı bölgesinden renk örnekler ve ortalama HSV değerlerini hesaplar.)

Face Alignment: Aligns a face from one image to another using affine transformations and Delaunay triangulation.
(Yüz Hizalama: Bir görüntüdeki yüzü, affine dönüşümler ve Delaunay üçgenleme kullanarak başka bir görüntüye hizalar.)

Visualization: Visualizes the aligned face, original image, and the result.
(Görselleştirme: Hizalanmış yüzü, orijinal görüntüyü ve sonucu görselleştirir.)

## Installation
(Kurulum)

## Clone the repository:
(Depoyu klonlayın:)

bash
Kodu kopyala
git clone https://github.com/yourusername/virtual-try-on.git
Install required packages:
(Gerekli paketleri yükleyin:)

bash
Kodu kopyala
pip install -r requirements.txt
Usage
(Kullanım)

Place the images you want to process in the assets directory. Update the paths in image_loader.py.
(İşlemek istediğiniz görüntüleri assets dizinine yerleştirin. image_loader.py dosyasındaki yolları güncelleyin.)

Run the main.py script to start the process.
(main.py scriptini çalıştırarak işlemi başlatın.)

bash
Kodu kopyala
python main.py
The output images will be saved in the assets directory.
(Çıktı görüntüleri assets dizininde kaydedilecektir.)

## File Descriptions
(Dosya Tanımları)

main.py: The main script that coordinates the process.
(Ana script, süreci koordine eder.)

face_detection.py: Contains functions for detecting facial landmarks.
(Yüz hatlarını tespit eden fonksiyonları içerir.)

image_processing.py: Includes functions for image transformations and face mask creation.
(Görüntü dönüşümleri ve yüz maskesi oluşturma fonksiyonlarını içerir.)

landmark_utils.py: Utility functions for processing facial landmarks.
(Yüz hatlarını işlemek için yardımcı fonksiyonlar.)

color_utils.py: Functions for color sampling and visualization.
(Renk örnekleme ve görselleştirme için fonksiyonlar.)

image_loader.py: Handles the loading of images.
(Görüntülerin yüklenmesini yönetir.)

## Contributing
(Katkıda Bulunma)

Feel free to submit pull requests or issues if you find any bugs or have suggestions for improvements.
(Bir hata bulursanız veya geliştirme önerileriniz varsa, çekme istekleri veya sorunlar göndermekten çekinmeyin.)

## License
(Lisans)

This project is licensed under the MIT License.
(Bu proje MIT Lisansı altında lisanslanmıştır.)

README dosyasını GitHub deponuza eklediğinizde, "yourusername" kısmını kendi GitHub kullanıcı adınızla değiştirmeyi unutmayın.

## Test İmages
(Test Görüntüleri)

![denemeler](https://github.com/user-attachments/assets/54123dd8-9732-4d72-9af2-febe8eadfbb9)
![deneme](https://github.com/user-attachments/assets/ddcd39ce-7d36-4fa4-a13a-21f462b1c659)
![denemee](https://github.com/user-attachments/assets/11b04133-4a7c-41c6-9d64-843fea38e880)
![denemeeee](https://github.com/user-attachments/assets/6c21e450-db85-4b05-8e41-ec932145ec35)
![denemes](https://github.com/user-attachments/assets/a3a9b95b-2628-486d-a6b3-ccb251ce7d99)



