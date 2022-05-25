def deaf_grandma(str):
    response = ""
    byCount = 0
    
    if len(str) == 0:
        return("WHAT!?")   
    if str.isupper() == True:
        response = "NO, NOT SINCE 1946!"
    else:
        response = "SPEAK UP KID!"
    if str == "GOODBYE" and byCount > 0:
        return("LATER, SKATER!")
    if str == "GOODBYE" and byCount == 0:
        byCount += 1
        response = "LEAVING SO SOON?"
    return(response)
    
# Solved except for final GOODBYE, struggling to keep count of byCount when returning reponses
    
print(deaf_grandma("hello"))
print(deaf_grandma("HELLO"))
print(deaf_grandma(""))
print(deaf_grandma("GOODBYE"))
print(deaf_grandma("GOODBYE"))
