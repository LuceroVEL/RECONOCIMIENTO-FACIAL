int option;
#include <SoftwareSerial.h>
SoftwareSerial SIM900(7, 8); //Configarión de los pines serial por software
void setup() {
   SIM900.begin(19200);//Arduino se comunica con el SIM900 a una velocidad de 19200bps
   Serial.begin(19200);//Velocidad del puerto serial de arduino 
   delay(20000);//Tiempo prudencial para el escudo inicie sesión de red con tu operador

}
void loop() {
  if (Serial.available() > 0)
  {inicio:
   char option = Serial.read();
    if (option == 'D') { 

  SIM900.print("ATD");//Comando AT para iniciar una llamada
  SIM900.print("+51XXXXXXXXXX");//Número de telefono al cual queremos llamar
  SIM900.println(";");//El ";" indica llamada de voz 
  Serial.println("Llamando...");//Leyenda que indica que se inicio el llamado
  delay(15000);//Duración del llamado antes de cortar
  SIM900.println("ATH"); // comando AT cortar llamada
  Serial.println("Llamada finalizada");//Leyenda que indica que finalizó el llamado
   delay (20000);
   }
    else {goto inicio;}
        }
}
