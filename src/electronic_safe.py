import time
from threading import Thread
import hal.hal_lcd as LCD
import hal.hal_keypad as keypad
import hal.buzzer as buzz

#Variables
#Attempt data
attempt = 0

#Safe password
password = [6,9,6,9]
input = []

#status
status = False



#init lcd
lcd = LCD.lcd()
lcd.lcd_clear()

#init buzzer
buzz.init()

def display():
	lcd.lcd_display_string("Safe Lock", 1)
	lcd.lcd_display_string("Enter PIN: ", 2)

def checkpasswd(password):
	if len(input)!= len(password):
		return False

	for i in range(len(password)):

		if password[i] != input[i]:
			return False

	return True

def key_press(key):
	global status
	global password
	global input
	global attempt

	if status == True :
		return

	lcd.lcd_clear()

	if key == "*" and len(pw) >= 1:
		status = False

		if checkpasswd(password):
			lcd.lcd_display_string("Safe Unlocked", 1)
			return
		else:
			w += 1

			if w>=3:
				lcd.lcd_display_string("Safe Disabled", 1)
				return

			lcd.lcd_display_string("Wrong Password" , 1)
			buzz.beep(1,0,1)
			lcd.lcd_clear()
			display()
			input = []
			status = True

	if key != "#" and key != "*" :
		password.append(key)
		lcd.lcd_dispaly_string("Safe Locked", 1)
		lcd.lcd_display_string("*" * len(password), 2)



def main():
	global status
	keypad.init(key_press)
	keypad_thread = Thread(target = keypad.get_key )
	keypad_thread.start()
	display()
	status = True



if __name__=="__main__":
    main()

