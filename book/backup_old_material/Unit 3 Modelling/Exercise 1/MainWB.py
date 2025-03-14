import numpy       as np
import matplotlib.pyplot as plt

#script to calculate the water balance of a one bucket model

S0 = 20                    #mm
k = 0.07                   #day^-1
alfa = 0.55                #(-)
tmax = 500                 #days, max = 669, because length P and PE
dt = 1                     #days, dt=1, because timestep P and PE
P_PE = np.genfromtxt('P_PE.txt')    #load file with precipitation and potential evaporation
P = P_PE[:,0]              #assign precipitation from file    
PE = P_PE[:,1]             #assign potential evaporation from file
S = np.zeros(tmax/dt)       #empty vector for storage: assigning an empty vector before a for loop speeds up your script
EA=np.zeros(tmax)           #empty vector for actual evaporation
Q=np.zeros(tmax)            #empty vector for modelled discharge

## Calculate water balance
S[0] = S0                    #set initial value for first field in storage vector
Q[1] = k*dt*S[0]**alfa      #calculate first value for discharge
for i in range(1,tmax/dt):
	S[i] = S[i-1]+P[i]       #add precipitation to the state of the previous time step
	EA[i] = min(PE[i],S[i])    #calculate the actual evaporation for time step t
	S[i] = S[i]-EA[i]          #substract the actual evaporation from the state
	Q[i] = k*dt*S[i]**alfa    #calculate the discharge
	S[i] = S[i]-Q[i]       #substract the discharge from the state                   


RC=sum(Q)/sum(P)               #calculate the average runoff coefficient
print(Q)

## plot the calculated discharge
t=range(0,tmax,dt)
plt.plot(t,Q,'b')
plt.title('Discharge from reservoir, k='+ str(k) + ', alfa=' + str(alfa) + ', RC='+ str(RC))
plt.xlabel('time (days)')
plt.ylabel('discharge (mm/d)')

plt.show()
