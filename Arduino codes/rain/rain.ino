#define SerialRainPin 0 

void setup(){
 Serial.begin(9600);
 pinMode(2, INPUT);
}

void loop(){
  int i;
  int rain = analogRead(SerialRainPin);
  for (i=0; i < 10; i++){
    rain += analogRead(SerialRainPin);
    Serial.print(".");
    delay(1000);
  }
  Serial.println();
  rain /= 10;
  if(rain<300)
    Serial.print("Heavy Rain: " );//rain);
  else if(rain<500)
    Serial.print("Moderate Rain: ");// + rain);
  else 
    Serial.print("No Rain: ");// + rain);
  Serial.println(rain);
}
