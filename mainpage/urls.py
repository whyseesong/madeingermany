from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(?P<users_id>[0-9]+)/$', views.user_detail, name='user_detail'),
	url(r'^user/write/$',views.write_user, name='write_user' ),
	url(r'^add/user/$', views.add_user, name='add_user'), 
	url(r'^(?P<users_id>[0-9]+)/device/write/$', views.write_device, name='write_device'),
	url(r'^(?P<users_id>[0-9]+)/add/device/$', views.add_device, name='add_device'),
	url(r'^(?P<users_id>[0-9]+)/delete/device_check/$', views.delete_device, name='delete_device'),
	url(r'^(?P<users_id>[0-9]+)/delete/device/$', views.del_device_model, name='del_device_model'),
	url(r'^delete/user_check/$', views.delete_user, name='delete_user'),
	url(r'^delete/user/$', views.del_user_model, name='del_user_model'),
	url(r'^(?P<users_id>[0-9]+)/modify/$', views.modify_data, name='modify_data'),
	url(r'^(?P<users_id>[0-9]+)/modify/save/$', views.modify_save, name='modify_save'),
	url(r'^(?P<users_id>[0-9]+)/modify/device/check/$', views.modify_device_check, name='modify_device_check'),
	url(r'^(?P<users_id>[0-9]+)/modify/device/$', views.modify_device_model, name='modify_device_model'),
	url(r'^(?P<users_id>[0-9]+)/modify/device/save/$', views.modify_device_save, name='modify_device_save'),
	]
