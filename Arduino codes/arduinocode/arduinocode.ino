/*
  Sensors and motor
*/
#include <DHT.h>
#include <AFMotor.h>
#include <Servo.h>

Servo myservo;

#define DHT_pin   A0
#define LDR_pin   A1
#define RAIN_pin  A2

DHT dht(DHT_pin, DHT22);

float hum, temp;
float i, rain;
int motor_angle = 0;
int turn_motor = 0;

void turn_motor_now(){
  if (motor_angle == 0){
    myservo.write(180);
    delay(1000);
    motor_angle = 180;
  }
  else{
    myservo.write(0);
    delay(1000);
    motor_angle = 0;
  }
}


void setup() {
    Serial.begin(9600);
    //Serial.println("setup");
    dht.begin();
    myservo.attach(10);
//    myservo.write(0);
//    delay(1000);
//    myservo.write(270);
}

void loop() {
  int hum_sum=0,temp_sum=0,rain_sum=0, ldr, ldr_sum = 0;
  delay(20);
  //Serial.print("..");
  hum  = dht.readHumidity();       //DHT
  temp = dht.readTemperature();
  ldr  = analogRead(LDR_pin);      //LDR code
  rain = analogRead(RAIN_pin);

  for(int i=0;i<30;i++)
  {
//    Serial.print("...");
    hum_sum   = hum_sum+hum;
    temp_sum  = temp_sum+temp;
    rain_sum  = rain_sum+rain;
    ldr_sum   = ldr_sum + ldr;
    if (Serial.available()){
      turn_motor = Serial.read() - '0';
      if (turn_motor == 1){
        turn_motor_now();
        turn_motor = 0;
      }
//      if (turn_motor == 2){
//        myservo.write(270);
//      }
    }
    hum   = dht.readHumidity();       //DHT
    temp  = dht.readTemperature();
    ldr   = analogRead(LDR_pin);      //LDR code
    rain  = analogRead(RAIN_pin);
    delay(1000);
  }
  int avg_hum,avg_temp,avg_rain, avg_ldr;
  avg_hum   = hum_sum / 30;
  avg_temp  = temp_sum / 30;
  avg_rain  = rain_sum / 30;
  avg_ldr   = ldr_sum / 30;
  
  Serial.print(avg_rain);
  Serial.print("\t");
  Serial.print(avg_temp);
  Serial.print("\t");
  Serial.print(avg_hum);
  Serial.print("\t");
  Serial.print(avg_ldr);
  Serial.println();
  
  if (Serial.available()){
    turn_motor = Serial.read() - '0';
    if (turn_motor == 1){
      turn_motor_now();
      turn_motor = 0;
      
      
      /*
      turn_motor = 0;
//      Serial.println("Turning motor...");
      myservo.write(180);
      digitalWrite(13, HIGH);
      delay(5000);
      //myservo.write(0);
      digitalWrite(13, LOW);
      delay(5000);
      */
    }
//    if (turn_motor == 2){
//        myservo.write(270);
//      }
  }
  
  //Serial.println("..................");
}
