def H(age,apples,cigs):
    answer = (100-age)+(apples*3.5)-(cigs-2)
    print (answer)
Sac=[27,20,0]
He=[54,24,0]
H(Sac[0],Sac[1],Sac[2])
H(*Sac)
H(*He)