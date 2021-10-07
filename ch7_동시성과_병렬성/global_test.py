class Point(object):
    def __new__(cls,*args,**kwargs):
        #print("From new")
        #print(cls)
        #print(args)
        #print(kwargs)
        # create our object and return it
        obj = super().__new__(cls)
        return obj
    def __init__(self, x = 0, y = 0):
        #print("From init")
        self.x = x
        self.y = y

class RectPoint(Point):
    MAX_Inst = 5555
    Inst_created = 777
    def __new__(cls,*args,**kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1
        print('Inst_created : ', cls.Inst_created)
        print('id(Inst_created) : ', id(cls.Inst_created))
        return super().__new__(cls)
    
    def test(self):
        print(self.__dict__)
        print('before : ', self.Inst_created)
        print('before id(Inst_created) : ', id(self.Inst_created))

        Inst_created = 10
        self.Inst_created = 20
        print(Inst_created)

        print(self.Inst_created)
        print('after id(Inst_created) : ', id(Inst_created))
        print('after id(self.Inst_created) : ', id(self.Inst_created))

        

p1 = RectPoint(0,0)
p1.test()
p1.test()

print('RectPoint.Inst_created : ', RectPoint.Inst_created)

p2 = RectPoint(2,0)
p2.test()
print('RectPoint.Inst_created : ', RectPoint.Inst_created)
