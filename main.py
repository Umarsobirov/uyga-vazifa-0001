print("VAZIFALAR!")

# task 1
def salom():
    return f"Assalomu Alekum!"

s = salom()
print(s)




# task 2
def kv(x):
    return x**2

k = kv(6)
print(k)




# task 3
def sum23(a, b):
    return a+b   

a = sum23(5, 8)
print(a)


# task 4
def salom1(ism="Mehmon"):
    return f"Salom {ism}"

s1 = salom1()
print(s1)



# task 5
def harflar_soni(text):
    return len(text)

h = harflar_soni("Salom Dunyo!")
print(f"Text Uzunligi: {h}")


# task 6
def juftlar(sonlar: list):
    for i in sonlar:
        if i%2==0:
            yield i

j = juftlar([1,2,3,4,5,6,7,8])

for x in j:
    print(x)


# task 7
def salom_va_yosh(ism, yosh):
    def format(ism, yosh):
        return f"Ismi: {ism}, va yoshi {yosh}"
    return format(ism, yosh)

sy = salom_va_yosh("Umarbek", 20)
print(sy)




# task 8
def my_sums(*args):
    return f"Sonlar Yigindisi: {sum(args)}"

sm = my_sums(2, 3, 4, 5, 6)
print(sm)





# task 9
def info(**kwargs):
    return ", ".join(f"{k}: {v}" for k, v in kwargs.items())

inf = info(ism="Ali", yosh=25, kasb="dasturchi")
print(inf)



# task 10
def faktorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("n butun son bo'lishi kerak")
    if n < 0:
        raise ValueError("n manfiy bo'lmasligi kerak")

    if n == 0 or n == 1:
        return 1

    return n * faktorial(n - 1)

print(faktorial(0))   
print(faktorial(1))   
print(faktorial(5))   
print(faktorial(10))  

