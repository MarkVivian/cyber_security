#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once:
  delay(4000);
  Keyboard.begin();

  // Step 1: Open Run dialog
  Keyboard.press(KEY_LEFT_GUI);
  delay(200);
  Keyboard.releaseAll();
  delay(900);

  // Step 2: Type PowerShell
  Keyboard.print("powershell");
  delay(200);
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
  delay(3000); // wait for PowerShell to open

  // Step 3: Type your message
  Keyboard.print("Write-Host \"hello mark .. it begins\" -ForegroundColor Red");
  delay(300);
  Keyboard.press(KEY_RETURN);
  Keyboard.releaseAll();
  Keyboard.end();
}

void loop() {
  // put your main code here, to run repeatedly:
}