class Subject: 

    def __init__(self): 
        self.observers = [] 

 

    def attach(self, obs): 
        self.observers.append(obs) 

  

    def notify(self, data): 
        for o in self.observers: 
            o.update(data) 

 

# This class will be executed as an observer. It can be named anything 

class Observer: 

# The observer must have a function called update with these two parameters. 
    def update(self, data): 
        print(f"Observer 1 received: {data}") 

 

# This class will be executed as a second observer. It can be named anything 
class SecondObserver: 
    def update(self, data): 
        print(f"Observer 2 received: {data}") 

 

# Create subject and observers 
subject = Subject() 

subject.attach(Observer()) 

subject.attach(SecondObserver()) 

 

# Notify all observers 

subject.notify("Hello World") 