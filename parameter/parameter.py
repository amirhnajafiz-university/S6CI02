from session.session import Session


"""
Parameter class.
    - fields:
        - a list of sessions
        - adding a new session method
        - removing a session method
        - choosing a session method

"""
class Parameter:
    def __init__(self):  # constructor
        # create a directory of sessions
        self.sessions = {}
    
    def NewSession(self, name):  # adding new sessions
        s = Session()
        self.sessions[name] = s 

        return s
    
    def DelSession(self, name):  # removing sessions
        self.sessions.pop(name)

    def With(self, name):  # choosing a session
        for i in self.sessions.keys():
            if i == name:
                return self.sessions.get(name)
        return None 
    
    def Input(self, x):  # check the results for an input
        temp = {}
        for s in self.sessions.keys():
            temp[s] = self.sessions.get(s).Input(x)
        return temp

    def Info(self):  # session information
        temp = {}
        for s in self.sessions.keys():
            temp[s] = self.sessions.get(s).Info()
        
        return dict(
            Length=len(self.sessions),
            Sessions=temp
        )
