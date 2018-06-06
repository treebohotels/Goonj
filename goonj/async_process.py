import threading


class AsyncProcess(object):
    """
    Currently using threads to implement async tasks
    """

    @staticmethod
    def async_processor(method_to_execute, *args, **kwargs):
        thread = threading.Thread(target=method_to_execute, *args, **kwargs)
        thread.start()
