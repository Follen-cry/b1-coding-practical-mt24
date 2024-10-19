# Implement of the preliminary PD controller

class controller:
    def __init__(self,Kp=0.15,Kd=0.6):
        self.Kp = Kp
        self.Kd = Kd

    def controller_output(self, error,error_prev)->float:
        return self.Kp*error + self.Kd*(error - error_prev)




