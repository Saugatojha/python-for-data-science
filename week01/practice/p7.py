# Count how many characters are in the string "hello world" using a for loop (without len()).
# count = "hello world"
# print(len(count))
# print(count[0])
text = "hello world"
count = 0 
for i in text:
    count += 1
print("The number of letter is", count)