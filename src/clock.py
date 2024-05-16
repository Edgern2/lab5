from hal import hal_lcd as LCD
import time

lcd = LCD.lcd()
lcd.lcd_clear()

def main():
	while(True):
		local_time = time.localtime()
		thime = time.strftime("%H:%M:%S", local_time)
		day = time.strftime("%d:%m:%y",local_time)
		lcd.lcd_display_string(thime, 1)
		lcd.lcd_display_string(day, 2)


# Main entry point
if __name__ == "__main__":
    main()
