l = [3, 45, 53, 56]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# above can be simplified using enumerate function

print("USING ENUMERATE FUNCTION: ")

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
    