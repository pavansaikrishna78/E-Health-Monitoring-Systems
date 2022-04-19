#include <SoftwareSerial.h>

#include <TinyGPS.h>

TinyGPS gps;
SoftwareSerial ss(4, 3);
void setup() {
  Serial.begin(9600); // See "Enhancements" above to learn when to change this.
  ss.begin(4800);
}

void loop() {
  //if (Serial.available())
  {
     float flat, flon;
     unsigned long age;
    // read the input on analog pin 0:
    gps.f_get_position(&flat, &flon, &age);
    float pulse = analogRead(A0)/10;
    float lati = flat;
    float longi = flon;
    
 
    Serial.print(pulse);
    Serial.print(',');
    Serial.print(lati);
    Serial.print(',');
    Serial.println(longi);
    delay(3000);
  }
}
