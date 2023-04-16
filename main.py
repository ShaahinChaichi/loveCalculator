# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator! \n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name1_t = name1.lower().count('t')
name2_t = name2.lower().count('t')

name1_r = name1.lower().count('r')
name2_r = name2.lower().count('r')

name1_u = name1.lower().count('u')
name2_u = name2.lower().count('u')

name1_e1 = name1.lower().count('e')
name2_e1 = name2.lower().count('e')

name1_l = name1.lower().count('l')
name2_l = name2.lower().count('l')

name1_o = name1.lower().count('o')
name2_o = name2.lower().count('o')

name1_v = name1.lower().count('v')
name2_v = name2.lower().count('v')

name1_e2 = name1.lower().count('e')
name2_e2 = name2.lower().count('e')

name_sum_t = name1_t + name2_t
name_sum_r = name1_r + name2_r
name_sum_u = name1_u + name2_u
name_sum_e1 = name1_e1 + name2_e1

name_sum_l = name1_l + name2_l
name_sum_o = name1_o + name2_o
name_sum_v = name1_v + name2_v
name_sum_e2 = name1_e2 + name2_e2

print(f"number of t = {name_sum_t},number of r = {name_sum_r} \n"
      f"number of u = {name_sum_u},number of e1 = {name_sum_e1}\n",
      f"number of l = {name_sum_l},number of o = {name_sum_o}\n",
      f"number of v = {name_sum_u},number of e2 = {name_sum_e2}")

right_number = name_sum_t + name_sum_r + name_sum_u + name_sum_e1
left_number = name_sum_l + name_sum_o + name_sum_v + name_sum_e2

print(f"{right_number}{left_number}%")
