from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Users, Devices

def index(request):
	users_list = Users.objects.order_by('user_name')
	template = loader.get_template('mainpage/index.html')
	context = {
		'users_list' : users_list,
	}
	return HttpResponse(template.render(context, request))

def user_detail(request, users_id):
	#return HttpResponse("it's detail for %s" % Users.objects.get(pk=users_id))
	devices_list = Devices.objects.filter(user=users_id)
	template = loader.get_template('mainpage/user_detail.html')
	context = {
		'devices_list' : devices_list,
		'userinput' : Users.objects.get(id=users_id),
	}
	return HttpResponse(template.render(context, request))

def write_user(request):
	template = loader.get_template('mainpage/write_user.html')
	context = {
		#'users_list' : users_list,
	}
	return HttpResponse(template.render(context, request))
	
def add_user(request):
	template = loader.get_template('mainpage/write_user_status.html')
	
	if request.POST.has_key('username') == False:
		return HttpResponse('input user name')
	else:
		iusername = request.POST['username']
	if request.POST.has_key('usergrade') == False:
		return HttpResponse('input user grade')
	else:
		iusergrade = request.POST['usergrade']
	
	new_user = Users(user_name=iusername, grade=iusergrade)
	context = {
		'inputuser' : new_user
	}
	try:
		new_user.save()
	except:
		return HttpResponse('user write error')

	return HttpResponse(template.render(context, request))

def write_device(request, users_id):
	template = loader.get_template('mainpage/write_device.html')
	userclass = Users.objects.get(id=users_id)
	context = {
		'deviceuser' : userclass,
	}
	return HttpResponse(template.render(context, request))

def add_device(request, users_id):
	template = loader.get_template('mainpage/write_device_status.html')
	
	if request.POST.has_key('devicename') == False:
		return HttpResponse('input device name')
	else:
		idevicename = request.POST['devicename']
	if request.POST.has_key('deviceip') == False:
		return HttpResponse('input IP Address')
	else:
		ideviceip = request.POST['deviceip']
	if request.POST.has_key('user_id') == False:
		return HttpResponse('user id missing')
	else:
		try:			
			ideviceuser = Users.objects.get(id=request.POST['user_id'])
		except:
			return HttpResponse('user id missing!')
	
	new_device = Devices(device_name=idevicename, ip=ideviceip, user=ideviceuser, attestated_time=timezone.now())
	context = {
		'inputdevice' : new_device
	}
	try:
		new_device.save()
	except:
		return HttpResponse('device write error')

	return HttpResponse(template.render(context, request))

def delete_device(request, users_id):
	devices_list = Devices.objects.filter(user=users_id)
	template = loader.get_template('mainpage/check_delete_device.html')
	context = {
		'devices_list' : devices_list,
		'userinput' : Users.objects.get(id=users_id),
	}
	return HttpResponse(template.render(context, request))

def del_device_model(request, users_id):
	template = loader.get_template('mainpage/delete_device.html')
	context = {

	}
	
	instance = request.POST['deldevicelist']
	ddevice = Devices.objects.get(id=instance)
	ddevice.delete()
	#dlist[instance].delete()

	return HttpResponse(template.render(context, request))

def delete_user(request):
	template = loader.get_template('mainpage/check_delete_user.html')
	context={
		'userlist' : Users.objects.all(),
		'devicelist' : Devices.objects.all(),
	}
	return HttpResponse(template.render(context, request))
	pass

def del_user_model(request):
	template = loader.get_template('mainpage/delete_user.html')
	context = {

	}
	instance = request.POST['deluserlist']
	alldevice = Devices.objects.all()

	for ddev in alldevice:
		if ddev.user == instance:
			ddev.delete()

	duser = Users.objects.get(id=instance)
	duser.delete()

	return HttpResponse(template.render(context, request))

def modify_data(request, users_id):
	template = loader.get_template('mainpage/modify_data.html')
	muser = Users.objects.get(id=users_id)
	mdevices_list = Devices.objects.filter(user=users_id)
	context = {
		'muser' : muser,
		'mdevices_list' : mdevices_list
	}
	return HttpResponse(template.render(context, request))

def modify_save(request, users_id):
	template = loader.get_template('mainpage/modify_save.html')
	if request.POST.has_key('username') == False:
		return HttpResponse('input user name')
	else:
		iusername = request.POST['username']

	if request.POST.has_key('usergrade') == False:
		return HttpResponse('input user grade')
	else:
		iusergrade = request.POST['usergrade']

	muser = Users.objects.get(id=users_id)

	muser.user_name = iusername
	muser.grade = iusergrade
	muser.save()
	context = {

	}
	return HttpResponse(template.render(context, request))
	
def modify_device_check(request, users_id):
	devices_list = Devices.objects.filter(user=users_id)
	template = loader.get_template('mainpage/modify_device_check.html')
	context = {
		'devices_list' : devices_list,
		'userinput' : Users.objects.get(id=users_id),
	}
	return HttpResponse(template.render(context, request))

def modify_device_model(request, users_id):
	template = loader.get_template('mainpage/modify_device.html')
	instance = request.POST['deldevicelist']
	muser = Users.objects.get(id=users_id)
	mdevices = Devices.objects.get(id=instance)
	context = {
		'muser' : muser,
		'mdevices' : mdevices,
	}
	return HttpResponse(template.render(context, request))


def modify_device_save(request, users_id):
	template = loader.get_template('mainpage/modify_save.html')
	if request.POST.has_key('devicename') == False:
		return HttpResponse('input device name')
	else:
		idevname = request.POST['devicename']

	if request.POST.has_key('ipaddr') == False:
		return HttpResponse('input ip address')
	else:
		idevip = request.POST['ipaddr']

	devid = request.POST['mdevice_id']

	mdevice = Devices.objects.get(id=devid)

	mdevice.device_name = idevname
	mdevice.ip = idevip
	mdevice.save()
	context = {

	}
	return HttpResponse(template.render(context, request))

def device_attestation(request, users_id):
	template = loader.get_template('mainpage/modify_save.html')
	devid = request.POST['mdevice_id']
	mdevice = Devices.objects.get(id=devid)
	if mdevice.is_attestated == False:
		mdevice.is_attestated=True
		mdevice.attestated_time=timezone.now()

	else:
		mdevice.is_attestated=False
	mdevice.save()
	context = {

	}
	return HttpResponse(template.render(context, request))
	pass