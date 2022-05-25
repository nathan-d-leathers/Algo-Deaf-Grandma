def deaf_grandma():
    byCount = 0
    kid_rep = input()
    if len(kid_rep) == 0:
        print("WHAT!?")   
    if kid_rep.isupper() == True:
        print("NO, NOT SINCE 1946!")
    else:
        print("SPEAK UP KID!")
    if kid_rep == "GOODBYE" and byCount > 0:
        print("LATER, SKATER!")
    if kid_rep == "GOODBYE" and byCount == 0:
        byCount += 1
        print("LEAVING SO SOON?")
 
print(deaf_grandma())

# need to use user inputs to solve problem without exiting code function
