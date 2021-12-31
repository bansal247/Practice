class student:
    
    def __init__(self, name, rollno, joining_date, current_topic):
        self.name = name
        self.rollno = rollno
        self.joining_date = joining_date
        self.current_topic = current_topic
    
    def name_parsing(self):
        if type(self.name) == list:
            for i in self.name:
                print(i)
        else:
            print("not in list")
        
    def crt_topic(self):
        print("current topic discussed in my class is ",self.current_topic)
    
    def str_roollno(self):
        try:
            if type(self.rollno) == str:
                print("do nothing")
            else:
                return str(self.rollno)
        except Exception as e:
            print(e)
    
    def duration(self,c_date):
        print("duration",c_date-self.joining_date)
        
    def __str__(self):
        return "this a studnt class where they can try to input there data and they can try to fetch it"