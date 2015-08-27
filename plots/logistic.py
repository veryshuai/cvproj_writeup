# This script plots a logistic curve in python

import math
import matplotlib.pyplot as plt
import numpy as np

alp = 0.01
bet = 1

def log_me(x):
    return (alp * np.exp((- alp + bet) * x) - alp) / (alp * np.exp((- alp + bet) * x) + bet)

def log_me_der(x):
    return (alp * (alp + bet) ** 2 * np.exp((- alp + bet) * x)) / ((alp * np.exp((- alp + bet) * x) + bet) ** 2)

#Create an array of 100 linearly-spaced points from 0 to 2*pi
t   = np.linspace(0,10,100)
y   = log_me(t) 
yd  = log_me_der(t) 

# Create the plot
fig = plt.figure(figsize=(17,8)) 
theplot = plt.plot(t,y,'b',3,log_me(3),'ro',7,log_me(7),'ro')
# deriv = plt.plot(t,yd,'y--')
plt.setp(theplot,ms=10)
plt.annotate('movement between firms', xy=(3,log_me(3)+.05), xytext=(1, log_me(1)+.1),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.annotate('movement between firms', xy=(6.7,log_me(6.7)-.05), xytext=(7.5, log_me(7.5)-.04),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.text(3.3,log_me(2.9),'Lagging Firm')
plt.text(5.9,log_me(7),'Leading Firm')
plt.title('The effect of movement between firms', fontsize=16)
plt.xlabel('time', fontsize=14)
plt.ylabel('% informed', fontsize=14)

# Save the figure in a separate file
plt.savefig('mean_field_logistic.png')

# Draw the plot to the screen
plt.show()
