# Indexing = accessing elements of a sequence using [] (indexing operator)
#            [start  :  end  :  step]   we can access a staring point of a string an ending point and a step.abs

credit_num =  "1234-5678-1546-9985"

print(credit_num[0]) #print the index (1st letter in string)

print(credit_num[0:4]) # print first 4 letter of string

print(credit_num[5:9])# print next set of digit

print(credit_num[5:])  # print everything till the end of string

print(credit_num[-3]) # print the 3rd form ending 



# Step 
print(credit_num[::2]) # print every 2nd character in the string 

print(credit_num[::4]) # print every 4nd character in the string 

