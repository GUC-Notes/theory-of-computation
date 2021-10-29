import itertools
class DFA :
    def __init__(self,states, alphabet, transition, start_state , accepted_states) :
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accepted_states = accepted_states
        self.verify()
            
    def verify(self):
       
        if not all (x  in self.states and y in self.alphabet for (x,y) in self.transition):
            raise Exception("transition function is not valid")
       
        if not all(x in self.states for x in self.transition.values()):
            raise Exception("Transition function is not valid")
        
        if not all(pair  in self.transition.keys() for pair in itertools.product(self.states,self.alphabet)):
            raise Exception('Transition functioىnis not valid')
        if not all(state in self.states for state in self.accepted_states):
            raise Exception("accepted states is not valid")
        if self.start_state not in self.states:
            raise Exception('not valid start state')
        print ('DFA created succesfully') 
    
    def compute (self,input):
        current_state = self.start_state
        for element in input:
            if element not in self.alphabet:
                raise Exception('invalid input')
            current_state = self.transition[(current_state,element)]
        if current_state in self.accepted_states:
            print('accepted')
        else:
            print ('rejected')


