from django.urls import path, include

urlpatterns = [
    path('', include('api.token.urls')),
    path('', include('api.fines.urls')),
    path('', include('api.payments.urls')),
    path('', include('api.pickup_points.urls')),
    path('', include('api.salaries.urls')),
    path('', include('api.shifts.urls')),
    path('', include('api.staff.urls')),
    path('', include('api.trainings.urls')),
]