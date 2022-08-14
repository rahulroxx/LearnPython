class ExtendedClass(tuple):
    _variables = [1, 2, 4]
    
    ''' try to write a docstring '''
    def __init__(self, *args, **kwargs):
        self.class_variables = "this is class variable"
        super().__init__(*args, **kwargs)

    def __add__():
        return f"this is a static text nothign else "
        
    @staticmethod
    def test_class_staticmethod():
        return "this is a static method"
    
    @classmethod
    def test_class_method(cls):
        return cls._variables

# for x in dir(ExtendedClass): print(x)

test_one = ([1, 2, 4], )

test_one[0][2] = ['nested list']
print(test_one)
