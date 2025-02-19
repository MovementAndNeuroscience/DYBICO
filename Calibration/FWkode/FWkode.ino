unsigned long dt = 3; // sends every 3 ms
unsigned long tnew = 0;
unsigned long told = dt; 
double alpha = 0.1; // running average, taking 10% of old read  
double alpha1 = 1.0 - alpha; // running average, taking 90% of new read 
double val1 = 0.0;
double val2 = 0.0;


void setup() {
  Serial.begin(115200);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  analogReference(EXTERNAL); // max is 1022, extern spændingsref, 4V
  told = millis();
}

void loop() {
  tnew = millis();
  val1 = alpha * analogRead(A0) + alpha1 * val1; // our read right now weight only alpha% of total, and old read weighs alpha1%, which gives us a average  
  val2 = alpha * analogRead(A1) + alpha1 * val2;
  if ((tnew - told) >= dt) {
    Serial.print(tnew - told); // comment out if wanting to zoom in on force traces without the 3 "ms" line.
    Serial.write(" ");
    Serial.print((int)val1);
    Serial.write(" ");
    Serial.print((int)val2);
    Serial.write("\n");
    told += dt;
  }
}
