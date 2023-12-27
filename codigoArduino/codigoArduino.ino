const int ledUm = 7;
const int ledDois = 6;
const int ledTres = 5;
const int ledQuatro = 4;
const int ledCinco = 3;

void setup() {
  Serial.begin(9600);
  pinMode(ledUm, OUTPUT);
  pinMode(ledDois, OUTPUT);
  pinMode(ledTres, OUTPUT);
  pinMode(ledQuatro, OUTPUT);
  pinMode(ledCinco, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    switch (command) {
      case '1':
        digitalWrite(ledUm, HIGH);
        Serial.println("Led um ligado");
        break;
      case '2':
        digitalWrite(ledDois, HIGH);
        Serial.println("Led dois ligado");
        break;
      case '3':
        digitalWrite(ledTres, HIGH);
        Serial.println("Led tres ligado");
        break;
      case '4':
        digitalWrite(ledQuatro, HIGH);
        Serial.println("Led quatro ligado");
        break;
      case '5':
        digitalWrite(ledCinco, HIGH);
        Serial.println("Led Cinco ligado");
        break;
      case '6':
        digitalWrite(ledUm, LOW);
        Serial.println("Led um desligado");
        break;
      case '7':
        digitalWrite(ledDois, LOW);
        Serial.println("Led dois desligado");
        break;
      case '8':
        digitalWrite(ledTres, LOW);
        Serial.println("Led tres desligado");
        break;
      case '9':
        digitalWrite(ledQuatro, LOW);
        Serial.println("Led quatro desligado");
        break;
      case '0':
        digitalWrite(ledCinco, LOW);
        Serial.println("Led Cinco desligado");
        break;

      case 'd':
        digitalWrite(ledCinco, LOW);
        digitalWrite(ledQuatro, LOW);
        digitalWrite(ledTres, LOW);
        digitalWrite(ledDois, LOW);
        digitalWrite(ledUm, LOW);


        break;
      default:
        // Comando desconhecido
        Serial.println("Comando desconhecido");
        break;
    }
  }
}
