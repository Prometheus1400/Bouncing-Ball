import matplotlib.pyplot as plt
import math as m

y_initial = 100
y_final = None
y_acceleration = -10
y_velocity_i = 0
y_velocity_f = None
time = 0
new_time = 0

while time <= 100:
    # position formula
    y_final = round(y_initial + y_velocity_i*(time - new_time) + (1/2)*y_acceleration*((time-new_time)**2),2)
    y_velocity_f = round(y_velocity_i + y_acceleration*(time - new_time),2)
    if y_final <= 0:
        print('t')
        y_initial = y_final
        y_velocity_i = -0.9 * y_velocity_f
        new_time = time

    plt.scatter(time, y_final)

    time = round(time + 0.1,2)
    print(time)
plt.show()



