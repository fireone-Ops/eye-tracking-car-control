import serial
import serial.tools.list_ports
import time

print("=" * 50)
print("DIAGNÓSTICO DE PORTA SERIAL")
print("=" * 50)

# 1. Listar todas as portas COM disponíveis
print("\n1. Portas COM disponíveis:")
print("-" * 50)
ports = serial.tools.list_ports.comports()

if not ports:
    print("   ✗ Nenhuma porta COM encontrada!")
else:
    for port in ports:
        print(f"   ✓ {port.device} - {port.description}")

# 2. Tentar conectar na COM7
print("\n2. Tentando conectar na COM7:")
print("-" * 50)

try:
    arduino = serial.Serial('COM7', 9600, timeout=2)
    print(f"   ✓ Conexão estabelecida em COM7")
    print(f"   - Taxa de baud: 9600")
    print(f"   - Timeout: 2s")
    
    # 3. Tentar enviar um comando de teste
    print("\n3. Enviando comando de teste 'P' (parar):")
    print("-" * 50)
    time.sleep(2)  # Aguarda Arduino inicializar
    
    try:
        arduino.write(b'P')
        print("   ✓ Comando 'P' enviado com sucesso!")
        response = arduino.readline()
        if response:
            print(f"   - Resposta do Arduino: {response.decode().strip()}")
        else:
            print("   - Nenhuma resposta do Arduino (isso é normal)")
    except Exception as e:
        print(f"   ✗ Erro ao enviar comando: {e}")
    
    arduino.close()
    print("\n   ✓ Porta fechada com sucesso")
    
except serial.SerialException as e:
    print(f"   ✗ Erro de conexão: {e}")
    print("\n   Possíveis soluções:")
    print("   1. Verifique se o Arduino está plugado via USB")
    print("   2. Instale os drivers CH340 (se usar placa Arduino clonada)")
    print("   3. Verifique qual porta COM o Arduino está usando")
    print("   4. Reinicie o Arduino (desplugue e replugue)")

print("\n" + "=" * 50)
