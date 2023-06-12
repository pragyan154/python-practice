class myclass:
    count = 0
    def __init__(self):
        myclass.count += 1

    @classmethod
    def get_instance_count(cls):
        return cls.count
    

obj1 = myclass()
o2 = myclass()
print(myclass.get_instance_count())