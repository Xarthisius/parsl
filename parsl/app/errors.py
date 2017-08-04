class ParslError(Exception):
    """ Base class for all exceptions

    Only to be invoked when only a more specific error is not available.
    """
    pass


class NotFutureError(ParslError):
    ''' Basically a type error. A non future item was passed to a function
    that expected a future.
    '''
    pass

class InvalidAppTypeError(ParslError):
    ''' An invalid app type was requested from the the @App decorator.
    '''
    pass


class AppException(ParslError):
    ''' An error raised during execution of an app.
    What this exception contains depends entirely on context
    '''
    pass

class AppFailure(ParslError):
    ''' An error raised during execution of an app.
    What this exception contains depends entirely on context
    Contains:
    reason (string)
    exitcode (int)
    retries (int/None)
    '''

    def __init__(self, reason, exitcode, retries=None, cmd_line=None):
        self.reason = reason
        self.exitcode = exitcode
        self.retries = retries
        self.cmd_line = cmd_line

    def __repr__ (self):
        return "AppFailure with code:{0} Reason:{1} cmd_line:{2}".format(self.exitcode, 
                                                                         self.reason, 
                                                                         self.cmd_line)

    def __str__ (self):
        return self.__repr__()

class MissingOutputs(ParslError):
    ''' Error raised at the end of app execution due to missing
    output files

    Contains:
    reason (string)
    outputs (List of strings/files..)
    '''

    def __init__(self, reason, outputs, cmd_line=None):
        self.reason = reason
        self.outputs = outputs
        self.cmd_line = cmd_line

    def __repr__ (self):
        return "Missing Outputs:{0} Reason:{1} cmd_line:{2}".format(self.outputs, 
                                                                    self.reason, 
                                                                    self.cmd_line)

    def __str__ (self):
        return self.__repr__()

class DependencyError(ParslError):
    ''' Error raised at the end of app execution due to missing
    output files

    Contains:
    reason (string)
    outputs (List of strings/files..)
    '''

    def __init__(self, dependent_exceptions, reason, outputs):
        self.dependent_exceptions = dependent_exceptions
        self.reason = reason
        self.outputs = outputs

    def __repr__ (self):
        return "Dependencies:{0}, Reason:{1} outputs:{2}".format(self.dependent_exceptions,
                                                                 self.reason,
                                                                 self.outputs)

    def __str__ (self):
        return self.__repr__()


