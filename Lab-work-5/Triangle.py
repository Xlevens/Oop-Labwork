
class Triangle:
    __objcount = 0 #Private Class based variable for counting the iterationss
    def __init__(self, SideA = None,SideB = None,SideC =  None):
        Triangle.__objcount+=1
        if isinstance(SideA, Triangle) and SideB is None and SideC is None: #Getting the instance of the reference Triangle
            other = SideA
            self.sideA = other.sideA
            self.sideB = other.sideB
            self.sideC = other.sideC
        elif(SideA is None and SideB is None and SideC is None): #default Triangle with default values 
            self.sideA = 1.0
            self.sideB = 1.0
            self.sideC = 1.0
        elif(SideA is not None and SideB is None and SideC is None): #Equilateral Triangle
            self.sideA = SideA
            self.sideB = SideA
            self.sideC = SideA
        elif(SideA is not None and SideB is not None and SideC is None): #Isoceles Traingle
            self.sideA = SideA
            self.sideB = SideA
            self.sideC = SideB
        elif(SideA is not None and SideB is not None and SideC is not None): #Scalene Triangle
            self.sideA = SideA
            self.sideB = SideB
            self.sideC = SideC
        else:
            raise ValueError("Wrong info")
    #Getter/Setter using "@property" and "setter"
    @property
    def sideA(self):
        return self._sideA
    @sideA.setter
    def sideA(self,value):
        
        if value<0:
            raise ValueError("A should not be less than OR equal to 0")
        self._sideA = value
    @property
    def sideB(self):
        return self._sideB
    @sideB.setter
    def sideB(self,value):
        if value<0:
            raise ValueError("B should not be less than OR equal to 0")
        self._sideB = value
    @property
    def sideC(self):
        return self._sideC
    @sideC.setter
    def sideC(self,value):
        if value<=0:
            raise ValueError("C should not be less than OR equal to 0")
        self._sideC = value
    
    def parimeter(self):
        return self.sideA+self.sideB+self.sideC
    def IsRightAngle(self):#Check whether it's right angle or not and returns True and False
        num = sorted([self.sideA,self.sideB,self.sideC])
        a,b,c = num
        if pow(a,2) + pow(b,2) == pow(c,2):
            return True
        else:
            return False
    def ObjectCount(cls): 
        return cls.__objcount #retunring the amounth of iterations done
    def __str__(self):
        return f"Triangle with sides {self.sideA},{self.sideB},{self.sideC}"
    
    









        