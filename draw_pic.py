import numpy as np
import matplotlib.pyplot as plt
import pandas as  pd

path = "your data file path"

d_9 = pd.read_csv(path).values[0:-1,1:9].T
d_tmp = d_9.copy()

#tranform rules (to match the sensor positions in paper)
d_9[0] = d_tmp[2]
d_9[1] = d_tmp[7]
d_9[2] = d_tmp[4]
d_9[3] = d_tmp[5]
d_9[4] = d_tmp[6]
d_9[5] = d_tmp[1]
d_9[6] = d_tmp[3]
d_9[7] = d_tmp[0]
signalLength = d_9.shape[1]

fig, ax = plt.subplots()
for i in range(d_9.shape[0]):
    dd = np.array(d_9[i])
    dd = (dd-np.mean(dd))/(np.max(dd)-np.min(dd)) 
    ax.plot(range(signalLength),(dd+(0.7*i)),)

plt.show()

