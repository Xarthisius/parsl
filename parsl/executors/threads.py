import concurrent.futures
import logging
from parsl.executors.base import ParslExecutor

logger = logging.getLogger(__name__)

class ThreadPoolExecutor(ParslExecutor):
    ''' The thread pool executor
    '''

    def __init__ (self, max_workers=2, thread_name_prefix=''):
        ''' Initialize the thread pool
        '''
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    def shutdown(self, wait=True):
        ''' Calls the shutdown method of the underlying executor 
        Wait behavior from documentation :
                
        Signal the executor that it should free any resources that it is using when the 
        currently pending futures are done executing. Calls to Executor.submit() and 
        Executor.map() made after shutdown will raise RuntimeError.

        If wait is True then this method will not return until all the pending futures 
        are done executing and the resources associated with the executor have been freed. 
        If wait is False then this method will return immediately and the resources associated
        with the executor will be freed when all pending futures are done executing. 
        Regardless of the value of wait, the entire Python program will not exit until all
        pending futures are done executing.
        '''
        return self.executor.shutdown(wait=wait)
        
    def submit (self, *args, **kwargs):
        ''' Submits work to the thread pool
        This method is simply pass through and behaves like a submit call as described
        here `Python docs: <https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor>`_

        Returns:
              Future
        '''

        return self.executor.submit(*args, **kwargs)

    def scale_out (self, workers=1):
        ''' Scales out the number of active workers by 1
        This method is notImplemented for threads and will raise the error if called.

        Raises:
             NotImplemented exception
        '''

        raise NotImplemented

    def scale_in (self, workers=1):
        ''' Scale in the number of active workers by 1
        This method is notImplemented for threads and will raise the error if called.

        Raises:
             NotImplemented exception
        '''

        raise NotImplemented

