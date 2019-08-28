def isdatevalid(d,m,y):
    if y>0 and (( m>=1 and m<=12) and ( ((m is 1 or m is 3 or m is 5 or m is 7 or m is 8 or m is 10 or m is 12) and (d >=1 and d<=31)) or ((m is 4 or m is 6 or m is 9 or m is 11) and ( d>=1 and d<=30)) or ((m is 2) and (d>=1 and d<=29) and ((y%100 is 0 and y%400 is 0) or (y%100 is not 0 and y%4 is 0))) or ((m is 2 ) and ( d>=1 and d<=28)) )):
        return True
    else:
        return False

d,m,y = input("Enter Date (d m y) - ").split(' ')
b = isdatevalid(int(d),int(m),int(y))
print(b)
