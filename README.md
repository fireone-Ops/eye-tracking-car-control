# Eye Tracking Car Control

Sistema de controle de um carrinho robótico utilizando visão computacional, rastreamento ocular e comunicação serial com Arduino.

O projeto utiliza **MediaPipe** para detectar a posição dos olhos em tempo real e converter os movimentos do olhar em comandos enviados para um Arduino, permitindo controlar o deslocamento do carrinho sem contato físico.

---


## Tecnologias

- Python
- OpenCV
- MediaPipe
- NumPy
- PySerial
- Arduino (C++)
- Comunicação Serial

---

## Funcionalidades

- Rastreamento ocular em tempo real.
- Controle do carrinho através do movimento dos olhos.
- Comunicação serial com Arduino.
- Calibração da posição neutra do olhar.
- Controle alternativo utilizando teclado.
- Ferramenta para diagnóstico da porta serial.
- Sistema de debounce para evitar envio excessivo de comandos.

---

## Estrutura do Projeto

```text
.
├── diagnostico_serial.py
├── README.md
└── controle_por_olhar/
    ├── main.py
    ├── controle_teclado.py
    └── arduino_carrinho_corrigido.ino
```

---

## Requisitos

### Hardware

- Arduino Uno, Nano ou Mega
- Webcam
- Driver para motores (L298N ou equivalente)
- Carrinho robótico

### Software

Instale as dependências:

```bash
pip install opencv-python mediapipe pyserial numpy
```

---

## Como executar

### 1. Diagnóstico da comunicação

```bash
python diagnostico_serial.py
```

---

### 2. Gravar o firmware

Abra o Arduino IDE.

Carregue o arquivo:

```text
controle_por_olhar/arduino_carrinho_corrigido.ino
```

Selecione a porta correta e envie para a placa.

---

### 3. Controle por rastreamento ocular

```bash
cd controle_por_olhar

python main.py
```

### Controles

| Ação | Movimento |
|------|-----------|
| Frente | Olhar para cima |
| Trás | Olhar para baixo |
| Esquerda | Olhar para esquerda |
| Direita | Olhar para direita |

Pressione **B** para calibrar.

Pressione **Q** para sair.

---

### Controle por teclado

```bash
cd controle_por_olhar

python controle_teclado.py
```

| Tecla | Ação |
|-------|------|
| W | Frente |
| S | Trás |
| A | Esquerda |
| D | Direita |
| P | Parar |
| Q | Sair |

---

## Configuração

### Porta Serial

```python
PORTA_SERIAL = "COM7"
BAUD_RATE = 9600
```

---

### Sensibilidade

```python
limiar = 6
```

Valores maiores tornam o sistema menos sensível.

---

## Protocolo de Comunicação

| Comando | Descrição |
|----------|-----------|
| F | Frente |
| T | Trás |
| E | Esquerda |
| D | Direita |
| P | Parar |

---

## Solução de Problemas

### Nenhuma porta serial encontrada

- Verifique a conexão USB.
- Instale o driver CH340 (caso utilize placas compatíveis).
- Reinicie o Arduino.

### A câmera não abre

- Feche outros programas que utilizem a webcam.
- Teste a câmera separadamente com OpenCV.

### O rosto não é detectado

- Utilize um ambiente bem iluminado.
- Posicione-se entre 30 cm e 1 metro da câmera.
- Ajuste o valor do `limiar`.

### Porta serial ocupada

Feche o Monitor Serial do Arduino IDE antes de executar o programa.

---

## Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Visão Computacional
- Rastreamento Facial
- Comunicação Serial
- Integração entre Software e Hardware
- Programação em Python
- Programação para Arduino
- Processamento de Imagens em Tempo Real

---

## Contexto

Projeto desenvolvido como trabalho da disciplina **Lógica e Inteligência Artificial**, explorando aplicações práticas de visão computacional, automação e integração entre software e hardware.

---

## 👥 Colaboradores

<p align="left">
  <a href="https://github.com/fireone-Ops">
    <img alt="Davi Sousa" src="https://img.shields.io/badge/Davi%20Sousa-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>

  <a href="https://github.com/Sidkkaz">
    <img alt="Heitor" src="https://img.shields.io/badge/Heitor-181717?style=for-the-badge&logo=github&logoColor=white">
  </a>
</p>
