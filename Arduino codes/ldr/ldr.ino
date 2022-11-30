#define ldrpin A1
int ldr_val = 0;
int avg_ldr = 0;
float ldr_sum = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 0; i < 30; i++){
    ldr_val = analogRead(ldrpin);
    ldr_sum += ldr_val;
    Serial.println();
    Serial.print("LDR val: ");
    Serial.print(ldr_val);
    delay(1000);
  }
  avg_ldr = ldr_sum / 30;
  Serial.println();
  Serial.print("Average over 30 sec: ");
  Serial.print(avg_ldr);
  delay(50);
  Serial.println("...................");
}
