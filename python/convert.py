#chuong trinh 1
def nhiphan(n):
    s=0
    p=str(n)
    if p=="0":
        return 2
    p[::-1]
    for i in range(len(p)):
        if int(p[i])==1 :
            s=s+2**i
    return s
def thapphan(n):
    s=[]
    while n != 0:
        if n%2==1 :
            s.append("1")
            n=n//2
        else :
            s.append("0")
            n=n//2
    s=s[::-1]
    p="".join(s)
    return p
option=int(input("""1. nhị phân qua thập phân
2. thập phân qua nhị phân
"""))
if option==1 :
    N=int(input("Nhập số nhị phân cần đổi"))
    T=nhiphan(N)
    print(f"số thập phân đổi ra là:{T}")
elif option==2:
    N=int(input("Nhập số thập phân cần đổi: "))
    T=thapphan(N)
    print(f"số nhị phân đổi ra là:{T}")
else:
    print("chọn sai option rồi")
