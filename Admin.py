class Admin(User):
    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)

    def add_user(self, user_details):
        pass
    def remove_user(self, user_id):
        pass
    def update_course_info(self, course_id, **kwargs):
        pass
    def create_course(self, course_id, course_details):
        pass