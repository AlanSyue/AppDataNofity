"""
@ author : Alan Syue
@ created_date : 2019.06.23
@ see : https://github.com/AlanSyue/AppDataNofity
@ descrition : 
You should set the value below to ensure the script run correct

"""
def init():
	setting={
		# set the following tool's account:google play console , iTunes connect , firebase , appannie
		'account':{'playconsole':'<account>',
					'itunes':'<account>',
					'firebase':'<account>',
					'appannie':'<account>'},

		# set the following tool's password:google play console , iTunes connect , firebase , appannie
		'pwd':{'playconsole':'<password>',
					'itunes':'<password>',
					'firebase':'<password>',
					'appannie':'<password>'},

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

	return setting
