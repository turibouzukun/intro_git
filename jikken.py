class TestClass():
    x="hello"

    def __init__(self,arg1):
        self.arg1=arg1
    
    def test_method1(self):
        print(self.x)
    def test_method2(self):
        print("引数1:"+self.arg1)

class className():
    def __init__(self,strA,strB):
        self.strA=strA
        self.strB=strB


#testClass=TestClass()
#testClass.test_method1()
#testClass.test_method2()

test=className("Hello","World")
test2=TestClass("argaaa")

test2.test_method2()

print(test.strA)
print(test.strA)

