from django.db import models
from django.utils.translation import gettext_lazy as _


class People(models.Model):
    TypeChoices = (
        (1, _("Student")),
        (2, _("Lecture"))
    )

    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150)
    type = models.IntegerField(choices=TypeChoices)
    email = models.EmailField()
    phone_no = models.CharField(max_length=14)

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"
