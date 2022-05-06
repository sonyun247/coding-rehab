# problem 4 - 모험가 길드

inputData = list(map(int, input().split()));
inputData.sort();
groupCount = 0;
userCount = 0;

for fearStat in inputData:
  userCount += 1;
  if userCount >= fearStat:
    groupCount += 1;
    userCount = 0;
  
print(groupCount);