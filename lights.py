import RPi.GPIO as IO
import time
IO.setmode(IO.BCM)
IO.setup(19, IO.OUT)
a = IO.PWM(0,100)
b = IO.PWM(1,100)
c = IO.PWM(2,100)
d = IO.PWM(3,100)
a.start(0)
b.start(0)
c.start(0)
d.start(0)

while 1:
	for x in range(50):
		a.changeDutyCycle(x);
		b.changeDutyCycle(x);
		c.changeDutyCycle(x);
		d.changeDutyCycle(x);
		time.sleep(0.1)

	for x in range(50):
		a.changeDutyCycle(50-x);
		b.changeDutyCycle(50-x);
		c.changeDutyCycle(50-x);
		d.changeDutyCycle(50-x);
		time.sleep(0.1)