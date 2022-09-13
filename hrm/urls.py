from django.urls import include, re_path
from rest_framework import routers
from hrm import views
from hrm.apiviews import EmployeeDetail

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet, basename="Department")

urlpatterns = [
    re_path('', include(router.urls)),
    re_path(r'^index', views.index),
    re_path(r'^emp/$', EmployeeDetail.as_view()),
    re_path(r'^emp/(?P<pk>[a-zA-Z0-9-]+)/$', EmployeeDetail.as_view()),
]
