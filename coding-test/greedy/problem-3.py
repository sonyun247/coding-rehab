# problem 3 - 곱하거나 더하거나

inputNum = input();
result = int(inputNum[0]);

for i in range(1,len(inputNum)):
  nextNum = int(inputNum[i]);
  if result <= 1 or nextNum <= 1:
    result += nextNum;
  else:
    result *= nextNum;
print(result);