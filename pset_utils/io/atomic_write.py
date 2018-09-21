from contextlib import contextmanager
import os
import tempfile

@contextmanager
def atomic_write(file, mode='w', as_file=True, **kwargs):
    """Write a file atomically
    :param file: str or :class:`os.PathLike` target to write
    :param bool as_file:  if True, the yielded object is a :class:File.
        Otherwise, it will be the temporary file path string
    :param kwargs: anything else needed to open the file
    :raises: FileExistsError if target exists
    Example::
        with atomic_write("hello.txt") as f:
            f.write("world!")"""


    temp = tempfile.TemporaryFile()
    f = open(file, mode)
    f.write(temp)
    # get data on disk
    f.flush()
    os.fsync(f.fileno())
    f.close()

    os.rename(temp, file)
