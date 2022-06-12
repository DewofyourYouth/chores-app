from django.db import models

# Create your models here.
class Family(models.Model):
    last_name = models.CharField(max_length=20)


class Parent(models.Model):
    first_name = models.CharField(max_length=20)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


class Child(models.Model):
    first_name = models.CharField(max_length=20)
    birthday = models.DateField(null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def child(self) -> str:
        return self.first_name

    def __repr__(self) -> str:
        return f"Child(first_name={self.first_name}, birthday={self.birthday}, family={self.family})"


class Task(models.Model):
    class ChoreType(models.IntegerChoices):
        DAILY = 1
        ALTERNATING = 2
        EXTRA_CREDIT = 3

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    points_value = models.FloatField()
    chore_type = models.IntegerField(
        choices=ChoreType.choices,
    )


class AccoutLog(models.Model):
    class ChoreState(models.IntegerChoices):
        DONE = 1
        NOT_DONE = 2
        VOID = 3

    class ActionType(models.IntegerChoices):
        CHORE = 1
        SPEND = 2

    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    action = models.CharField(max_length=200)
    action_type = models.IntegerField(choices=ActionType.choices)
    points = models.FloatField(default=0.0)
    chore = models.ForeignKey(
        Task,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    state = models.IntegerField(
        ChoreState.choices,
        default=ChoreState.VOID,
        null=True,
        blank=True,
    )
