def deaf_grandma():
    bye_count = 0
    kid_rep = input("HEY KID! ")
    
    while bye_count < 2:
        if len(kid_rep) == 0:
            kid_rep = input("WHAT? ")  
        elif kid_rep == "GOODBYE" and bye_count > 0:
            return("LATER, SKATER! ")
        elif kid_rep == "GOODBYE" and bye_count == 0:
            bye_count += 1
            kid_rep = input("LEAVING SO SOON? ")
        elif kid_rep.isupper() == True:
            kid_rep = input("NO, NOT SINCE 1946! ")
        else:
            kid_rep = input("SPEAK UP KID! ")

 
 
print(deaf_grandma())

# output in console:

# HEY KID! hi grandma
# SPEAK UP KID! HELLO
# NO, NOT SINCE 1946!  
# WHAT? GOODBYE
# LEAVING SO SOON? GOODBYE
# LATER, SKATER! 
