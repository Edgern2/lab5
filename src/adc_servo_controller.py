import hal.hal_adc as adc
import hal.hal_servo as srv

def main():
	adc.init()
	srv.init()
	while (True):
		srv.set_servo_position(adc.get_adc_value(1)/5.7)


if __name__ == "__main__":
    main()
