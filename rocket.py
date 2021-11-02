import numpy as np 
import matplotlib as plt

class Rocket():
    def __init__(self, air_res, engine_thrust, viscosity, rocket_mass, delta_t):
        self.e_t = engine_thrust
        self.ang = 45  #launch alnge
        self.r_m = rocket_mass
        self.g = -9.8

        self.v_x = 0 # velocity
        self.x = 0 # position
        self.a_x # acceleratio
        self.f_x = np.cos(self.ang) * self.e_t

        self.v_y = 0
        self.y = 0
        self.a_y = 0
        self.f_y = np.sin(self.ang) * self.e_t

        self.a_r = air_res
        self.vis = viscosity

        self.d_t = delta_t
        self.i = 0
    def launch(self):
        while True:
            self.main_calc()
            self.append_data()

    def main_calc(self):
        self.a_x = (self.f_x / self.r_m) - self.a_r
        self.v_x = self.a_x * self.d_t
        self.x = self.v_x * self.d_t

        self.a_y = (self.f_y / self.r_m) - self.a_r + self.g
        self.v_y = self.a_y * self.d_t
        self.y = self.v_y * self.d_t
    
    def append_data(self):
        self.i += 1
        self.data[1].append(self.y)
        self.data[2].append(self.v_y)
        self.data[4].append(self.i * self.d_t)

    def plot(self):
        plt.plot(self.data[1])
        plt.ylabel("X(t)")
        plt.xlabel("t*20")
        plt.show()
    
    if __name__ == '__main__':
        rocket = Rocket()
        rocket.launch()
        rocket.plot()