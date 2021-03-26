# class DatabaseException(Exception):
#     def __init__(self, err='NoSQL'):
#         Exception.__init__(self, err)
#
# class PreconditionsException(DatabaseException):
#     def __init__(self, err='PreconditionsErr'):
#         DatabaseException.__init__(self, err)
#
# def testRaise():
#     raise PreconditionsException()
# try:
#
#     raise PreconditionsException("aa")
#
# except PreconditionsException as e:
#
#     raise