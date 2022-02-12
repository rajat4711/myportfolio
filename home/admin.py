from django.contrib import admin
from .models import Home
from .models import skills
from .models import about
from .models import education
from .models import experience
from .models import services
from .models import projects
from .models import contact
from .models import Messages
from .models import blog
admin.site.register(Home)
admin.site.register(about)
admin.site.register(skills)
admin.site.register(education)
admin.site.register(experience)
admin.site.register(services)
admin.site.register(projects)
admin.site.register(contact)
admin.site.register(Messages)
admin.site.register(blog)
# Register your models here.
