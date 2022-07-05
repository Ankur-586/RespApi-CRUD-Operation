# Write a Python code to find the Requests module - version, licence, copyright information, author, author email, 
# document url, title and description.


from django.db import models

class ModuleApis(models.Model):
    version = models.IntegerField()
    license = models.TextField()
    copyright = models.TextField()
    information = models.TextField()
    author = models.TextField()
    author_email = models.EmailField()
    document_url = models.TextField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.license

    


      
