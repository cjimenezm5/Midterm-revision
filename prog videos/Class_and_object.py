
#class= blueprint
#object = instance of a class


class Computer:
    # put here attributes (variables) & behaviour (methods = functions)

    def __init__(self, cpu, ram): #usually used to visualise the variables, it's called automatically
        self.cpu = cpu
        self.ram = ram #this assigns it to teh object, each onject will now have its own cpu and ram


    def config(self): #must call config
        print("Configuration is:", self.cpu, self.ram)





comp1  = Computer("i5", "i5")
comp2 = Computer("Ryzen 3", 8)

comp1.config() #to get the method must mention the class first
comp2.config() #can also do this






















