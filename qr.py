import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
from urllib.error import URLError

font = cv2.FONT_HERSHEY_PLAIN
url = "http://192.168.200.166/"

cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)

prev = ""
pres = ""
while True:
    try:
        img_resp = urllib.request.urlopen(url + "cam-hi.jpg")
        imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        frame = cv2.imdecode(imgnp, -1)

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            pres = obj.data
            if prev == pres:
                pass
            else:
                print("Type:", obj.type)
                print("Data: ", obj.data)
                prev = pres
            cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)

        cv2.imshow("live transmission", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    except URLError as e:
        print(
            "Error: Unable to connect to the host. Check network configuration. Error message:",
            e.reason,
        )

cv2.destroyAllWindows()
