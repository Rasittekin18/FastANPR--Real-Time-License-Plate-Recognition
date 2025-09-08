import cv2
import asyncio
import json
import os
from fastanpr import FastANPR

# FastANPR sınıfından bir örnek oluştur
fast_anpr = FastANPR()


async def main():
    # Resim dosyalarının yollarını belirle
    image_files = [
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\1.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\2.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\3.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\4.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\5.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\6.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\7.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\8.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\9.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\10.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\11.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\12.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\13.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\14.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\15.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\16.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\17.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\18.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\19.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\20.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\21.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\22.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\23.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\24.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\25.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\26.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\27.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\28.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\29.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\30.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\31.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\32.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\33.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\34.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\35.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\36.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\37.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\38.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\39.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\40.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\41.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\42.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\43.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\44.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\45.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\46.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\47.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\48.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\49.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\50.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\51.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\52.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\53.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\54.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\55.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\56.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\57.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\58.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\59.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\60.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\61.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\62.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\63.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\64.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\65.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\66.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\67.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\68.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\69.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\70.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\71.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\72.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\73.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\74.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\75.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\76.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\77.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\78.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\79.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\80.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\81.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\82.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\83.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\84.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\85.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\86.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\87.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\88.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\89.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\90.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\91.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\92.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\93.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\94.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\95.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\96.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\97.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\98.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\99.jpg",
        "C:\\Users\\Rasit\\OneDrive\\Masaüstü\\Test\\100.jpg",
        # Klasördeki diğer resim dosyalarını da buraya ekleyebilirsiniz
    ]

    # Resimleri yükle
    images = [cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2RGB) for file in image_files]

    # ANPR işlemini çalıştır
    number_plates = await fast_anpr.run(images)

    # JSON çıktısı için veri yapısını oluştur
    output_data = {}

    # Sonuçları işleme
    for file, plates in zip(image_files, number_plates):
        # JSON dosyasına eklemek için her resim için veri hazırlama
        file_data = []
        # Orijinal resmi yeniden yükle (renkli hali)
        image = cv2.imread(file)

        # Görüntüyü 500x500 olarak yeniden boyutlandır
        target_size = (500, 500)
        resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)

        # Oranları hesapla
        x_ratio = target_size[0] / image.shape[1]
        y_ratio = target_size[1] / image.shape[0]

        # Plakaların kutu bilgilerini incele
        # ... kodun başlangıcı aynı ...

        for plate in plates:
            plate_info = {
                "detection_bounding_box": plate.det_box,
                "detection_confidence": plate.det_conf,
                "recognition_text": plate.rec_text,
                "recognition_polygon": plate.rec_poly,
                "recognition_confidence": plate.rec_conf
            }
            file_data.append(plate_info)

            # ✅ Terminale yazdır
            print(f"\nGörsel: {file}")
            print(f"Plaka Metni: {plate.rec_text}")
            print(f"Tanıma Güveni: {plate.rec_conf:.2f}" if plate.rec_conf is not None else "Tanıma Güveni: Bilinmiyor")
            print(f"Tanıma Polygonu: {plate.rec_poly}")
            print(f"Tespit Kutusu: {plate.det_box}")
            print(f"Tespit Güveni: {plate.det_conf:.2f}" if plate.det_conf is not None else "Tespit Güveni: Bilinmiyor")

            # Kutuyu ve metni görsel üzerine çiz
            box = plate.det_box
            if isinstance(box, list) and len(box) == 4:
                top_left = (int(box[0] * x_ratio), int(box[1] * y_ratio))
                bottom_right = (int(box[2] * x_ratio), int(box[3] * y_ratio))
                cv2.rectangle(resized_image, top_left, bottom_right, (0, 255, 0), 2)

                text = plate.rec_text
                cv2.putText(resized_image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                            (0, 255, 0), 2)

        # ... kalan kod aynı ...

        # JSON çıktısına ekle
        output_data[file] = file_data

        # Yeniden boyutlandırılmış görseli göster
        cv2.imshow('ANPR Results', resized_image)
        cv2.waitKey(0)  # Her görselin gösterilmesi için bir tuşa basmayı bekler
        cv2.destroyAllWindows()

    # JSON dosyasının mevcut olup olmadığını kontrol et
    json_file_path = 'anpr_results.json'
    if not os.path.exists(json_file_path):
        # JSON dosyası yoksa oluştur ve veriyi yaz
        with open(json_file_path, 'w') as json_file:
            json.dump(output_data, json_file, indent=4)
    else:
        # JSON dosyası varsa, mevcut veriyi yükle ve yeni veriyi ekle
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)

        # Yeni veriyi mevcut veriye ekle
        existing_data.update(output_data)

        # Güncellenmiş veriyi JSON dosyasına yaz
        with open(json_file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)


# Asenkron işlevi çalıştırın
if __name__ == "__main__":
    asyncio.run(main())
