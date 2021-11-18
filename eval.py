import numpy as np
import matplotlib.pyplot as plt
import os


loss = []
val_acc = []
train_acc = []
strs = []
time = []
with open('logs', 'r') as f:
    strs = f.readlines()
    f.close()

print(len(strs))

for line in strs:
    if "loss = " in line:
        i = line.index("loss = ")
    
        i += len("loss = ")
        e = line.find(',', i)
        loss.append(float(line[i: e]))
    elif "Train acc = " in line:
        i = line.index("Train acc = ")
    
        i += len("Train acc = ")
        e = line.find(',', i)
        train_acc.append(float(line[i: e]))
        
        i = line.index('val acc = ')
        i += len("val acc = ")
        e = line.find('. ', i)
        val_acc.append(float(line[i: e]))
        
        i = line.index('Time cost ')
        i += len("Time cost ")
        e = line.find(' min', i)
        time.append(float(line[i: e]))
        
    else:
        pass
    
# print(loss)
print(train_acc)
print(val_acc)
# print(time)

# train_lossli=np.array(train_lossli)
# val_lossli=np.array(val_lossli)

train_accli=np.array(train_acc)
val_accli=np.array(val_acc)

# plt.plot(train_lossli,label='train')
# plt.plot(val_lossli,label='val')
# plt.legend()
# plt.title('loss')
# plt.show()

# plt.plot(train_accli,label='train')
# plt.plot(val_accli,label='val')
# plt.plot(loss, label='train loss')
# plt.plot(time, label='train time')
# plt.legend()
# plt.title('time')
# plt.show()
