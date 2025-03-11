name = "Tom"
age = 22
score = 99.5

#%操作符输出
print("Name: %s, Age: %d, Score: %.2f" % (name, age, score))

#format()
print("Personal info: {} {} {}".format(name, age, score))

#f-string输出
print(f"Personal info :{name} {age} {score}")