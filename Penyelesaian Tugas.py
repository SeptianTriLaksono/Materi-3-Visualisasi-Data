import numpy as np
import matplotlib.pyplot as plt

g = 9.8 
v0 = 0   
h0 = 10 

# waktu jatuh
t_f = np.sqrt(2 * h0 / g)
print("Waktu yang diperlukan benda untuk mencapai tanah = ", t_f, " s")

# kecepatan saat mencapai tanah
v = g * t_f
print("Kecepatan saat mencapai tanah = ", v, " m/s")

# ketinggian akhir (seharusnya 0 karena benda mencapai tanah)
h = h0 - 0.5 * g * t_f**2
print("Ketinggian Akhir = ", h, " m")


t = np.linspace(0, t_f, 1000)
v = g * t
h = h0 - 0.5 * g * t**2

# Plot kecepatan terhadap waktu
fig, ax2 = plt.subplots()
ax2.plot(t, v)
ax2.set(xlabel='t (s)', ylabel='v (m/s)', title='Grafik Kecepatan terhadap Waktu')
ax2.grid()

# Plot ketinggian terhadap waktu
fig, ax1 = plt.subplots()
ax1.plot(t, h)
ax1.set(xlabel='t (s)', ylabel='h (m)', title='Grafik Ketinggian terhadap Waktu')
ax1.grid()

plt.show()
