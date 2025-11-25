#include <Arduino.h>

// Classe para controlar a ponte H
class MotorController {
private:
    int IN1, IN2, IN3, IN4;

public:
    MotorController(int in1, int in2, int in3, int in4)
        : IN1(in1), IN2(in2), IN3(in3), IN4(in4) {}

    void begin() {
        pinMode(IN1, OUTPUT);
        pinMode(IN2, OUTPUT);
        pinMode(IN3, OUTPUT);
        pinMode(IN4, OUTPUT);
    }

    void frente() {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    }

    void tras() {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    }

    void esquerda() {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);
        digitalWrite(IN3, HIGH);
        digitalWrite(IN4, LOW);
    }

    void direita() {
        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, HIGH);
    }

    void parar() {
        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);
        digitalWrite(IN3, LOW);
        digitalWrite(IN4, LOW);
    }
};

MotorController motor(2, 4, 12, 13);  // Troque pelos pinos que você usa
char cmd;

void setup() {
    Serial.begin(9600);
    motor.begin();
}

void loop() {
    if (Serial.available()) {
        cmd = Serial.read();

        switch (cmd) {
            case 'F': motor.frente();   break;
            case 'T': motor.tras();     break;
            case 'E': motor.esquerda(); break;
            case 'D': motor.direita();  break;
            case 'P': motor.parar();    break;
        }
    }
}
