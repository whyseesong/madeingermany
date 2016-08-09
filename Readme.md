MadeInGermany
================
###administerating users and devices for remote attestation environments

##Features
+ User list view
+ Devices list view
+ New user save
+ User delete
+ User edit
+ New device save
+ Device delete
+ Device edit
+ device attestate

##Requirements
+ Python 2.7
+ Django 1.10

##Quick Start
1. Download these files in whatever you want.
2. Move your current directory to downloaded folder
3. excute terminal and use code below:
`
$ python manage.py runserver
`
4. Then the server will start on local
5. home address is **127.0.0.1:8080/mainpage/**

##Documentation
###Classes & attributes
+ Users
	+ user_name
	+ grade
+ Devices
	+ device_name
	+ ip
	+ is_attestated
	+ attestated_time

###Views.py structure
+ index
	+ user_detail
		+ write_device
			+ add_device
		+ delete_device
			+ del_device_model
		+ modify_data
			+ modify_save
		+ modify_device_check
			+ modify_device_model
				+ modify_device_save
			+ device_attestation
	+ write_user
		+ add_user
	+ delete_user
		+ del_user_model

###Functions
#####this document follows the structure mentioned at Views.py structure before.
+ index
######load mainpage/index.html file and show user details. you can see user lists of name and user grade.
	+ click user name : jump to **user_detail**
	+ click new user : jump to **write_user**
	+ click delete user : jump to **delete_user**

>>+ user_detail
>>######load mainpage/user_detail.html file. this page shows you user details(user name, user grade), and details of devices which current user have. device details include device name, ip address, is attestated, and attestated time.
	>>+ click new device : jump to **write_device**
	>>+ click delete device : jump to **delete_device**	
	>>+ click modify user : jump to **modify_data**	
	>>+ click modify device(*if device exists*) : jump to modify_device_check	
	>>+ click back : return to **index**

>>>+ write_device
>>>######load mainpage/write_device.html file. you can enter attributes of new device : device name and ip address. 
	>>>+ click save : jump to **add_device**
	>>>+ click back : return to **index**

>>>>+ add_device
>>>>######asdfasdf

>>>+ delete_device

>>>>+ del_device_model

>>>+ modify_data

>>>>+ modify_save

>>>+ modify_device_check

>>>>+ modify_device_model

>>>>>+ modify_device_save

>>>>+ device_attestation

>>+ write_user
>>######load mainpage/write_user_status.html file. input user details(user name, user grade) to make a new user, and click save button.
>>	+ click save : jump to **add_user**
>>	+ click back : return to **index**

>>>+ add_user

>>+ delete_user
>>######load mainpage/check_delete_user.html file. this page shows you all of users and devices. check radiobox which you want to delete, and click delete button. if you delete user which have device(s), devices would be deleted though.
>>	+ click delete : jump to **del_user_model**
>>	+ click back : return to **index**

>>>+ del_user_model