from models import *


class ControllerEvent:
    pass


class ControllerGuest:
    pass


class ControllerGroup:
    @staticmethod
    def get_all_groups_by_user(user):
        return user.group.all()


class ControllerTemplate:
    pass
