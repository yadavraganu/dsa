"""
__cause__ is the cause of the exception - due to the given exception, the current exception was raised.
This is a direct link - X threw this exception, therefore Y has to throw this exception.

__context__ on the other hand means that the current exception was raised while trying to handle another exception,
and defines the exception that was being handled at the time this one was raised. This is so that you don't lose the
fact that the other exceptions happened (and hence were at this code to throw the exception) - the context.
X threw this exception, while handling it, Y was also thrown.

__traceback__ shows you the stack - the various levels of functions that have been followed to get to the current
line of code. This allows you to pinpoint what caused the exception. It is likely to be used
(potentially in tandem with __context__) to find what caused a given bug.
"""
print('#' * 50 + 'Case 1' + '#' * 50)
try:
    number = int('N/A')
except Exception as e:
    print(
        f'Type of exception {type(e)}\n'
        f'Error : {e} \n'
        f'Below is the exception while handling that this exception is raised - {e.__cause__} \n'
        f'Below is the exception while handling that this exception is raised - {e.__context__} \n'
        f'Below is the error with params {e.args}')


class customException(Exception):
    def __init__(self, error):
        self.error = error
        self.err_typ = type(self.error)
        self.cause = self.error.__cause__
        self.context = self.error.__context__
        self.args = self.error.args
        super().__init__(
            f'Type of exeception {self.err_typ} \n'
            f'Error : {self.error} \n'
            f'Below is the exception which caused this exception - {self.cause} \n'
            f'Below is the exception while handling that this exception is raised - {self.context} \n'
            f'Below is the error with params {self.args}')


print('#' * 50 + 'Case 2' + '#' * 50)
try:
    try:
        number = 1 / 0
    except Exception as err:
        raise customException(err) from err
except Exception as error:
    raise customException(error)
