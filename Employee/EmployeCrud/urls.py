from django.urls import path

from .views import index
from .views import create
from .views import store
from .views import edit
from .views import update
from .views import destroy

urlpatterns = [
    path('', index, name='employee'),
    path('employee/create/', create, name='employee_create'),
    path('employee/store/', store, name='employee_store'),
    path('employee/edit/<uuid:id>', edit, name='employee_edit'),
    path('employee/update/<uuid:id>', update, name='employee_update'),
    path('employee/destroy/<uuid:id>', destroy, name='employee_destroy'),
]
