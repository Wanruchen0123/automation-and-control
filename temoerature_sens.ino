#define T_Sensor A1
double T = 0.0;
double V_sens = 0;
double T_offset = 14;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
delay(1000);
Serial.print("ADC: ");
Serial.println(analogRead(T_Sensor));
V_sens = (double)analogRead(T_Sensor) * 3.3 / 4096.0;
Serial.print("V_sens: ");
Serial.print(V_sens);
T = V_sens /0.01 + 14;
Serial.print("T: ");
Serial.println(T);
}
