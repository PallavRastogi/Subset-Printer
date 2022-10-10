# extremely compressed program, obfuscated by me
def subset(items):
    for i in range(2**len(items)):
        for t, po in enumerate(list(((len(items)-len(str(bin(i))[2:]))*"0") + str(bin(i))[2:])):
            if po == "1": print(items[t], end = " ")                
        print("\n")
#end


# create a binary number for each object, increment the binary number by 1 each time loop runs
# -
# for each digit of binary number, if digit is 1
# print the corresponding item
# else do not print
# print empty set {} at start
  
