
UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self,magnitude=0,unit="ml"):
        if type(magnitude)== int or type(magnitude)==float:
            if magnitude > 0 :
                self.__magnitude = magnitude
                if unit in UNITS:
                    self.__unit = unit  
                else:
                    self.__magnitude = None
                    self.__unit = None
            else:
                self.__magnitude = 0 
                self.__unit = None
        else:
            self.__magnitude = 0 
            self.__unit = None
       
        


        
        
    def __str__(self):
        if self.is_valid() == False:
            return ("Not a Volume")
        return "{:.3f} {}".format(self.__magnitude,self.__unit)

        
        
    def __repr__(self):    
        if self.is_valid() == False:
            return ("Not a Volume")
        
        return "{:.6f} {}".format(self.__magnitude,self.__unit)
        
    def is_valid(self):    
        if self.__unit == None:
            return False 
        else:
            return True 
        
    
    def get_units(self):     
        if self.is_valid() == True: 
            return self.__unit
        else:
            return None
        
    
    def get_magnitude(self):  
        return self.__magnitude
    
    def metric(self):     
        if self.is_valid() == True: 
            if self.__unit == "ml":
                return Volume(self.__magnitude,self.__unit)
            elif self.__unit == "oz":
                mag = self.__magnitude*MLperOZ
                A = "ml"
                return Volume(mag,A)
        else:
            return None


        
    def customary(self):    
        if self.is_valid() == True: 
            if self.__unit == "oz":
                return Volume(self.__magnitude, self.__unit)
            elif self.__unit == "ml":
                mag = self.__magnitude/MLperOZ
                A = "oz"
                return Volume(mag,A)
        else:
            return None

        
    def __eq__(self,other): 

        
        if not isinstance(other, Volume):
            return False
        if self.is_valid()== False:
            return False  
        elif other.is_valid() == False:
            return False
        if self.__magnitude == other.__magnitude and self.__unit == other.__unit:
            return True
        else:
            return False


        
       
    def add(self,other):
        if type(other) == float or type(other) == int:
            adding = self.__magnitude + other
            return Volume(adding,self.__unit )
        if self.is_valid() and other.is_valid():
            if self.__unit == other.__unit:
                adding = self.__magnitude + other.__magnitude
                return Volume(adding,self.__unit )
            else:
                if self.__unit == "oz":
                    change_val = other.customary()
                    adding = self.__magnitude + change_val.__magnitude
                    return Volume(adding,self.__unit )
                elif self.__unit == "ml":
                    change_val2 = other.metric()
                    adding = self.__magnitude + change_val2.__magnitude
                    return Volume(adding,self.__unit )
        
    
    def sub(self,other): 
        if type(other) == float or type(other) == int:
            sub = self.__magnitude - other
            return Volume(sub,self.__unit )
        if self.is_valid() and other.is_valid():
            if self.__unit == other.__unit:
                sub = self.__magnitude - other.__magnitude
                return Volume(sub,self.__unit )
            else:
                if self.__unit == "oz":
                    change_val3 = other.customary()
                    sub = self.__magnitude - change_val3.__magnitude
                    return Volume(sub,self.__unit )
                elif self.__unit == "ml" :
                    change_val4 = other.metric()
                    sub = self.__magnitude - change_val4.__magnitude
                    return Volume(sub,self.__unit )
