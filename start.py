"""
@ author : Alan Syue
@ created_date : 2019.06.23
@ see : https://github.com/AlanSyue/AppDataNofity
@ descrition : 
execute this python file will check the cookie file, crawl the data we need and send the eamil

"""
import setting
import mailText
import os
import cralwer
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class startCrawler():

	def getCookies(account,pwd,firebaseProjectName):
		googleCookiesPath=os.path.exists('./cookies/googleCookies.pkl')
		itunesCookiesPath=os.path.exists('./cookies/itunesCookies.pkl')
		firebaseCookiePath=os.path.exists('./cookies/firebaseCookies.pkl')
		appannieCookiePath=os.path.exists('./cookies/appAnnieCookies.pkl')

		print("====== Let's start to check if the file contain login cookie exists or not =======")

		if googleCookiesPath ==False:
			cralwer.playconsoleCralwer.getCookies(account['playconsole'],pwd['playconsole'])
			print('create googleCookies success')
		else:
			print('already exists googleCookies file')

		if itunesCookiesPath==False:
			cralwer.itunesCralwer.getCookies(account['itunes'],pwd['itunes'])
			print('create itunesCookies success')
		else:
			print('already exists itunesCookies file')

		if firebaseCookiePath==False:
			cralwer.firebaseCralwer.getCookies(account['firebase'],pwd['firebase'],firebaseProjectName)
			print('create firebaseCookies success')
		else:
			print('already exists firebaseCookies file')

		if appannieCookiePath==False:
			cralwer.appannieCralwer.getCookies(account['appannie'],pwd['appannie'])
			print('create appaniieCookies success')
		else:
			print('already exists appaniieCookies file')

		print("====== auto check was finished =======")

	def getData(account,pwd,playConsoleAccount,StatisticsPlace,googleAppId,iOSAppID,firebaseProjectName,country,andro_category,iOS_category):
		today = datetime.date.today()
		yesterday = today - datetime.timedelta(days=2)

		yesterday_split=str(yesterday).split('-')
		playconsole_date=yesterday_split[0]+yesterday_split[1]+yesterday_split[2]
		playconsole_date=playconsole_date+'-'+playconsole_date

		print("====== Let's start to crawling the data from third party tools =======")

		try:
			playconsoleData=cralwer.playconsoleCralwer.getData(playconsole_date,playConsoleAccount,StatisticsPlace)
		except:
			cralwer.playconsoleCralwer.getCookies(account['playconsole'],pwd['playconsole'])
			playconsoleData=cralwer.playconsoleCralwer.getData(playconsole_date,playConsoleAccount,StatisticsPlace)
		try:
			itunesConnect_data=cralwer.itunesCralwer.getData(yesterday,iOSAppID)
		except:
			cralwer.itunesCralwer.getCookies(account['itunes'],pwd['itunes'])
			itunesConnect_data=cralwer.itunesCralwer.getData(yesterday,iOSAppID)
		try:
			firebaseData=cralwer.firebaseCralwer.getData(firebaseProjectName)
		except:
			cralwer.firebaseCralwer.getCookies(account['firebase'],pwd['firebase'],firebaseProjectName)
			firebaseData=cralwer.firebaseCralwer.getData(firebaseProjectName)
		try:
			appannie_data=cralwer.appannieCralwer.getData(yesterday,googleAppId,iOSAppID,country,andro_category,iOS_category)
		except:
			cralwer.appannieCralwer.getCookies(account['appannie'],pwd['appannie'])
			appannie_data=cralwer.appannieCralwer.getData(yesterday,googleAppId,iOSAppID,country,andro_category,iOS_category)
		
		data_dict={}
		data_dict.update(playconsoleData)
		data_dict.update(itunesConnect_data)
		data_dict.update(firebaseData)
		data_dict.update(appannie_data)

		print("====== finished crawling the data from third party tools =======")

		return data_dict
class sendMail():

	def py_mail(SUBJECT, BODY, TO, FROM,password ):
	    """With this function we send out our html email"""
	    print("====== Start sending to "+TO+" =======")
	    # Create message container - the correct MIME type is multipart/alternative here!
	    MESSAGE = MIMEMultipart('alternative')
	    MESSAGE['subject'] = SUBJECT
	    MESSAGE['To'] = TO
	    MESSAGE['From'] = FROM
	    MESSAGE.preamble = """
	Your mail reader does not support the report format.
	Please visit us <a href="http://www.mysite.com">online</a>!"""

	    # Record the MIME type text/html.
	    HTML_BODY = MIMEText(BODY, 'html')

	    # Attach parts into message container.
	    # According to RFC 2046, the last part of a multipart message, in this case
	    # the HTML message, is best and preferred.
	    MESSAGE.attach(HTML_BODY)

	    # The actual sending of the e-mail
	    server = smtplib.SMTP('smtp.gmail.com:587')

	    # Credentials (if needed) for sending the mail
	    server.starttls()
	    server.login(FROM,password)
	    server.sendmail(FROM, [TO], MESSAGE.as_string())
	    server.quit()

	    print("====== finished sending to "+TO+" =======")
		
if __name__ == "__main__":

	"""Create variable from setting.py """
	account = setting.init()['account']
	pwd=setting.init()['pwd']
	playConsoleAccount=setting.init()['playConsoleAccount']
	StatisticsPlace=setting.init()['StatisticsPlace']
	googleAppId=setting.init()['googleAppId']
	iOSAppID=setting.init()['iOSAppID']
	country=setting.init()['appannie_parameter']['country']
	andro_category=setting.init()['appannie_parameter']['andro_category']
	iOS_category=setting.init()['appannie_parameter']['iOS_category']
	firebaseProjectName=setting.init()['firebaseProjectName']
	gmailAccount=setting.init()['sendFrom']['gmailAccount']
	gmailPwd=setting.init()['sendFrom']['gmailPwd']
	sendTo_list=setting.init()['sendTo_list']
	email_title=setting.init()['email_title']

	"""check the login cookies file exists or not """
	startCrawler.getCookies(account,pwd,firebaseProjectName)

	"""Start to crawling data and the function will return data (type = dict) """
	data_dict=startCrawler.getData(account,pwd,playConsoleAccount,StatisticsPlace,googleAppId,iOSAppID,firebaseProjectName,country,andro_category,iOS_category)

	"""input the data dictionary into the function and it will get the email content back """
	TEXT=mailText.getMail(data_dict)

	"""Start to send the email"""
	for email in sendTo_list:
		sendMail.py_mail(email_title, TEXT, email, gmailAccount,gmailPwd)
