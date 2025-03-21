GENDER: list = [["male", "MALE"], ["female", "FEMALE"]]


class RoleOptions:
    teacher: str = "Teacher"
    student: str = "Student"
    guardian: str = "Guardian"
    management: str = "Management"

    @classmethod
    def options(cls):
        return [
            (cls.teacher, "TEACHER"),
            (cls.student, "STUDENT"),
            (cls.guardian, "GUARDIAN"),
            (cls.management, "MANAGEMENT"),
        ]

    @classmethod
    def default(cls):
        return cls.teacher