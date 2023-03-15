from pathlib import Path
from typing import Callable, Iterable, Union

"""
    IO helper utilities for website project
"""

PathLike = Union[Path, str, None]

def to_path(p: PathLike) -> Path:
    return Path(p or "")

class _SafeIterable(Iterable):
    """
        Iterable wrapper proxy which guarantees handler() will be called at 
        end or (optionally, as with `finally`) on exception.

        Useful for preventing resource leaks.
    """
    def __init__(self, it: Iterable, handler: Callable, finally_):
        self.it = iter(it)
        self.handler = handler
        self.finally_ = finally_
        self.stopped = False

        if hasattr(self.it, "__iter__"):
            self.__iter__ = self.it.__iter__
        if hasattr(self.it, "__getitem__"):
            self.__getitem__ = self.it.__getitem__

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            v = next(self.it)
        except StopIteration:
            self._stop(False)
            raise
        except Exception:
            self._stop(True)
            raise
        return v

    def _stop(self, is_exc):
        if not self.stopped:
            self.stopped = True

            # call handler if on finally_ enabled or if
            # this is a normal stop
            if self.finally_ or not is_exc:
                self.handler()



def safe_iter(it: Iterable, handler: Callable, finally_=True) -> Iterable:
    return _SafeIterable(it, handler, finally_)