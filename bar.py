import matplotlib.pyplot as plt

x=[2,4,6,8,10]
y=[6,7,8,2,4]
x2=[1,2,5,7,9]
y2=[4,6,3,5,8]
plt.bar(x,y,label='Bar1',color='r')
plt.bar(x2,y2,label='Bar2',color='b')

plt.xlabel('x')
plt.ylabel('y')
plt.title('matplot\n check it out')
plt.legend()
plt.show()
