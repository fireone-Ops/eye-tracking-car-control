# Controle por Olhar - Eye-Tracking Car Control

Um projeto que utiliza visão computacional e rastreamento de íris para controlar um carrinho robótico via Arduino.

## 📋 Descrição

Este projeto implementa um sistema de controle inovador onde um carrinho com motor é comandado através do movimento dos olhos do usuário. Utiliza a biblioteca MediaPipe para detecção facial em tempo real e comunica com um Arduino via porta serial.

## ✨ Características

- **Controle por Visão**: Rastreamento de íris em tempo real usando MediaPipe
- **Interface Simples**: Suporta também controle por teclado
- **Comunicação Serial**: Protocolo de comunicação com Arduino
- **Debouncing**: Envia apenas quando há mudança de comando
- **Diagnóstico**: Ferramenta para diagnosticar conexão com Arduino

## 🏗️ Estrutura do Projeto

```
.
├── README.md                          # Este arquivo
├── diagnostico_serial.py              # Ferramenta de diagnóstico da porta serial
└── controle_por_olhar/
    ├── main.py                        # Controle por rastreamento de olhar
    ├── controle_teclado.py            # Controle alternativo por teclado
    └── arduino_carrinho_corrigido.ino # Firmware do Arduino
```

## 🔧 Requisitos

### Hardware
- Arduino (Uno, Nano, Mega, etc.)
- Câmera USB (integrada ou externa)
- Módulo motor para carrinho (L298N recomendado)

### Software
```bash
pip install opencv-python mediapipe pyserial numpy
```

## 🚀 Como Usar

### 1. Diagnóstico da Porta Serial
Primeiro, verifique se o Arduino está conectado corretamente:

```bash
python diagnostico_serial.py
```

Isso listará todas as portas COM disponíveis e tentará conectar.

### 2. Upload do Firmware
1. Abra o Arduino IDE
2. Carregue o arquivo `controle_por_olhar/arduino_carrinho_corrigido.ino`
3. Verifique a porta COM e o modelo do Arduino
4. Faça o upload para a placa

### 3. Controle por Rastreamento de Olhar
```bash
cd controle_por_olhar
python main.py
```

**Instruções:**
- Pressione **B** para calibrar a posição inicial do olhar
- Mova os olhos para controlar o carrinho:
  - **Cima**: Frente
  - **Baixo**: Trás
  - **Esquerda**: Esquerda
  - **Direita**: Direita
- Pressione **Q** para sair

### 4. Controle por Teclado (Alternativo)
```bash
cd controle_por_olhar
python controle_teclado.py
```

**Comandos:**
- **W**: Frente
- **S**: Trás
- **A**: Esquerda
- **D**: Direita
- **P**: Parar
- **Q**: Sair

## ⚙️ Configuração

### Alterar Porta Serial
Edite a variável `PORTA_SERIAL` nos scripts Python:

```python
PORTA_SERIAL = 'COM7'  # Altere conforme sua porta
BAUD_RATE = 9600
```

### Ajustar Sensibilidade
No `main.py`, ajuste a variável `limiar`:

```python
limiar = 6  # Aumente para menos sensível, diminua para mais sensível
```

## 📊 Protocolo de Comunicação

O Arduino espera receber os seguintes comandos via serial:

| Comando | Ação |
|---------|------|
| **F** | Frente |
| **T** | Trás |
| **E** | Esquerda |
| **D** | Direita |
| **P** | Parar |

## 🔍 Troubleshooting

### Erro: "Nenhuma porta COM encontrada"
- Verifique se o Arduino está plugado via USB
- Instale os drivers CH340 (para placas clonadas)
- Reinicie o Arduino (desplugue e replugue)

### A câmera não abre
- Verifique se outra aplicação está usando a câmera
- Teste com `cv2.VideoCapture(0)` em um script Python simples

### Rosto não está sendo detectado
- Certifique-se de ter boa iluminação
- Posicione-se a uma distância de 30cm a 1m da câmera
- Tente ajustar o limiar de sensibilidade

### Porta serial "Esperando por dados"
- Feche o Arduino IDE ou Serial Monitor
- Verifique se outro programa está usando a porta COM7

## 📚 Tecnologias Utilizadas

- **OpenCV**: Processamento de imagem e exibição
- **MediaPipe**: Detecção facial e rastreamento de íris
- **PySerial**: Comunicação com Arduino
- **NumPy**: Processamento numérico

## 📝 Notas Importantes

1. **Calibração**: Sempre pressione **B** antes de começar para calibrar a posição neutra do olhar
2. **Iluminação**: Ambiente bem iluminado melhora significativamente a detecção
3. **Distância**: Mantenha distância de 30cm a 1m da câmera
4. **Timeout**: Se o rosto não for detectado por ~1s, um aviso será exibido

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido para a disciplina de **Lógica e IA** como trabalho de conclusão, demostrando aplicações práticas de:
- Visão computacional
- Machine learning (MediaPipe)
- Comunicação com hardware
- Programação em Python
- Programação Arduino

## 📄 Licença

Este projeto é fornecido como-está para fins educacionais.

## ✉️ Contato

Desenvolvido por: Davi de Sousa
<p align="left">
    <a href="https://www.linkedin.com/in/davisousavilela">
        <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://github.com/fireone-Ops">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
    </a>
</p>

---

**Última atualização**: Março de 2026
