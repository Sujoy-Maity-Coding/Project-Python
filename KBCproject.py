#Kon banega crorepoti app
que=[["A) Which country played in the first-ever Test match?","India","Australia","England","Pakistan",3],
    ["B) Highest team score in Test cricket.","1000","852","984","952",4],
    ["C) In which year was the first IPL season held?","2008","2012","2009","2014",1],
    ["D) Who has scored the most runs in the history of IPL?","Suresh Raina","Chris Gyle","Virat Kohli","Subhman Gill",3]]

money=[1000,2000,3000,5000]
name=input("Enter your name:")
s=0

for i in range(len(que)):
    print(f"\nHii {name},Your question for {money[i]} is:\n{que[i][0]}")
    print(f"1){que[i][1]}       2){que[i][2]}")
    print(f"3){que[i][3]}       4){que[i][4]}")
    ans=int(input("Enter correct answer(1 to 4):"))
    if(ans==que[i][5]):
        print(f"You won {money[i]} rupees.")
    else:
        print(f"Sorry Wrong answer, Correct answer is:{que[i][5]}")
        break
    n=i
    s=s+money[i]

print(f"\nYou give correct answer of {n+1} question. So You won total {s} rupees.")
print("Thanks for coming.")