from django.db import models

class User(models.Model):
    username   = models.CharField(max_length = 50, unique = True)
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50)
    email  = models.EmailField(max_length = 70, blank = True, unique = True)
    password = models.CharField(max_length = 20)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
    class Meta:
      	db_table = "user"

class Post(models.Model):
 	user = models.ForeignKey(User, on_delete = models.CASCADE)
 	title = models.CharField(max_length = 100)
 	text = models.TextField()
 	created_at = models.DateTimeField(blank = True, null = True, auto_now_add = True)
 	updated_at = models.DateTimeField(auto_now = True)
 	def __str__(self):
 		return self.title

 	class Meta:
 		db_table = "post"