import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('transactions.csv')
#print(data)
#print(data.head(100))
#get data from first 100 entries for analysis

#Data is filtered from dump.
first_quarter_data = data.head(100)
hand_picked_data = first_quarter_data[["Period", "Data_value"]]

#Statistical operations over data
print("---------------------------")
#Find maximum of data values
maxOfData = hand_picked_data.max()
print(maxOfData)
print("---------------------------")
#Find minimum of data values
minOfData = hand_picked_data.min()
print(minOfData)
print("---------------------------")
#Find mean of data values
meanOfData = hand_picked_data.mean()
print(meanOfData)
print("---------------------------")
#Find median of data values
medianOfData = hand_picked_data.median()
print(medianOfData)
print("---------------------------")
#Find mode of data values
modeOfData = hand_picked_data.mode()
print(modeOfData)
print("---------------------------")
#Measures of the Dispersion
varianceOfData = hand_picked_data.var()
print(varianceOfData)
print("---------------------------")
#Putting everything together
describeData = hand_picked_data.describe()
print(describeData)
print("---------------------------")


#Data visualization
#1. Histogram
x = hand_picked_data["Data_value"]
print(x)
plt.hist(x, bins=10)
plt.show()

#2. Bar Plot
p = hand_picked_data["Data_value"]
q = hand_picked_data["Period"]
q_ceil = np.ceil(q)
q_min = q_ceil/60
print(q_min)

#fig = plt.figure(figsize=(10, 5))
plt.bar(p, q_min, width=4.0)
plt.xlabel("Amount of Transaction")
plt.ylabel("Time taken by transaction")
plt.title("Time taken by transaction to send amount")
plt.show()

#3. Graph
plt.plot(p, q_min)
plt.xlabel("Amount of Transaction")
plt.ylabel("Time taken by transaction")
plt.title("Time taken by transaction to send amount")
plt.show()

#4. Box plot for each feature
data_1 = hand_picked_data["Data_value"]
data_2 = hand_picked_data["Period"]
data = [data_1, data_2]
fig = plt.figure(figsize =(10, 7))
# Creating axes instance
ax = fig.add_axes([0, 0, 1, 1])
# Creating plot
bp = ax.boxplot(data)
# show plot
plt.show()