import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[1,2,3]
y2=[10,14,12]
plt.plot(x,y,label='first')
plt.plot(x2,y2,label='second')
plt.xlabel('Plot label')
plt.ylabel('Important var')
plt.title('matplot\n check it out')
plt.legend()
plt.show()
