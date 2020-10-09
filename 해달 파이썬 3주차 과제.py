class SSoDDeok:
    def __init__(self,x,y):
        self.Sausage = x
        self.Ricecake = y


    def Making(self):
        x = self.Sausage
        y = self.Ricecake
        i = 1
        while i <= x or i <= y :
            if(x>=y):
                if(i <= self.Sausage):
                    print("$))))))")
                if (i <= self.Ricecake):
                    print("((((((@")
                i = i + 1
            else:
                if (i <= self.Ricecake):
                    print("((((((@")
                if (i <= self.Sausage):
                    print("$))))))")
                i = i + 1

        print("   |\n")


print("소떡소떡 몇개 주문하시겠어요??")
count = int(input())
print("소세지는 몇개로 하시겠나요??")
So = int(input())
print("떡은 몇개로 하시겠나요??")
DDuk = int(input())

SsoDDuk = []
i = 0
while i < count:
    SsoDDuk.append(SSoDDeok(So,DDuk))
    i = i + 1
i = 0
while i < len(SsoDDuk):
    SsoDDuk[i].Making()
    i = i + 1

print("주문하신 소떡소떡 나왔습니다. 소시지와 떡을 하나씩 드시면 더욱 맛있습니다! * $)))))) 이건 소세지고, ((((((@ 이건 떡입니다^^")