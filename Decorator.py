from functools import wraps
def make_blinks(function):
    """ Defines the decorator """
    @wraps(function)
    #define the inner function
    def decorator():
        ret = function()
        return "<blink>"+ ret +"</blink>"#add new functionality to the function being decorated.
    return decorator

#apply the decorator here
@make_blinks
def hello_world():
    """Original Function """ 
    return "Hello World"
#check the results of decorating
print(hello_world())   
print(hello_world.__name__)   
print(hello_world.__doc__)   
