from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository

class UserController:

    @staticmethod
    def registerUser(user = None):
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUsersAll():
        responseBody = UserRepository.getUsersAll()
        return ResponseEntity(body=responseBody)

    @staticmethod
    def getUser(username=None):
        responseBody = UserRepository.findUserByUsername(username)
        return ResponseEntity(body=responseBody)







