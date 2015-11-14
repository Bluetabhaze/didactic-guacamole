OPEN = True 
CLOSE = False
Claw (CLAW_CLOSE)
Claw (CLAW_CLOSE)
import spiagent
import time

def Claw (open):
    global Servo4
    if open:
     Servo4.Postion = -1.0
    else:
     Servo4.position4 = 1.0

# def OpenClaw() /*
# def CloseClaw()/*



t = spiagent.Transport ("mamre.local")
Servo1 = spiagent.Servo (t,spiagent.LPC1114_PWM1)
Servo2 = spiagent.Servo (t,spiagent.LPC1114_PWM2)
Servo3 = spiagent.Servo (t,spiagent.LPC1114_PWM3)
Servo4 = spiagent.Servo (t,spiagent.LPC1114_PWM4)

for i in range (0,10):
    Claw(True)
    time.sleep (0.5)
    Claw(False)
