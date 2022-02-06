from django.contrib import admin
# Register your models here.
from .models import Post
from .models import Question,Oops_modelans,Oops_userans,User,Dbms_userans,Dbms_modelans,Dbms_Question,Os_userans,Os_Question,Os_modelans
admin.site.register(Post)
admin.site.register(Question)
admin.site.register(Oops_modelans)
admin.site.register(Oops_userans)
admin.site.register(Dbms_Question)
admin.site.register(Dbms_modelans)
admin.site.register(Dbms_userans)
admin.site.register(Os_Question)
admin.site.register(Os_modelans)
admin.site.register(Os_userans)
admin.site.register(User)