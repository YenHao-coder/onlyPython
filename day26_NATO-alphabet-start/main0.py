# Dictionary comprehension:
# new_dictionary = {new_key: new_value for item in list if test}
# new_dictionary = {new_key: new_value for (key, value) in dict.items() if test}

# List comprehension:
# new_list = [new_item for item in list if test]

# Ex:原列表中所有元素加1後，建立成新列表
"""原本方法:
num = [1,2,3]
new_num = []
for n in num:
    n = n+1
    new_num.append(n)"""

import random

number = [1,2,3]
naMe = "University"
friends = ['Alex', 'Beth', "Caroline", 'Dave', 'Elenrona','Fraddie']

# 一個全部加1的新陣列
new_num = [n+1 for n in number]
# 2倍數的新陣列
double_num = [n*2 for n in range(1,5)]
# 單字轉字母的新陣列
letters_list = [letter for letter in naMe]
# 名字5個字母以上的朋友改為大寫的陣列
caps_list = [name.upper() for name in friends if len(name) >= 5]
# 學生的成績字典
friends_scores = {student:random.randint(1,100) for student in friends}
# 成績及格與不及格
friends_passed = { student:"passed" for (student,score) in friends_scores.items() if score >= 60}

print(new_num)
print(double_num)
print(letters_list)
print(caps_list)
print(friends_scores)
print(friends_passed)