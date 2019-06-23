"""
@ author : Alan Syue
@ created_date : 2019.06.23
@ see : https://github.com/AlanSyue/AppDataNofity
@ descrition : 
this python file contain google play console,iTunes connect, firebase, appannie's get cookie file function and crawl data function

"""
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import pickle
import time

class playconsoleCralwer():
	"""docstring for appannieCralwer"""
	def getCookies(account,pwd):
		driver = webdriver.Chrome()
		driver.get("https://accounts.google.com/signin/v2/identifier?hl=zh-TW&passive=true&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgoogle%26oq%3Dgoogle%26aqs%3Dchrome..69i57j69i60l3j69i65l2.2835j0j1%26sourceid%3Dchrome%26ie%3DUTF-8&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
		time.sleep(5)
		driver.find_element_by_id('identifierId').send_keys(account)
		driver.find_element_by_id('identifierId').send_keys(Keys.ENTER)
		time.sleep(5)
		driver.find_element_by_class_name('whsOnd').send_keys(pwd)
		driver.find_element_by_class_name('whsOnd').send_keys(Keys.ENTER)
		time.sleep(10)
		pickle.dump( driver.get_cookies() , open("./cookies/googleCookies.pkl","wb"))

	def getData(date,playConsoleAccount,StatisticsPlace):
		# get play console data (download number)
		driver = webdriver.Chrome()
		playConsole_url='https://play.google.com/apps/publish/?account='+playConsoleAccount+'#StatisticsPlace:p='+StatisticsPlace+'&statms=DAILY_USER_INSTALLS&statgs=DAILY&statd=OS_VERSION&statc=false&dvals=@OVERALL@&dvals=28&dvals=26&dvals=27&dvals=23&cask=false&statdr='+date+'&statcdr='+date+'&grdk=@OVERALL@'
		driver.get(playConsole_url)

		googleCookies = pickle.load(open("./cookies/googleCookies.pkl", "rb"))
		for googleCookie in googleCookies:
			driver.add_cookie(googleCookie)

		driver.get(playConsole_url)
		time.sleep(10)
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		andro_download=bs.findAll('h3')[7].text
		print('Your Apps downloads number in Google play:'+andro_download)

		playconsoleData={'andro_download':andro_download}

		return playconsoleData

class appannieCralwer():
	"""docstring for ClassName"""
	def getCookies(account,pwd):
		driver = webdriver.Chrome()
		driver.get("https://www.appannie.com/account/login/?_ref=header")
		time.sleep(5)
		driver.find_element_by_id('email').send_keys(account)
		time.sleep(5)
		driver.find_element_by_id('password').send_keys(pwd)
		driver.find_element_by_id('submit').click()
		time.sleep(5)
		pickle.dump( driver.get_cookies() , open("./cookies/appAnnieCookies.pkl","wb"))

	def getData(date,googleAppId,iOSAppID,country,andro_category,iOS_category):
		# get appannie data (android,ios rank)
		driver = webdriver.Chrome()
		driver.get("https://www.appannie.com/account/login/?_ref=header")
		appAnnie_ios_url='https://www.appannie.com/apps/ios/top-chart/?country='+country+'&category='+iOS_category+'&device=iphone&date='+str(date)+'&feed=All&rank_sorting_type=rank&page_number=0&page_size=100&table_selections='
		appAnnie_andr_url='https://www.appannie.com/apps/google-play/top-chart/?country='+country+'&category='+andro_category+'&device=&date='+str(date)+'&feed=All&rank_sorting_type=rank&page_number=0&page_size=100&table_selections='

		appAnnieCookies = pickle.load(open("./cookies/appAnnieCookies.pkl", "rb"))
		for appAnnieCookie in appAnnieCookies:
			driver.add_cookie(appAnnieCookie)

		driver.get(appAnnie_ios_url)
		time.sleep(5)
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		iOS_rank=bs.find('td',{'data-appid':iOSAppID}).find_previous_sibling('td').text
		print('Your Apps rank in iOS store:'+iOS_rank)
		time.sleep(3)
		driver.get(appAnnie_andr_url)
		time.sleep(5)
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		andro_rank=bs.find('td',{'data-appid':googleAppId}).find_previous_sibling('td').text
		print('Your Apps rank in Google play:'+andro_rank)

		appannie_data={"iOS_rank":iOS_rank,'andro_rank':andro_rank}

		return appannie_data

class itunesCralwer():
	"""docstring for itunesCralwer"""
	def getCookies(account,pwd):
		driver = webdriver.Chrome()
		# get cookies from itunes connect
		driver.get("https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app")
		time.sleep(5)
		driver.switch_to_frame('aid-auth-widget-iFrame')
		# enter login
		driver.find_element_by_id('account_name_text_field').send_keys(account)
		driver.find_element_by_id('sign-in').click()
		time.sleep(5)
		driver.find_element_by_id('password_text_field').send_keys(pwd)
		driver.find_element_by_id('sign-in').click()
		time.sleep(5)
		pickle.dump( driver.get_cookies() , open("./cookies/itunesCookies.pkl","wb"))

	def getData(date,iOSAppID):
		# get itunes connect data (download number)
		base_url='https://appstoreconnect.apple.com/WebObjects/iTunesConnect.woa/ra/ng/app'
		iTunes_url = 'https://reportingitc2.apple.com/sales.html?startDate='+str(date)+'&endDate='+str(date)+'&filter_content='+iOSAppID+'&filter_content_type=22,31'
		driver = webdriver.Chrome()
		driver.get(base_url)

		itunesCookies = pickle.load(open("./cookies/itunesCookies.pkl", "rb"))
		for itunesCookie in itunesCookies:
			driver.add_cookie(itunesCookie)

		time.sleep(10)
		driver.get(iTunes_url)
		time.sleep(10)
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		iOS_download=bs.find('td',{'class':'status'}).text
		print('Your Apps downloads number in iOS store:'+iOS_download)

		itunesConnect_data={'iOS_download':iOS_download}

		return itunesConnect_data

class firebaseCralwer():
	"""docstring for firebaseCralwer"""
	def getCookies(account,pwd,firebaseProjectName):
		# get cookies from google login for firebase
		driver = webdriver.Chrome()
		driver.get("https://console.firebase.google.com/project/"+firebaseProjectName+"/overview")
		time.sleep(5)
		driver.find_element_by_id('identifierId').send_keys(account)
		driver.find_element_by_id('identifierId').send_keys(Keys.ENTER)
		time.sleep(5)
		driver.find_element_by_class_name('whsOnd').send_keys(pwd)
		driver.find_element_by_class_name('whsOnd').send_keys(Keys.ENTER)
		time.sleep(5)
		pickle.dump( driver.get_cookies() , open("./cookies/firebaseCookies.pkl","wb"))

	def getData(firebaseProjectName):
		# get firebase data (dau,retention)
		firebase_url='https://console.firebase.google.com/project/'+firebaseProjectName+'/overview'
		driver = webdriver.Chrome()
		driver.get(firebase_url)

		firebaseCookies = pickle.load(open("./cookies/firebaseCookies.pkl", "rb"))
		for firebaseCookie in firebaseCookies:
			driver.add_cookie(firebaseCookie)

		driver.get(firebase_url)
		time.sleep(10)
		bs = BeautifulSoup(driver.page_source, 'html.parser')
		andro_dau=bs.findAll('span',{'data-row':'1'})[0].text
		andro_retention=bs.findAll('span',{'data-row':'1'})[1].text
		iOS_dau=bs.findAll('span',{'data-row':'2'})[0].text
		iOS_retention=bs.findAll('span',{'data-row':'2'})[1].text
		print('Your Apps Daily Active User in Android:'+andro_dau+"\n"+'Your Apps retention in Android:'+andro_retention)
		print('Your Apps Daily Active User in iOS:'+iOS_dau+"\n"+'Your Apps retention in iOS:'+iOS_retention)

		firebaseData={'andro_dau':andro_dau,'andro_retention':andro_retention,'iOS_dau':iOS_dau,'iOS_retention':iOS_retention}

		return firebaseData
		
		
		
