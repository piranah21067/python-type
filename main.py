import random
import time
correct=0
print("------- welcome to python type -------")
print("------- by Tanish.K --------")
words= "i love python programming"
print("                 "+words)
start=time.time()
type= input("type words here: ")
end=time.time()
r = min( len(type) , len(words))

for i in range(r ):

    if words[i]==type[i]:
        correct= correct+1

print("----------- Statistics ---------------")
print("your accuracy is", (correct/len(type))*100,"%")
timeTaken=end-start
cps=correct/timeTaken
print("your cps is", cps)
cpm=cps*60
print("your clicks per minute is", cpm)
wpm=cpm/5
print("your wpm is", wpm)
print("--------------------------")