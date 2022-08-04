# loading the dataset into a pandas object
import pandas as pd
data_set = pd.read_csv("spambase.data")

#assigning names to coloumns
c_names=[]
for i in range(0,58):
    c_names.append(i+1)
data_set.columns=c_names

#descretizing the data into 6 values
discrete_data=[]
for i in range(0,6):
    discrete_data.append(i+1)
for i in range(1,len(data_set.loc[0])):
    data_set[i]=pd.cut(data_set[i],6,labels=discrete_data)

# Divide the data set into training data nd testing data
from sklearn.model_selection import train_test_split
train, test = train_test_split(data_set, test_size = 0.30)
train_in=train.iloc[:,:-1]
train_out=train.iloc[:,-1]
test_in=test.iloc[:,:-1]
test_out=test.iloc[:,-1]

# taking positive instances from training data to train the model
positive_train = train_in[train_out==1]

Hypothesis = []
for x in  range(0, 57):
    Hypothesis.append([])

#applying the algorithms 4.1 and 4.3 on positive trainuing examples
def LGG_ID(value,Hypothesis):
# Checking value whether it is in Hypothesis list or not  if value found in hypothesis return 0 else 1
    for element in Hypothesis:
        if element==value:  # Comparing with the hypothesis
            return 0
    return 1

for row in positive_train.values.tolist():
    # every element from each instance it goes till last column
    for j in range(0, len(row)):
       # if element(row[j]) not found in Hypothesis list then add the element to Hypothesis
        if (LGG_ID(row[j],Hypothesis[j])==1):
       # append row[j] to hypothesis list
            Hypothesis[j].append(row[j])

# printing thr hypothesis
for row in Hypothesis:
    print("(", end=" ")
    for j in range(0, len(row)):

        print(row[j], end=" ")
        if j != len(row) - 1:
            print("∨", end=" ")
    print(")", end=" ")
    print(" ^ ", end=" ")

print(" ")


# calculating the accuracy
tp, tn, fp, fn = 0,0,0,0
i = 0
for row in test_in.values.tolist():
    count = 0
    for j in range(0, len(row)):
        if row[j] in Hypothesis[j]:
            count = count + 1
    # calculating true positives
    if count == len(row) and test_out.iloc[i] == 1:
        tp = tp + 1

    # calculating true negatives
    if count != len(row) and test_out.iloc[i] == 0:
        tn = tn + 1

    # calculating false positives
    if count == len(row) and test_out.iloc[i] == 0:
        fp = fp + 1

    # calculating false negatives
    if count != len(row) and test_out.iloc[i] == 1:
        frn = fn + 1

    i = i + 1

# printing the accuracy
print("Accuiracy is :" +str((tp + tn)/(tp + tn + fp + fn)*100))














































