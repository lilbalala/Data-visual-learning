import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

filename = r'E:\课程\数据可视化\data\unemployment-rate-1948-2010.csv'
xa = []
ya = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        for datarow in reader:
            if reader.line_num != 1 :
                ya.append(float(datarow[3]))
                xa.append(int(datarow[1]))
except csv.Error:
    print("Error reading csv file")
    sys.exit(-1)
plt.figure()
plt.scatter(xa[:],ya[:],s=10,c='g',marker='o',alpha=0.5)
poly = np.polyfit(xa,ya,deg = 3)
plt.plot(xa,np.polyval(poly,xa))
plt.show()