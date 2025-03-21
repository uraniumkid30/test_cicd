from abc import ABC, abstractmethod


class GenderOptions:
    MALE: str = "male"
    FEMALE: str = "female"

    @classmethod
    def options(cls):
        return [(cls.MALE, "MALE"), (cls.FEMALE, "FEMALE")]

    @classmethod
    def default(cls):
        return cls.FEMALE


class CategoryOptions:
    SCIENCE: str = "Science"
    SCI_FI: str = "ScienceFiction"
    RELIGIOUS: str = "Religious"
    ART: str = "Art"
    GENERAL: str = "General"

    @classmethod
    def options(cls):
        return [
            (cls.SCIENCE, cls.SCIENCE.upper()),
            (cls.SCI_FI, cls.SCI_FI.upper()),
            (cls.RELIGIOUS, cls.RELIGIOUS.upper()),
            (cls.ART, cls.ART.upper()),
            (cls.GENERAL, cls.GENERAL.upper()),
        ]

    @classmethod
    def default(cls):
        return cls.GENERAL
