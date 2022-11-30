#include <DHT.h>
#define DHTPIN 7
#define DHTTYPE DHT22
#define LDR_pin A0
DHT dht(DHTPIN, DHTTYPE);

int chk;
float hum;
float temp;
//int LDR_pin=A0;
int LED_pin=11;
int threshold=300;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  pinMode(LED_pin,OUTPUT);
}
void loop() {
  
  delay(2000);
  //dht code
  hum = dht.readHumidity();
  temp = dht.readTemperature();
  Serial.print("Humidity:");
  Serial.print(hum);
  Serial.print("%, Temp:");
  Serial.print(temp);
  Serial.println("Celsius");
  delay(2000);

  //LDR code
  int i=analogRead(LDR_pin);
  Serial.println(i);
  delay(300);
  if(i<threshold)
  {
    digitalWrite(LED_pin,HIGH);
  }
  else
    digitalWrite(LED_pin,LOW);
  
}
