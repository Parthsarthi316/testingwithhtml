print(2+3*5+6)
# for i in range (10):
#     print ("hello ",end="")
class Dog():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return ("Hello!!")
mydog=Dog('Eevee')
print(mydog)


try:
    f=open("simple.txt","r")
    # f.write("Happy bday!")
except IOError:
    print("Gadbad")
else:
    print("sab changa!")
    f.close()
finally:
    print("hamesha chalega ye!")
