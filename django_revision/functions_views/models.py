from django.db import models

class indicator(models.Model):
    category = models.CharField(max_length=200)

class show_code(models.Model):
    category = models.ForeignKey(indicator , on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    code = models.CharField(max_length=50000)

    def __str__(self):
        return f'{self.title}' 