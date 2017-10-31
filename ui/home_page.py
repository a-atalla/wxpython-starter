from ui.wxform.gui import PnlHome
from controllers import UserController


class HomePage(PnlHome):
    def __init__(self, parent):
        super(HomePage, self).__init__(parent)
        print(self.users_view)
        self.users_view.AppendTextColumn("count")
        self.users_view.AppendTextColumn("First Name")
        self.users_view.AppendTextColumn("Last Name")
        self.users_view.AppendTextColumn("username")
        self.users_view.AppendTextColumn("Password")

        # Get data and populate in teh view
        self.populate_user_view()

    def populate_user_view(self):

        uc = UserController()
        users = uc.get_all()

        for user in users:
            self.users_view.AppendItem([str(user.id),
                                        user.first_name,
                                        user.last_name,
                                        user.username,
                                        user.password])

    def on_btn_test(self, event):
        print('Test Button Clicked')
