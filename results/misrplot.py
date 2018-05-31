import matplotlib 
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import time
# plt.ion()
filename = "./results/misrfile.txt"
X,Y = [],[]
img_num = 1763
img_num_out = img_num // 10
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = [float(s) for s in line.split()]
        X.append(value[0])
        Y.append(value[1])
index = X.index(img_num_out)
img_num /= 1.0
X = [i/img_num for i in X[:]]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('missrate at 0.1 : {}'.format(Y[index])) 
ax.set_xscale("log")
ax.set_ylim(0, 1)
ax.plot(X, Y)
plt.savefig('./results/misr{}'.format(int(time.time())))
# plt.pause(1)
plt.clf()