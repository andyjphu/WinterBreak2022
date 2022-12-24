class helpers():
    def __init__(self) -> None:
        pass
    @staticmethod
    def truncate(value,degree_of_accuracy=3):
        __s__ = str(value).split(sep=".")
        try:
            return __s__[0] + "." + __s__[1][0:degree_of_accuracy]
        except IndexError:
            return __s__[0]