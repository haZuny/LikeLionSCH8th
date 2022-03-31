from django.db import models



# Create your models here.

#포토폴리오 카드 모델
class Card(models.Model):
    title = models.CharField(max_length=50)
    describe = models.TextField()
    img = models.ImageField(upload_to="images/")

