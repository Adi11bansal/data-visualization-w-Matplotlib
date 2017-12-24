import matplotlib.pyplot as plt

x=[3,5,3,5,26,4,2]
y=[6,4,2,6,4,8,7]
plt.scatter(x,y,label='skt',color='k',s=500,marker='x')

plt.xlabel('x')
plt.ylabel('y')
plt.title('matplot\n check it out')
plt.legend()
plt.show()
