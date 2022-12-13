from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    ## for function based view
    # path('employee/', views.employee),

    ## for class based view 
    # path('employee/', views.Employee_details.as_view()),

    ## for function based api_view
    # path('employee/', views.employee, name='EmpDetails_list'),
    path('empdetails/', views.empdetails, name='EmpDetails'),
    # path('employee/<int:pk>', views.employee), # used to get endpoint from url while using browsable api

    ## for class based APIView
    # path('employee/',views.EmployeeAPI.as_view()),

    ## Generic Class Based View
    # path('employee/',views.EmployeeList.as_view()),
    # path('employee/',views.EmployeeCreate.as_view()),
    # path('employee/<int:pk>',views.EmployeeRetrive.as_view()),
    # path('employee/<int:pk>',views.EmployeeUpdate.as_view()),
    # path('employee/<int:pk>',views.EmployeeDestroy.as_view()),
    # path('employee/',views.EmployeeLC.as_view()),   # For list and post
    # path('employee/<int:pk>',views.EmployeeRUD.as_view()),   # for retirve, update and delete

    ## For concrete generic view
    # path('employee/', views.EmployeeList.as_view()),
    # path('employee/', views.EmployeeCreate.as_view()),
    # path('employee/<int:pk>', views.EmployeeRetrieve.as_view()),
    # path('employee/<int:pk>', views.EmployeeUpdate.as_view()),
    # path('employee/<int:pk>', views.EmployeeDelete.as_view()),    
    # path('employee/', views.EmployeeListCreate.as_view()),    
    # path('employee/<int:pk>', views.EmployeeRetrieveUpdateDestroy.as_view()),  

    # geo ip api url
    path('geoip/', views.home_geoip),
    path('github/', views.github),
    path('search/', views.odapi),

]

#-----------------------------------------------------------------------------------------------------------------------------


## For ViewSet

from rest_framework.routers import DefaultRouter

## Create default router object
router=DefaultRouter()

## register router object with url
# router.register('employeeapi',views.EmployeeViewSets, basename='empapi')

## For Modelviewset
#router.register('employeeapi',views.EmployeeModelViewSet, basename='empapi')

## For read only model viewset
#router.register('employeeapi',views.EmployeeROMVS, basename='empapi')


## Define where to find url
'''
urlpatterns=[
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), # for login/logout option on brosable API
]
'''


