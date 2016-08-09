MadeInGermany
================
### administerating users and devices for remote attestation environments

## Features
+ User list view
+ Devices list view
+ New user save
+ User delete
+ User edit
+ New device save
+ Device delete
+ Device edit
+ device attestate

## Requirements
+ Python 2.7
+ Django 1.10

## Quick Start
1. Download these files in directory whatever you want.
2. Move your current directory to downloaded folder
3. excute terminal and use code below:
`
$ python manage.py runserver
`
4. Then the server will start on local
5. home address is **127.0.0.1:8080/mainpage/**

## Documentation
### page structure tree
+ user list (home)
	+ user detail (print user detail)
		+ save new device (input information about new device)
			+ print saving status (print device save completion message)
		+ delete device (check device to delete)
			+ print deletion status (print device delete completion message)
		+ modify user (input information about user to modify)
			+ print modification status (print user modification completion message)
		+ modify device (check device to modify)
			+ modify device detail (input information about device to modify)
				+ print modification status (print device modification completion message)
			+ device attestation (change isattestated value)
				+ print attestation status (print value modification completion message)
	+ new user (input information about new user)
		+ print saving status (print user save completion message))
	+ delete user (check user to delete)
		+ print deletion status (print user delete completion message)

### Views.py structure
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

### Classes & attributes
+ Users
	+ user_name
	+ grade
+ Devices
	+ device_name
	+ ip
	+ is_attestated
	+ attestated_time

### Functions
##### this document follows the structure mentioned at 'page structure tree' and 'Views.py structure' before.
+ index
###### load *mainpage/index.html* file and show user details. you can see user lists of name and user grade.
	+ click user name : jump to **user_detail**
	+ click new user : jump to **write_user**
	+ click delete user : jump to **delete_user**

+ user_detail
###### load *mainpage/user_detail.html* file. this page shows you user details(user name, user grade), and details of devices which current user have. device details include device name, ip address, is attestated, and attestated time.
	+ click new device : jump to **write_device**
	+ click delete device : jump to **delete_device**	
	+ click modify user : jump to **modify_data**	
	+ click modify device(*if device exists*) : jump to modify_device_check	
	+ click back : return to **index**

+ write_device
###### load *mainpage/write_device.html* file. you can enter attributes of new device : device name and ip address. 
	+ click save : jump to **add_device**
	+ click back : return to **index**

+ add_device
###### get some values(device name and ip address) from **write_device** and *manage/write_device.html* file with POST method. other values(is attestated and attestated time) are given with default value. the default value of 'is attestation' is False, and 'attestated time' is current saving time. with these values, function makes a new devices class and save to the database. then load *mainpage/wrtie_device_status.html* file. if save successes, device informations are printed on the page.
	+ click back : return to **index**

+ delete_device
###### load *mainpage/check_delete_device.html* file. with this file, page shows table of device list property of current user. the table has attributes consists of device name, ip address, is attestated and attestated time and checkbox to select be deleted. you can click checkbox and delete button to delete device which you want.
	+ click delete : jump to **del_device_model**
	+ click back : return to **index**

+ del_device_model
###### get id of device which you selected at **delete_device** function with *mainpage/check_delete_device.html* file. then find the device with id, and delete it from database. after deleting, load *mainpage/delete_device.html* file and print completion message.
	+ click back : return to **index**

+ modify_data
###### when you click modify user button at user detail with *mainpage/user_detail.html* file, this function is called. it loads *mainpage/modify_data.html* file, which allows you input user's new data. you can modify user's data(user name or grade) as input data and click save button.
	+ click save : jump to **modify_save**
	+ click back : return to **index**

+ modify_save

+ modify_device_check

+ modify_device_model

+ modify_device_save

+ device_attestation

+ write_user
###### load mainpage/write_user_status.html file. input user details(user name, user grade) to make a new user, and click save button.
	+ click save : jump to **add_user**
	+ click back : return to **index**

+ add_user

+ delete_user
###### load mainpage/check_delete_user.html file. this page shows you all of users and devices. check radiobox which you want to delete, and click delete button. if you delete user which have device(s), devices would be deleted though.
	+ click delete : jump to **del_user_model**
	+ click back : return to **index**

+ del_user_model