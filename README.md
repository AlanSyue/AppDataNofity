# AppDataNotify
This tool will automate collect the Apps data from the following sources:
1. Google Play Console ( https://developer.android.com/distribute/console/ )
2. iTunes Connect ( https://itunesconnect.apple.com/ )
3. firebase analytics ( https://firebase.google.com/ )
4. App Annie ( https://www.appannie.com/cn/ )
And it will send the mail to you via gmail you set, and this mail contain the data we crawled.

# Installation
## use version: Python 3.7.3
```
pip install selenium
```
```
pip install beautifulsoup4
```
```
pip install pickle
```
# How to use it
1. clone this repo to your local place :
```
git clone https://github.com/AlanSyue/AppDataNotify.git
```
2. open the `setting.py` file , and set the following value :
```
setting={
	# set the following tool's account:google play console , iTunes connect , firebase , appannie
	'account':{'playconsole':'<account>',
				'itunes':'<account>',
				'firebase':'<account>',
				'appannie':'<account>'},

	# set the following tool's password:google play console , iTunes connect , firebase , appannie
	'pwd':{'playconsole':'<password>@',
				'itunes':'<password>@',
				'firebase':'<password>@',
				'appannie':'<password>@'},

	# You can get playConsoleAccount, StatisticsPlace 's value from google play console'
	# see: https://play.google.com/apps/publish/?account={playConsoleAccount}#AppDashboardPlace:p={StatisticsPlace}
	'playConsoleAccount':'<google play console account>',
	'StatisticsPlace':'<google play console StatisticsPlace>',

	'googleAppId':'<google play store app id>',
	'iOSAppID':'<iOS app store app id>',
	# see https://www.appannie.com/apps/google-play/top-chart/?country={country}&category={andro_category}&device=
	# see https://www.appannie.com/apps/ios/top-chart/?country={country}&category={iOS_category}}&device=iphone
	'appannie_parameter':{'country':"<App Annie's country code>",'andro_category':"<App Annie's google play store category code>",'iOS_category':"<App Annie's iOS app store category code>"},
	# see https://console.firebase.google.com/u/0/project/{firebaseProjectName}/overview
	'firebaseProjectName':'<firebase project name>',
	'sendFrom':{'gmailAccount':'<gmail account>','gmailPwd':'<gmail password>'},
	'sendTo_list':['<email address>','<email address>'.....],
	'email_title':"today's App data, let's see it!", # the eamil title you want to set to 
}

```
3. execute the start.py :
```
python start.py

```
4. You will receive the email, and the email's format will like :

| Android                | data  |
|------------------------|-------|
| daily acitve user      | 22173 |
| 1-Day Retention        | 31.3% |
| Google play store rank | 1     |
| iOS                    | data  |
| daily acitve user      | 23956 |
| 1-Day Retention        | 34.5% |
| iOS store rank         | 1     |
| APP downloads          | data  |
| Android                | 2,602 |
| iOS                    | 2.95K |

5. use crontab to schedule getting daily Apps data ( for example : every 8:30 am execute start.py )
```
30    8     *     *     *     python /AppDataNofity/start.py

```
