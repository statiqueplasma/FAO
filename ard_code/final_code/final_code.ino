// written for RoboJax.com 
String inputData = ""; // a string to hold incoming data
boolean check = false; // whether the string is complete
String inputDatasignature = "$GPGLL";
void setup() {
    // initialize serial:
    Serial.begin(9600);
    // reserve 200 bytes for the inputData:
    inputData.reserve(200);
}
void loop(){
  
  
  
}

void GPSread() {
    // print the string when a newline arrives:
    if (check) {
        String BB = inputData.substring(0, 6);
        if (BB == signature) {
            String LAT = inputData.substring(7, 17);
            int LATperiod = LAT.indexOf('.');
            int LATzero = LAT.indexOf('0');
            if (LATzero == 0) {
                LAT = LAT.substring(1);
            }

            String LON = inputData.substring(20, 31);
            int LONperiod = LON.indexOf('.');
            int LONTzero = LON.indexOf('0');
            if (LONTzero == 0) {
                LON = LON.substring(1);
            }

            Serial.println(LAT);
            Serial.println(LON);

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
