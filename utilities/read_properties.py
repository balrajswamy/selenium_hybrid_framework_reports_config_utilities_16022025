import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get("admin_login_info","admin_page_url")
        return url

    @staticmethod
    def get_valid_user_email():
        valid_user_email = config.get("admin_login_info", "valid_user_email")
        return valid_user_email

    @staticmethod
    def get_valid_user_password():
        valid_user_password = config.get("admin_login_info", "valid_user_password")
        return valid_user_password
