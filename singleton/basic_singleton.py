class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() method')

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

a = ClassicSingleton.get_instance()
b = ClassicSingleton.get_instance()
c = ClassicSingleton.get_instance()

print(a.get_instance())
print(b.get_instance())
print(c.get_instance())
