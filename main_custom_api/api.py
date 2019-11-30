from instagram import Account, WebAgent
from instagram.exceptions import InternetException

from main_custom_api.UserModelData import UserData

agent = WebAgent()


def get_inst_data(username):
    global agent

    try:
        account = Account(username)
        agent.update(account)
        return UserData(account)
    except InternetException:
        return None

