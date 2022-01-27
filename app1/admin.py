from cv2 import DRAW_MATCHES_FLAGS_DEFAULT
from django.contrib import admin
from .models import *

# Register Feedback Model
admin.site.register(Feedback)
admin.site.register(Form)