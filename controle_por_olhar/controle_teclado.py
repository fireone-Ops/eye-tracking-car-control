import serial
import time
import sys

# CONFIGURAÇÃO DA PORTA SERIAL
PORTA_SERIAL = 'COM7'
BAUD_RATE = 9600
DELAY_INICIAL = 2  # segundos para Arduino inicializar

# Inicializar conexão com Arduino
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

print("\n" + "=" * 60)
print("CONTROLE DO CARRINHO POR TECLADO")
print("=" * 60)
print("\nComandos:")
print("  W - Frente")
print("  S - Trás")
print("  A - Esquerda")
print("  D - Direita")
print("  P - Parar")
print("  Q - Sair do programa")
print("\n" + "=" * 60 + "\n")

try:
    while True:
        # Receber entrada do usuário
        comando_input = input("Digite comando (W/S/A/D/P/Q): ").upper().strip()
        
        if not comando_input:
            continue
        
        comando = comando_input[0]  # Pega apenas o primeiro caractere
        
        # Mapear entrada para comando Arduino
        comando_arduino = None
        descricao = ""
        
        if comando == 'W':
            comando_arduino = 'F'
            descricao = "FRENTE"
        elif comando == 'S':
            comando_arduino = 'T'
            descricao = "TRÁS"
        elif comando == 'A':
            comando_arduino = 'E'
            descricao = "ESQUERDA"
        elif comando == 'D':
            comando_arduino = 'D'
            descricao = "DIREITA"
        elif comando == 'P':
            comando_arduino = 'P'
            descricao = "PARAR"
        elif comando == 'Q':
            print("\n✓ Encerrando programa...")
            break
        else:
            print("✗ Comando inválido! Use W/S/A/D/P/Q")
            continue
        
        # Enviar comando ao Arduino
        try:
            if arduino and arduino.is_open:
                arduino.write(comando_arduino.encode())
                arduino.flush()
                print(f"→ Comando enviado: {comando_arduino} ({descricao})")
            else:
                print(f"✗ Erro: Porta serial não está aberta")
                break
        except serial.SerialException as e:
            print(f"✗ Erro ao enviar comando: {e}")
            break

except KeyboardInterrupt:
    print("\n\n✗ Programa interrompido pelo usuário")

finally:
    # Fechar porta serial
    if arduino and arduino.is_open:
        arduino.close()
    print("✓ Porta serial fechada")
    print("✓ Programa encerrado")
