from django.db import models


class Scheme(models.Model):
    SELECT = (
        ("Scholarship", "Scholarship"),
        ("Scheme", "Scheme"),
        ("Ed Loan", "Ed Loan")
    )
    TYPE = (
        ("State", "State"),
        ("Central", "Central")
    )
    CAT = (
        ("SC/ST", "SC/ST"),
        ("OBC", "OBC"),
        ("All", "All"),
        ("Kashmiri Migrants", "Kashmiri Migrants")
    )
    LEVEL = (
        ("Meritorious", "Meritotrious"),
        ("All", "All")
    )
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Both", "Both")
    )
    select = models.CharField(max_length=50, choices=SELECT)
    type = models.CharField(max_length=50, choices=TYPE)
    cat = models.CharField(max_length=50, choices=CAT)
    gender = models.CharField(max_length=50, choices=GENDER)
    level = models.CharField(max_length=50, choices=LEVEL)
    beneficiary = models.CharField(max_length=100)
    org = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField()
    desc = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title
