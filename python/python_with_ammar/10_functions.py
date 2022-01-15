#define function
#1
# def print_codanics():
#     print("we are learning python with ammar")
#     print("we are learning python with ammar")
#     print("we are learning python with ammar")
# print_codanics()

#2
def print_codanics():
    text="we are learning python with ammar"
    print(text)
    print(text)

print_codanics()
#3
def print_codanics(text):
    print(text)
    print(text)
print_codanics("we are learning python with ammar")    
#defining a function with if , else elif statement
def school_calcuator(age, text):
    if age==5:
        print("hammad can  join the school")
    elif age>5:
        print("hammad should go to high school")
    else:
        print("hammad is still a baby")

school_calcuator(2, "hammad")      
#defining a function of future 
def future_age(age):   
    new_age=age+20
    return new_age 
    print(new_age)
future_prected_age=future_age(18) 
print(future_prected_age)       