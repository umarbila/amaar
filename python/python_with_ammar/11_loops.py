#while
# x=0
# while(x<5):
#     print(x)
#     x=x+1

#for loop
# for x in range(4,11):
#     print(x) 
    #array
days=["mon", "tue", "wed", "fri", "sat", "sun"]
for d in days:
    # if(d=="fri"):break
    if(d=="fri"):continue#skips d 
    print(d)