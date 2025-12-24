# student_solution.py

# ---------- ЗАДАНИЕ 1 ----------
def task1(s):
    # s — строка вида "подстрока1,подстрока2"
    # вернуть кортеж: (len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)
    "a"=s.split(",")
sub1="a"[0]
sub2="a"[1]
print(len(sub1) > len(sub2), sub1==sub2, sub2 in sub1)

# ---------- ЗАДАНИЕ 2 ----------
def task2(s):
    # s — любая строка
    # вернуть кортеж:
    # (s.strip(), len(s), s.count('a'), s.replace('a','@'), s.istitle())
    return s.strip()("  Hello World  ")
len("s") ("An apple a day")
"s".count("a")("The Quick Brown Fox")
"s".replace("a", "@")("aaAAbb")
"s".istitle()

# ---------- ЗАДАНИЕ 3 ----------
def task3(s):
    # s — строка
    # вернуть кортеж: (без первого и последнего символа, каждый второй символ, строка.lower() в обратном порядке)
    print((s[1:-1],s[::2]),s.lower()[::-1])
# ---------- ЗАДАНИЕ 4 ----------
def task4(nums):
    # nums — список чисел
    # вернуть кортеж: (отсортированный список, сумма, (min, max))
    num1 = sorted("nums")
num2 = sum("nums")
num3 = min("nums")
num4 = max("nums")
print(("num1", num2, num3, num4))


# ---------- ЗАДАНИЕ 5 ----------
def task6(s):
    # s — строка
    # вернуть True если палиндром (без учёта регистра) и нет пробелов, иначе False
    "a" = s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1] and " " not in s
print("a")

# ---------- ЗАДАНИЕ 6 ----------
def task7(n):
    # n — целое число
    # вернуть кортеж: (hex(n) без '0x', len(hex), True если 'a' есть в hex)
    "a"=hex(n).replace("0x", "")
print(("a", len("a"),"a" in "a" ))

# ---------- ЗАДАНИЕ 7 ----------
def task8(month_num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # вернуть название месяца по номеру (1-12)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    a=int(input())
    b=months[a-1]
    print(b)
