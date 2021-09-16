from math import floor
year = int(input("year? "))
a = year % 19
b = floor(year // 100)
c = year % 100
d = floor(b // 4)
e = b % 4
f = floor((b + 8) // 25)
g = floor((b - f + 1) // 3)
h = (((19 * a) + b - d - g + 15) % 30)
i = floor(c // 4)
k = c % 4
l = ((32 + (2 * e) + (2 * i) - h - k) % 7)
m = floor((a + (11 * h) + (22 * l)) // 451)
month = floor((h + l + (7 * m) + 144) // 31) - 1
day = 1 + ((h + l - (7 * m) + 114) % 31)

print(year, month, "/", day)