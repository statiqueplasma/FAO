// written for RoboJax.com 
#include <SoftwareSerial.h>;
String inputData = ""; // a string to hold incoming data
boolean check = false; // whether the string is complete
String signature = "$GPGLL";
String ID = "1";
String LAT;
String LON;
int PH;
int VIS;
SoftwareSerial Serial4 (10, 11); // RX ; TX

void setup() {
    // initialize serial:    
    Serial.begin(9600);
    Serial2.begin(9600);
    Serial3.begin(9600);
    Serial4.begin(9600);
    // reserve 200 bytes for the inputData:
    inputData.reserve(200);
}
void loop(){
  GPSread();
  delay(1000);
  dataread(); 
  delay(1000);
  Serial1.println(String(ID) + String(LAT) + String(LON) + String(PH) + String(VIS));
  
  
  
  
}
void dataread(){
  if(Serial4.available()){
    VIS = Serial4.read();
  }
  if(Serial3.available()){
    PH = Serial3.read();    
  }
}

void GPSread() {
    // print the string when a newline arrives:
    if (check) {
        String BB = inputData.substring(0, 6);
        if (BB == signature) {
            LAT = inputData.substring(7, 17);
            int LATperiod = LAT.indexOf('.');
            int LATzero = LAT.indexOf('0');
            if (LATzero == 0) {
                LAT = LAT.substring(1);
            }

            LON = inputData.substring(20, 31);
            int LONperiod = LON.indexOf('.');
            int LONTzero = LON.indexOf('0');
            if (LONTzero == 0) {
                LON = LON.substring(1);
            }

        }

        // Serial.println(inputData);
        // clear the string:
        inputData = "";
        check = false;
    }
}

/*
SerialEvent occurs whenever a new data comes in the
hardware serial RX. This routine is run between each
time loop() runs, so using delay inside loop can delay
response. Multiple bytes of data may be available.
*/
void serialEvent() {
    while (Serial.available()) {
        // get the new byte:
        char inChar = (char) Serial.read();
        // add it to the inputData:
        inputData += inChar;
        // if the incoming character is a newline, set a flag
        // so the main loop can do something about it:
        if (inChar == '\n') {
            check = true;
        }
    }
}
