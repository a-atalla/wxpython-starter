from models import Session, User

s = Session()


class UserController(object):

    def get_all(self):
        
        all_users = s.query(User).all()
        
        return all_users
        
    def add_user(self, username, password, first_name, last_name):
        u = User(username, password, first_name, last_name)
        s.add(u)
        s.commit()
