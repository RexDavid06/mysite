from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.name}  Subject: {self.subject}"
    

    class Meta:
        ordering = ['-date_sent']

    
