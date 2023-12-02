import matplotlib.pyplot as plt
s = [13.8,20,31.4,26.7,8.1]
g = ["Strongly disagree","Disagree",'Neutral','Agree',"Strongly Agree"]
e = [0,0,0.1,0,0]
cl = ["green","blue",'yellow','red','brown']
plt.pie(s,labels=g,explode=e,autopct="%2.1f%%",colors=cl)
plt.show()

'''from matplotlib import pyplot as plt
import numpy as np
#some example data
x = np.linspace(0.1, 9.9, 20)
y = 3.0 * x
#some confidence interval
ci = 1.96 * np.std(y)/np.sqrt(len(x))
fig, ax = plt.subplots()
ax.plot(x,y)
ax.fill_between(x, (y-ci), (y+ci), color='b', alpha=.1)
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event")'''

# import libraries
import pandas
import numpy
from sklearn.utils import resample
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

# load dataset
x = numpy.array([180,162,158,172,168,150,171,183,165,176])

# configure bootstrap
n_iterations = 1000 # here k=no. of bootstrapped samples
n_size = int(len(x))

# run bootstrap
medians = list()
for i in range(n_iterations):
s = resample(x, n_samples=n_size)
m = numpy.median(s)
medians.append(m)

# plot scores
plt.hist(medians)
plt.show()

# confidence intervals
alpha = 0.95
p = ((1.0-alpha)/2.0) * 100
lower = numpy.percentile(medians, p)
p = (alpha+((1.0-alpha)/2.0)) * 100
upper = numpy.percentile(medians, p)

print(f"\n{alpha*100} confidence interval {lower} and {upper}")

