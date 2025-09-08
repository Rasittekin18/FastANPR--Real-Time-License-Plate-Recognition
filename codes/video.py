import cv2
import asyncio
from fastanpr import FastANPR

async def run_on_video(video_path):
    # FastANPR nesnesi oluştur
    fast_anpr = FastANPR()

    # Videoyu aç
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # İsteğe bağlı: Her 5 karede bir tanıma yap
        frame_count += 1
        if frame_count % 5 != 0:
            continue

        # RGB formatına çevir (gerekli)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Tek karelik liste halinde gönder
        results = await fast_anpr.run([frame_rgb])

        # Plaka varsa yazdır
        for plate in results[0]:
            print("Plaka:", plate.rec_text, "Güven:", plate.rec_conf)

            # Plakayı kare üzerine çiz
            x1, y1, x2, y2 = map(int, plate.det_box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, plate.rec_text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # Kareyi göster
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Asenkron fonksiyonu çalıştır
asyncio.run(run_on_video("C:\\Users\Rasit\\PycharmProjects\\pythonProject9\\yeni_ortam_adi\\fastanpr\\4.mp4"))
