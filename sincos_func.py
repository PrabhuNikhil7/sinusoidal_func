
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import math
import time
import schedule
from numpy import array
def sincos():
    ts = int(time.time())
    if (ts%15 == 0):
        ts_list = []
        print("================")
        print("TimeStamp: " + str(ts))
        print("================")
        for i in range(2880):
            ts_list.append(ts)
            ts = ts + 15
        ts_list.append(ts_list[-1] + 15)
        total_values = 2880 # No. of values
        x_values = []
        for i in range(total_values):
            x_values.append(i)
        a = array(x_values)

        # Here NEW data is inserted every 15 sec
        initial_val = 6000 # Initial value
        final_val = 5500 # End value

        if (initial_val > final_val):
            # High to Low

            # Cosine func
            print("Cosine function values")
            amplitude = abs((initial_val - final_val)/2)
            # For accuracy
            freq_list = []
            count = 0
            b_val = np.linspace(0,1,1000000)
            for i in range(1000000):
                b = b_val[i]
                k = (initial_val + final_val)/2
                y = amplitude * np.cos(b * a) + k
                if (y[-1] - final_val) < 0.00001:
                    if (b != 0.0):
                        freq_list.append(b)
                        count = count + 1
                        if (count >= 10):
                            break
            # Output
            for i in range(len(freq_list)):
                k = (initial_val + final_val)/2
                y = amplitude * np.cos(freq_list[i] * a) + k
                x_values.append(total_values)
                b = array(x_values)
                y1 = np.append(y, final_val)
                print(y1)
                # Output graph
                plt.plot(ts_list, y1)
                plt.title('COSINE')
                plt.xlabel('TIME STAMPS')
                plt.ylabel('BTC PRICE')
                #plt.show()

            # Sine func
            print("Sine function values")
            old_initial_val = initial_val
            initial_val = old_initial_val + (old_initial_val - final_val)
            amplitude = abs((initial_val - final_val)/2)
            # For accuracy
            freq_list = []
            count = 0
            b_val = np.linspace(0,1,1000000)
            for i in range(1000000):
                b = b_val[i]
                k = (initial_val + final_val)/2
                y = amplitude * np.sin(b * a) + k
                if (y[-1] - final_val) < 0.00001:
                    if (b != 0.0):
                        freq_list.append(b)
                        count = count + 1
                        if (count >= 10):
                            break
            # Output
            for i in range(len(freq_list)):
                k = old_initial_val
                y = amplitude * np.sin(freq_list[i] * a) + k
                x_values.append(total_values)
                b = array(x_values)
                y1 = np.append(y, final_val)
                print(y1)
                # Output graph
                plt.plot(ts_list, y1)
                plt.title('SINE')
                plt.xlabel('TIME STAMPS')
                plt.ylabel('BTC PRICE')
                #plt.show()

        else:
            # Low to High

            # Sine func
            print("Sine function values")
            amplitude = abs(initial_val - final_val)
            # For accuracy
            freq_list = []
            count = 0
            b_val = np.linspace(0,1,1000000)
            for i in range(1000000):
                b = b_val[i]
                k = initial_val
                y = amplitude * np.sin(b * a) + k
                if (abs(y[-1] - final_val)) < 0.00001:
                    if (b != 0.0):
                        freq_list.append(b)
                        count = count + 1
                        if (count >= 10):
                            break
            # Output
            for i in range(len(freq_list)):
                k = initial_val
                y = amplitude * np.sin(freq_list[i] * a) + k
                x_values.append(total_values)
                b = array(x_values)
                y1 = np.append(y, final_val)
                print(y1)
                # Output graph
                plt.plot(ts_list, y1)
                plt.title('SINE')
                plt.xlabel('TIME STAMPS')
                plt.ylabel('BTC PRICE')
                #plt.show()

            # Cosine func
            print("Cosine function values")
            amplitude = 2 * abs(initial_val - final_val)
            old_initial_val = initial_val
            initial_val = old_initial_val - (final_val - old_initial_val)
            # For accuracy
            freq_list = []
            count = 0
            b_val = np.linspace(0,1,1000000)
            for i in range(1000000):
                b = b_val[i]
                k = initial_val
                y = amplitude * np.cos(b * a - np.pi/3) + k
                if (abs(y[-1] - final_val)) < 0.00001:
                    if (b != 0.0):
                        freq_list.append(b)
                        count = count + 1
                        if (count >= 10):
                            break
            # Output
            for i in range(len(freq_list)):
                k = initial_val
                y = amplitude * np.cos(freq_list[i] * a - np.pi/3) + k
                x_values.append(total_values)
                b = array(x_values)
                y1 = np.append(y, final_val)
                print(y1)
                # Output graph
                plt.plot(ts_list, y1)
                plt.title('COSINE')
                plt.xlabel('TIME STAMPS')
                plt.ylabel('BTC PRICE')
                #plt.show()
schedule.every(1).seconds.do(sincos)
while True:
    schedule.run_pending()
    time.sleep(1)

