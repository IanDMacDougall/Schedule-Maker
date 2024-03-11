class Professor(User):
    def __init__(self, user_id, username, email, password, department, office_hours):
        super().__init__(user_id, username, email, password)
        #self.department = department
        #self.office_hours = office_hours
