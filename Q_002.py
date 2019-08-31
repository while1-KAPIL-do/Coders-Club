# Question - https://www.hackerrank.com/challenges/nested-list/problem

# Q_2 ( Solution )

def isListHaveSameValue(l):

    nl = []
    b = False
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if i!=j:
                if l[i][1] is l[j][1] :
                    nl.append(l[i][0])
                    nl.append(l[j][0])
                    nl.sort()
                    b = True
                    break
            if b:
                break
    if b:
        print(nl[0])
        print(nl[1])
        return True
    else:
        print("List have no same values...!")
        return False


l = [["kapil",1],["kapil2",2],["kapil3",3],["kapil4",4],["kapil5",5]]
print(isListHaveSameValue(l))

