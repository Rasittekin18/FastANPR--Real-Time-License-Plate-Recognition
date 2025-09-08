import cv2
import asyncio
from fastanpr import FastANPR


async def run_ip_camera(url):
    cap = cv2.VideoCapture(url)
    fast_anpr = FastANPR()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = await fast_anpr.run([frame_rgb])

        for plate in results[0]:
            print("Plaka:", plate.rec_text)
            x1, y1, x2, y2 = map(int, plate.det_box)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, plate.rec_text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("IP Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Telefon IP adresinle değiştir
video_url = "http://192.168.197.187:8080/video"

# Asenkron çalıştır
asyncio.run(run_ip_camera(video_url))
