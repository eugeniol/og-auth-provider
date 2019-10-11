Initial Auth server that acts as OAuth2 provider.

This uses Django2.2 and this plugin https://github.com/Humanitec/django-oauth-toolkit-jwt


Caveats of that plugin (make need to fork it)
    algorithm='RS256' https://github.com/Humanitec/django-oauth-toolkit-jwt/blob/master/oauth2_provider_jwt/utils.py#L46


### Troubleshoot:

Create a fresh django 2.2 project (see the repo) connected to whiskey_mysql 
- run the migration
- attempt to login to whiskey admin
    It breakes since there is contenttypes migration that removes a column in database
    rollback contenttypes to 0001 `./manage.py migrate contenttypes 0001`
    - login works

- attemp to create a user account from 2.2 allauth sign up, account creates successfully 
- login as admin and make it super_user to check if new account as su can login to old django admin
- it breakes since it misses security user profile added by whiskey signal (https://github.com/ordergroove/whiskey/blob/master/api/security/models.py#L30)
    - Attach manually the UserProfile to that user and it works
- Attempt to login with new user into old dashboard.
    It breakes in this line https://github.com/ordergroove/data/blob/master/data/main/views.py#L135 sine  user.last_login is null. 
    Checking into database and user has last_login set, I belive the problem is django auth migration `./manage.py sqlmigrate auth 0005` that does `ALTER TABLE `auth_user` MODIFY `last_login` datetime(6) NULL;` that cause old django Datetime field cant be parsed into pytho date correctly.

    



### Comparation after auth_user table after migrate
    
Before auth_user 
```
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| username     | varchar(30)  | NO   | UNI | NULL    |                |
| first_name   | varchar(30)  | NO   |     | NULL    |                |
| last_name    | varchar(30)  | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| password     | varchar(128) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| date_joined  | datetime     | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```

After migration
```
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| username     | varchar(30)  | NO   | UNI | NULL    |                |
| first_name   | varchar(30)  | NO   |     | NULL    |                |
| last_name    | varchar(30)  | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| password     | varchar(128) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| date_joined  | datetime     | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
```



### Migratios from django 1.7 to 2.2

```
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0002
BEGIN;
--
-- Alter field name on permission
--
ALTER TABLE `auth_permission` MODIFY `name` varchar(255) NOT NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0003
BEGIN;
--
-- Alter field email on user
--
ALTER TABLE `auth_user` MODIFY `email` varchar(254) NOT NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0004
BEGIN;
--
-- Alter field username on user
--
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0005
BEGIN;
--
-- Alter field last_login on user
--
ALTER TABLE `auth_user` MODIFY `last_login` datetime(6) NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0006
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0007
BEGIN;
--
-- Alter field username on user
--
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0008
BEGIN;
--
-- Alter field username on user
--
ALTER TABLE `auth_user` MODIFY `username` varchar(150) NOT NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0009
BEGIN;
--
-- Alter field last_name on user
--
ALTER TABLE `auth_user` MODIFY `last_name` varchar(150) NOT NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0010
BEGIN;
--
-- Alter field name on group
--
ALTER TABLE `auth_group` MODIFY `name` varchar(150) NOT NULL;
COMMIT;
~/dev/og/ogauth/oauth3/oauth3 (master ✘) [venv]✹✚✭ ᐅ ./manage.py sqlmigrate auth 0011
BEGIN;
--
-- MIGRATION NOW PERFORMS OPERATION THAT CANNOT BE WRITTEN AS SQL:
-- Raw Python operation
--
COMMIT;
```

