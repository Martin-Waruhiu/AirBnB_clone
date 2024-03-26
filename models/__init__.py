#!/usr/bin/python3
"""importing the storage class"""


from models.engine.file_storage import FileStorage
"""import the file storage class"""

storage = FileStorage()

storage.reload()
