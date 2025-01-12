# create class
class Employee:
    
    # Initializing
    def __init__(self):
        print('Empoyee created')

    # Calling destructor
    def __del__(self):
        print("destructor called")

def Create_obj():
      print('Making Object...')
      obj = Employee()
      print('function end...')
      return obj
print('calling create_obj() fuunction...')
obj = Create_obj()
print('Program End...')