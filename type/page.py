from enum import Enum

class PageType(Enum):
    ADMIN = "admin"
    PATIENT = "patient"
    NULL = "null"
    REGISTER = "register"
    LOGIN = "login"