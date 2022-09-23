numbers=[]
print("Please enter 5 numbers, the system will give you the max number")
i=1
while i<6:
    try:
        numbers.append(float(input(f"""Enter #{i}: """)))
        i+=1
    except:
        print("only enter numeral caracters.")
        numbers.clear()
        i=1

print(f"""The list generate is: {numbers}""")
print("")
nMax=float("-inf")
for n in numbers:
    if nMax<n:
        nMax=n
print(f"""The max number is: {nMax}""")
