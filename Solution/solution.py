from itertools import permutations
import pandas as pd
df = pd.read_csv(r"C:\Users\raj\Desktop\Computer Languages\Python\AI & ML Academics\6citytsp.csv",header=None)
print(df)
# brute force approach
citylist = [0,1,2,3,4,5]
cost = []
startcity = int(input("Enter the startCity : "))
startcity_ = startcity
if startcity in citylist :
    citylist.remove(startcity)
else : 
    print("Error in the entering the city.")
per = list(permutations(citylist))
for i in per :
    cost_= 0
    for j in i :
        cost_ += df[startcity][j]
        startcity = j
    cost_ += df[startcity_][startcity]
    startcity = startcity_
    cost.append(cost_)
bestpath = []
for i in range(len(cost)) : 
    if cost[i] == min(cost) : 
        bestpath.append(list(per[i]))
for i in bestpath : 
    i.insert(0,startcity_)
    i.insert(6,startcity_)
print(f"According brute force approach, The best cost effective path or paths :  {bestpath}.")

#nearest neighbour approach
startCity = int(input("Enter the startCity : "))
startCity_ = startCity
bestpath = []
minValue = 0
minValueList = []
minIndexList = []

minIndex = 0
minIndexList.append(startCity)
for i in range(6)  : 
    tempList = list(df.loc[startCity])
    minValue = min(value for value in df.loc[startCity] if value not in minValueList and value != 0)
    minIndex = tempList.index(minValue)
    if minIndex in minIndexList :
        df[minIndex][startCity] = max(df.loc[startCity])
    else :
        startCity = minIndex
        minValueList.append(minValue)
        minIndexList.append(minIndex)
        bestpath.append(minIndex)
bestpath.insert(0,startCity_)
bestpath.insert(6,startCity_)
print(f"According nearest neighbour approach The best cost effective path is {bestpath}.")