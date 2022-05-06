# 1이 될 때까지

a = int(input());
b = int(input());
count = 0;

while a != 1:
  if a % b == 0:
    a //= b;
    count += 1;
  else:
    a -= 1;
    count += 1;

print(count);
  
# solution - O(logN)
    
# a, b = map(int, input().split());
# count = 0;

# while true:  
#   target = (a//b)*b;
#   count += a - target
#   a = target 
#   if a < b :
#     break;
#   a //= b; 
#   count += 1;

# count += (a-1);
# print(count);

