import csv
import matplotlib.pyplot as plt
with open('Bernoulli equation.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    x=[]
    y=[]
    for row in reader:
        depth=float(row['Depth '])
        density=float(row['Water density (kg/m3)'])
        static_pressure=(density*9.81*depth)/100000
        x.append(static_pressure)
        y.append(depth)
        '''print(f"python = {static_pressure},  excel ={row['Static pressure (Pa)']}")'''
    print(x)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    plt.plot(x,y,color='blue', linewidth=2, marker='o')
    plt.ylim(0, 10)
    plt.xlim(0, 1)
    plt.xlabel('Static pressure (bar)')
    plt.ylabel('Depth')
    plt.title('Static preesure in different depths')
    plt.savefig('static preesure & depth.png')
    plt.show()
    