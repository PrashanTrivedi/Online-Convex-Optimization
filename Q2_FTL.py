import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as ss
import random as rand
colors = list("rgbcmyk")
shape = ['--^', '--d', '--v']
np.random.seed(1000)
T=int(input('Enter the  value of T' ))
d=10
delta=0.1
eta=0.1
times=20
w_t=[]
loss_vector=[]
loss_play=[]
average=[]
interval_lower_limit=[]
interval_upper_limit=[]
interval_vector=[]
z=1.96
for t in range(1,T+1):
    cumulative_regret=[]
    for j in range(times):
        loss=[]
        for i in range(8):
            loss.append(np.random.binomial(size=1, n=1, p= 0.5))
        loss9=np.random.binomial(size=1, n=1, p= 0.5-delta)
        loss.append(loss9)
        if t<T/2:
            loss10=np.random.binomial(size=1, n=1, p= 0.5+delta)
            loss.append(loss10)
        else:
            loss10=np.random.binomial(size=1, n=1, p= 0.5-2*delta)
            loss.append(loss10)
        loss=np.squeeze(np.asarray(loss))
        loss_vector.append(loss)
        m=[0 for i in range(10)]
        for j in range(t-1):
            m=m+np.array(loss_vector[j])
        t2=[]
        for w in range(10):
            t2.append(m[w])
        loss_always=min(t2)
        w=np.argmin(m)
        w_t.append(w)
        #print('w_t',w_t)
        loss_play_w=loss_vector[t-1][w]
        #print('loss_play_w',loss_play_w)
        loss_play.append(loss_play_w)
        sum_of_loss=sum(loss_play)
        cumulative_regret.append(-loss_always+sum_of_loss)
    average.append(np.mean(cumulative_regret))
    sd=np.std(cumulative_regret)
    interval_lower_limit.append((z*sd)/(math.sqrt(times)))
    interval_upper_limit.append((z*sd)/(math.sqrt(times)))
interval_vector.append(interval_lower_limit)
interval_vector.append(interval_upper_limit)

#print('first term of loss',sum_of_loss)
#print('second term of regret',loss_always)
#print('cumulative_regret',cumulative_regret)

t=range(T)
plt.errorbar(t,average,interval_vector,fmt='bs--',label='Cumulative regret with CI',elinewidth=0.5,
             ecolor='k',capsize=5,capthick=0.5)
plt.plot(t,average,colors[0] + shape[0], label='Weighted majority')
plt.title('FTL')
plt.xlabel('t')
plt.ylabel('cumulative_regret')
plt.show()
        

    
    

