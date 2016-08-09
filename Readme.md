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
1. Make directory or move to directory where you want to download.
2. Download files through code below:
`
$ git clone https://github.com/whyseesong/madeingermany.git
`
3. run server using code below:
`
$ python madeingermany/manage.py runserger
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
##### This document follows the structure mentioned at 'page structure tree' and 'Views.py structure' before.
+ #### index
###### Load *mainpage/index.html* file and show user details. You can see user lists of name and user grade.
	+ click user name : jump to **user_detail**
	+ click new user : jump to **write_user**
	+ click delete user : jump to **delete_user**

+ #### user_detail
###### Load *mainpage/user_detail.html* file. This page shows you user details(user name, user grade), and details of devices which current user have. Device details include device name, ip address, is attestated, and attestated time.
	+ click new device : jump to **write_device**
	+ click delete device : jump to **delete_device**	
	+ click modify user : jump to **modify_data**	
	+ click modify device(*if device exists*) : jump to modify_device_check	
	+ click back : return to **index**

+ #### write_device
###### Load *mainpage/write_device.html* file. You can enter attributes of new device : device name and ip address. 
	+ click save : jump to **add_device**
	+ click back : return to **index**

+ #### add_device
###### Get some values(device name and ip address) from **write_device** and *manage/write_device.html* file with POST method. Other values(is attestated and attestated time) are given with default value. The default value of 'is attestation' is False, and 'attestated time' is current saving time. With these values, function makes a new devices class and save to the database. Then load *mainpage/wrtie_device_status.html* file. If save successes, device informations are printed on the page.
	+ click back : return to **index**

+ #### delete_device
###### Load *mainpage/check_delete_device.html* file. With this file, page shows table of device list property of current user. The table has attributes consists of device name, ip address, is attestated and attestated time and checkbox to select be deleted. You can click checkbox and delete button to delete device which you want.
	+ click delete : jump to **del_device_model**
	+ click back : return to **index**

+ #### del_device_model
###### Get id of device which you selected at **delete_device** function with *mainpage/check_delete_device.html* file. tTen find the device with id, and delete it from database. After deleting, load *mainpage/delete_device.html* file and print completion message.
	+ click back : return to **index**

+ #### modify_data
###### When you click modify user button at **user detail** function with *mainpage/user_detail.html* file, this function is called. It loads *mainpage/modify_data.html* file, which allows you input user's new data. You can modify user's data(user name or grade) as input data and click save button.
	+ click save : jump to **modify_save**
	+ click back : return to **index**

+ #### modify_save
###### Get attributes about user from **modify_data** function with *mainpage/modify_data.html* file and save modified details of users at database. Then loads *mainpage/modify_save.html* file to print user modification completion message.
	+ click back : return to **index**

+ #### modify_device_check
###### Load *mainpage/modify_device_check.html* file to print detail device informations about current user. Check radiobox to modify device.
	+ click modify detail : jump to **modify_device_model**
	+ click back : return to **index**

+ #### modify_device_model
###### Load *mainpage/modify_device.html* file. if you want to change 'device name' or 'ip address', input new values and click save button. If you want to change 'is attestated' and 'attestated time', click attestation button.
	+ click save : jump to **modify_device_save**
	+ click attestation : jump to **device_attestation**
	+ click back : return to **index**

+ #### modify_device_save
###### Load *mainpage/modify_save.html* file to print device modification success. Get values of 'device id', 'device name' and 'ip address' sent form **modify_device_model** with post method. Find device class correspond with device id, modify attributes, and save to the database.
	+ click back : return to **index**

+ #### device_attestation
###### Load *mainpage/modify_save.html* file to print device attestation modification success. Get device id from *mainpage/modify_device.html* file with post method. Find device correct with the posted device id and change 'is_attestated' value to opposite value from bofore and 'attestated_time' value to current time.
	+ click back : return to **index**

+ #### write_user
###### Load mainpage/write_user_status.html file. Input user details(user name, user grade) to make a new user, and click save button.
	+ click save : jump to **add_user**
	+ click back : return to **index**

+ #### add_user
###### Get user details(user name, user grade) from *mainpage/write_device.html* file and *write_user* . Make new user class with these values and save it to database. Load *mainpage/write_user_status.html* file to print user save success message.
	+ click back : return to **index**

+ #### delete_user
###### Load *mainpage/check_delete_user.html* file. This page shows you all of users and devices. Check radiobox which you want to delete, and click delete button. If you delete user which have device(s), devices would be deleted though.
	+ click delete : jump to **del_user_model**
	+ click back : return to **index**

+ #### del_user_model
###### Get id of checked user from *mainpage/check_delete_user.html* file and **delete_user** . Find user correspond with given id and delete it from database. Load *mainpage/delete_user.html* file to print user delete success message.
	+ click back : return to **index**