import matplotlib.pyplot as plt

population_ages = [22,13,55,62,45,21,22,34,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54]

##ids=[x for x in range(len(population_ages))]
##plt.bar(ids,population_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)



plt.xlabel('x')
plt.ylabel('y')
plt.title('matplot\n check it out')
plt.legend()
plt.show()
