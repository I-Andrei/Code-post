from django.db import models

class CodePost(models.Model):
    title = models.CharField(default='0000000', max_length=200)
    pub_date = models.DateTimeField('date published')
    post_content = models.CharField(default='0000000', max_length=200)