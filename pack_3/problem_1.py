class TStringStack:
    def __init__(self,string):
        self.string=string
        self.stack=""
    def check(self):
        for i in range(len(self.string)):
            if (self.string[i]=="{") 
            or (self.string[i]=="[") 
            or (self.string[i]=="(") 
            or (self.string[i]=="}") 
            or (self.string[i]=="]") 
            or (self.string[i]==")"):
                self.stack+=self.string[i]
            if self.string[i]=="}":
                if self.stack[len(self.stack)-2]=="{":
                    self.stack=self.stack[:-2]
                else:
                    return False
            if self.string[i]=="]":
                if self.stack[len(self.stack)-2]=="[":
                    self.stack=self.stack[:-2]
                else:
                    return False
            if self.string[i]==")":
                if self.stack[len(self.stack)-2]=="(":
                    self.stack=self.stack[:-2]
                else:
                    return False
        if self.stack=="":
            return True
        else:
            return self.stack
            
            
s=input()
x=TStringStack(str)
print(x.check())
