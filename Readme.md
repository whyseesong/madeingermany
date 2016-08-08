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

###Functions
+ index
load mainpage/index.html file and show user details. you can see user lists of name and user grade.
	1. click user name : jump to **user_detail**
	2. click new user : jump to **write_user**
	3. click delete user : jump to **delete_user**

>+ user_detail
>load mainpage/user_detail.html file. this page shows you user details(user name, user grade), and details of devices which current user have. device details include device name, ip address, is attestated, and attestated time.
>	1. click new device : jump to **write_device**
>	2. click delete device : jump to **delete_device**
>	3. click modify user : jump to **modify_data**
>	4. click modify device(*if device exists*) : jump to modify_device_check
>	5. click back : return to **index**

>>+ write_device
>>asdfasdf

>+ write_user
>load mainpage/write_user_status.html file. input user details(user name, user grade) to make a new user, and click save button.
>	1. click save : jump to **add_user**
>	2. click back : return to **index**

>+ delete_user
>load mainpage/check_delete_user.html file. this page shows you all of users and devices. check radiobox which you want to delete, and click delete button. if you delete user which have device(s), devices would be deleted though.
>	1. click delete : jump to **del_user_model**
>	2. click back : return to **index**