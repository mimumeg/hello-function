def hello():
    print("Hello World")


hello()


def say_hello(name):
    print(f"Hi, {name}")


say_hello('Bob')
say_hello('Tom')


def double(number):
    return 2 * number


result_1 = double(3)
print(result_1)


# 1分課題
def str_combine(str1, str2):
    # return str1 + str2
    return f"{str1}{str2}"

result = str_combine("Kazuma", "Takahashi")  # TakahashiKazumaを返す
print(result)
