import cv2
import mediapipe as mp
import numpy
import serial
import time

#CONFIGURAÇÃO DA PORTA SERIAL 
# Altere 'COM3' e '9600' conforme sua placa Arduino
PORTA_SERIAL = 'COM7'
BAUD_RATE = 9600
DELAY_INICIAL = 2  # segundos para Arduino inicializar

arduino = None
try:
    arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    time.sleep(DELAY_INICIAL)
    print(f"✓ Conectado ao Arduino em {PORTA_SERIAL}")
except serial.SerialException as e:
    print(f"✗ Erro ao conectar Arduino: {e}")
    print(f"  Verifique se Arduino está em {PORTA_SERIAL} e plugado.")
    print(f"  Dica: Feche Arduino IDE, Serial Monitor ou outro programa usando COM7")
    exit()

#CONFIGURAÇÃO DO MEDIAPIPE
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

# CONFIGURAÇÃO DA CÂMERA 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Câmera não pode ser aberta.")
    arduino.close()  # Fecha porta serial antes de sair
    exit()

base_right = None
base_left = None
ultimo_comando = None  # Debouncing: envia apenas quando comando muda
frames_sem_rosto = 0  # Contador para detectar perda de rastreamento
TIMEOUT_ROSTO = 30  # Frames sem detecção antes de alertar (em 30 FPS ~= 1s)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    cx_right = cy_right = None
    cx_left = cy_left = None

    # DETECÇÃO DE ROSTO E ÍRIS 
    if results.multi_face_landmarks:
        frames_sem_rosto = 0  # Reset: rosto detectado
        
        for face_landmarks in results.multi_face_landmarks:
            # Ponto 468: íris direita (landmark do MediaPipe)
            iris_r = face_landmarks.landmark[468]
            cx_right = int(iris_r.x * w)
            cy_right = int(iris_r.y * h)
            cv2.circle(frame, (cx_right, cy_right), 3, (0, 0, 255), -1)

            # Ponto 473: íris esquerda (landmark do MediaPipe)
            iris_l = face_landmarks.landmark[473]
            cx_left = int(iris_l.x * w)
            cy_left = int(iris_l.y * h)
            cv2.circle(frame, (cx_left, cy_left), 3, (0, 0, 255), -1)
    else:
        # Rosto não detectado
        frames_sem_rosto += 1
        if frames_sem_rosto == TIMEOUT_ROSTO:
            print(f"⚠️  Aviso: Rosto não detectado por ~1s")
            # Uncoment a linha abaixo para parar carrinho quando perde rosto:
            # ultimo_comando = None  # Force enviar comando "P" (parar)

    key = cv2.waitKey(1)

    if key == ord('b') and cx_right and cx_left:
        base_right = (cx_right, cy_right)
        base_left = (cx_left, cy_left)
        print("Base definida!")

    direction = "--"
    comando = "P"

    if base_right is not None and cx_right is not None:
        dx = cx_right - base_right[0]
        dy = cy_right - base_right[1]

        # AJUSTE AQUI: Limiar de sensibilidade 
        # Aumente para menos sensível (ex: 10, 15)
        # Diminua para mais sensível (ex: 3, 4)
        limiar = 6

        if dy < -limiar:
            direction = "CIMA"
            comando = "F"
        elif dy > limiar:
            direction = "BAIXO"
            comando = "T"
        elif dx > limiar:
            direction = "ESQUERDA"
            comando = "E"
        elif dx < -limiar:
            direction = "DIREITA"
            comando = "D"
        else:
            direction = "CENTRO"
            comando = "P"

        cv2.putText(frame, direction, (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # DEBOUNCING: Envia apenas quando comando muda 
        if comando != ultimo_comando:
            try:
                if arduino and arduino.is_open:
                    arduino.write(comando.encode())
                    arduino.flush()  # Garante que foi enviado
                    ultimo_comando = comando
                    print(f"→ Comando enviado: {comando} ({direction})")
                else:
                    print(f"✗ Erro: Porta serial não está aberta")
            except serial.SerialException as e:
                print(f"✗ Erro ao enviar comando: {e}")
                if arduino:
                    arduino.close()
                exit()

    cv2.imshow("Frame", frame)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
if arduino and arduino.is_open:
    arduino.close() 
print("✓ Programa encerrado e porta serial fechada.")