from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))

    def __str__(self):
        return self.name

    # class Meta:
    #     # 自定义权限
    #     permissions = (
    #         ("view_person", "Can view person entries"),
    #         ("edit_person", "Can edit person entries"),
    #     )



class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name