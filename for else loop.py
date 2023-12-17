##### can do same thing with while loop


for i in range(4):
    print(i)
else:
    print("agar loop puri execute hui to else wale part me jayega")

# 0
# 1
# 2
# 3
# agar loop puri execute hui to else wale part me jayega


for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("loop yaha puri execute nahi hui break hui hai to else wala block execute nahi hoga")
# 0
# 1
# 2
# 3
# 4
