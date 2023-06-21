from django.urls import path
from agent import views
from agent.views import home,Listuser,Listagent,Postpackage,Listpackages

urlpatterns=[
    path('',views.index),
    path('listofusers',Listuser.as_view()),
    path('listofagents',Listagent.as_view()),
    path('login/',views.login),
    path('loginhome',views.log),
    path('updatestatus/<int:aid>/',views.updatestatus),
    path('areject/<int:aid>',views.agentreject),
    path('status/',views.ch),
    path('editagent/',views.editagent),
    path('updateagent/',views.updateagent),
    path('deleteagents/<int:aid>/',views.deleteagent),
    path('regis',views.usereg),
    path('agentregis',views.agentreg),
    path('hihi',views.home),
    path('searchp/',views.searchpackage),
    path('listofpackages',Listpackages.as_view()),
    path('updateuser',views.user_details_update),
    path('updateclient',views.client_details_update),
    path('deleteclients/<int:uid>/',views.deleteclient),
    path('addpackage',views.addpackage),
    path('listpackages',views.listpackage),
    path('pp',views.packagepost),
    path('request/<int:pid>/',views.packagerequest),
    path('viewreq/<int:pid>/',views.viewreq),

]