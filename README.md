# 🫣 Protect Iris & Fingerprint Algorithm
- python
- OpenCV
- haarcascade
- Skeleton
## 👀홍채 보호 알고리즘
이미지를 통해 인식한 얼굴 좌표값은 (x,y), 눈의 좌표값은 (ex, ey, ew, eh)으로 정의한다. 홍채의 중앙 좌표값을 얻기 위해 두 개의 좌표를 p1 과 p2를 다음과 같이 정의한다.

<img width="260" alt="스크린샷 2023-05-21 오후 2 49 12" src="https://github.com/kayamz/protect-biometric-information/assets/68880055/4d916c8e-ce80-465a-a599-1812395c4159">


## ✌🏼지문 보호 알고리즘

이미지 상에서 손이 뻗어나가는 각도가 수직이 아닌 경우가 많기 때문에, 어떠한 각도에서도 지문을 찾아내는 공식이 필요했다.
따라서 두번째마디 끝과 손가락의 끝의 중앙 좌표를 구하는 알고리즘을 구현했다.

<img width="200" alt="스크린샷 2023-05-21 오후 2 41 24" src="https://github.com/kayamz/protect-biometric-information/assets/68880055/9a7a179c-046a-49bc-80fa-571491b7cae3">

피타고라스의 공식을 이용하여 구한 뒤, 자연스러운 Blur 처리를 위해 연산식을 연구한 결과, 손가락 한마디의 크기가 가로축보다 세로축의 길이가 일반적으로 길다는 점을 고려해 나누기 3을 하여 원모양의 blur가 자연스럽게 해당 영역 안에서 위치하도록 한다.

<img width="330" alt="스크린샷 2023-05-21 오후 2 29 29" src="https://github.com/kayamz/protect-biometric-information/assets/68880055/3167f47b-78e6-4039-b606-db692a97a408">
