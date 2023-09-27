class Singleton(type):
    """
    This is the singleton class to created only one instance of the
    classes that need to guarantee that exists only one instance of
    itself
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Method to create and return the instance class if it has not been
        created, create the instance

        :param args:    dict    Arguments passed to instance
        :param kwargs:  dict    Arguments passed to create the instance
        :return:        object of instanced class
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
