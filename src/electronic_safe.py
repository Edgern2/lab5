import hal.hal_lcd as LCD
import hal.hal_keypad as keypad
import hal.buzzer as buzz


#Safe password
password = [6969]

#init lcd
lcd = LCD.lcd()
lcd.lcd_clear()

def main():
	lcd.lcd_display_string("Safe Lock", 1)
	lcd.lcd_display_string("Enter PIN: ", 2)





