class Student(User):
    def __init__(self, user_id, username, email, enrollment_year, major):
        super().__init__(user_id, username, email)
        self.enrollment_year = enrollment_year
        self.major = major

    def register_course(self, course_id):
        pass

    def drop_course(self, course_id):
        pass