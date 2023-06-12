import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def process_marks(records):
    students = []
    for record in records:
        name, email, *marks = record.split(',')
        if len(marks) != 3 or not all(mark.isdigit() and int(mark) >= 35 for mark in marks):
            continue
        if not validate_email(email):
            continue
        marks = list(map(int, marks))
        total_marks = sum(marks)
        students.append((name, email, marks, total_marks))

    students.sort(key=lambda x: x[3], reverse=True)
    rank = 1
    prev_total_marks = None
    for i, student in enumerate(students):
        if student[3] != prev_total_marks:
            rank = i + 1
            prev_total_marks = student[3]
        students[i] = student + (rank,)

    return students

# Test the program with the given sample input
sample_input = [
    "11",
    "Name-0,name0@gmail.com,80,92,80",
    "Name-1,name1@gmail.com,87,94,95",
    "Name-2,name2@gmail.com,98,95,78",
    "Name-3,name3@gmail..com,92,63,76",
    "Name-4,name4@gmail.com,90,86,88",
    "Name-5,name5@gmail.com,98,85,99",
    "Name-6,name6@gmail.com,83,,84",
    "Name-7,name7@gmail.com.,80,76,86",
    "Name-8,name 8@gmail.com,92,83,76",
    "Name-9,name9@gmail.com,90,95,86",
    "Name-10,name10@gmail.com,82,0,80"
]

num_records = int(sample_input[0])
records = sample_input[1:]

result = process_marks(records)

# Print the output
for i in range(len(result)):
    name, email, marks, total_marks, rank = result[i]
    marks_str = ','.join(str(mark) for mark in marks)
    print(f"{name},{email},{marks_str},{total_marks},{rank}")










# # You are using Python
# import re
# import copy
# def check_valid(email):
#     email = email.strip()
#     #print(email)
#     temp = r'^[\w\.-]+@[\w-]+\.\w+$'
#     match = re.match(temp, email)
    
#     if match:
#         #print(match)
#         return True
#     return False
    
# def check_all(email,m1,m2,m3):
#     if check_valid(email) and int(m1) >= 35 and int(m2) >= 35 and int(m3) >= 35:
#         return True
#     return False
    
# n = int(input())
# mat = []
# totals = []
# for _ in range(n):
#     try:
#         l = input().split(",")
#             #],l[3],l[4])
#         a = int(l[2])
#         b  = int(l[3])
#         c = int(l[4])
#         s = a+b+c
#         #print(l[0])
#         check_valid(l[1])
#         if check_all(l[1], l[2], l[3], l[4]):
#             l.append(s)
#             mat.append(l)
#             totals.append(s)
#     except:
#         pass
        
# #print(mat)
# ans = copy.deepcopy(mat)

# j = 0
# totals = list(set(totals))
# totals.sort(reverse=True)
# print(totals)
# for arr in mat:
#     i = totals.index(arr[-1])
#     ans[j].append(str(i+1))
#     j += 1
    
# for sublist in ans:
#     sublist_str = ' '.join(map(str, sublist))
#     print(sublist_str)

    






# s = input()
# n,k = map(int, input().split())

# s = "12321"
# n,k = 5,1

# changes = 0
# for i in range(n//2 ):
#     # print(k, "k")
#     if s[i] == s[-(i+1)]:
#         pass
#     else:
#         changes += 1
# # print("change", changes)
# if changes > k :
#     print("NO")
# elif k >= n :
#     print("9"*n)
# else:
#     diff = k-changes
#     l = list(s)
#     for i in range(n//2 ):
        
#         j = -(i+1)
#         # print("ij",i,j, diff)
#         if l[i] != l[j]:
#             if diff:
#                 l[i] = '9'
#                 l[j] = '9'
#                 diff -= 1
#             else:
#                 m = max(int(l[i]),int(l[j]))
#                 # print(m, "m")

#                 l[i],l[j] = str(m), str(m)
#         else:
#             pass

# if diff > 1:
#     for i in range(n//2):
#         if diff >1 :
#             if l[i] != "9":
#                 l[i] , l[-(i+1)] = "9", "9"
#                 diff -= 2
#         else:
#             break
# if diff == 1 and n % 2 != 0 :
#     l[n//2] = "9"

#         # print(l)
# print(l)





# def isValid(s):
#     numset = {}
#     numdic = {}
#     for i in s:
#         if i in numdic:
#             numdic[i] += 1
#         else:
#             numdic[i] = 1
            
        
    
#     for i in numdic:
#         if numdic[i] in numset:
#             numset[numdic[i]] += 1
#         else:
#             numset[numdic[i]] = 1
            
#     print(numset)
            
#     if len(numset) > 2:
#         return "NO"
#     elif len(numset) == 1:
#         return "YES"
#     else:
#         freq1, freq2 = numset.keys()
#         count1, count2 = numset.values()
#         if (count1 == 1 and (freq1 - freq2 == 1 or freq1 == 1)) or (count2 == 1 and (freq2 - freq1 == 1 or freq2 == 1)):
#             return "YES"
#         else:
#             return "NO"
        
# s = input()
# print(isValid(s))


# s 
# = input()
# n = len(s)
# subs = {}
# for i in range(0,n):  
#     for j in range(i,n):  
#         sub = (s[i:(j+1)])
#         sub_length = len(sub)
#         if sub_length in subs:
#             subs[sub_length].append(sub)
#         else:
#             subs[sub_length] = [sub]

# print(subs)

# #abba
# #{1: ['a', 'b', 'b', 'a'], 2: ['ab', 'bb', 'ba'], 3: ['abb', 'bba'], 4: ['abba']}
# #

# def anagram_pairs(strings):
#     anagram_dict = {}
#     for string in strings:
#         key = ''.join(sorted(string))
#         if key in anagram_dict:
#             anagram_dict[key] += 1
#         else:
#             anagram_dict[key] = 1
#     total_pairs = 0

#     for count in anagram_dict.values():
#         if count >= 2:
#             total_pairs += count//2

#     return total_pairs

# total_anagrams = 0
# # now for each length we iterate through their list- 
# # it will make it more optimized by not to go through the full list.
# for length in subs :
#     len_subs = subs[length]
#     total_anagrams += anagram_pairs(len_subs)

# print(total_anagrams)




# # print(arr)


