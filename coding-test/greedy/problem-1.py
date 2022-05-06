# 거스름돈
# https://youtu.be/2zjoKjt97vQ?t=243
# https://replit.com/@sonyun247/greedy-solution

count = 0;
money = 1260;

array = [500, 100, 50, 10];

for coin in array:
    count += money // coin;
    money %= coin;

print(count);