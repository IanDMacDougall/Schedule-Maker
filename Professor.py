class Professor(User):
    def __init__(self, user_id, username, email, department, office_hours):
        super().__init__(user_id, username, email)
        #self.department = department
        #self.office_hours = office_hours
