"""
@ author : Alan Syue
@ created_date : 2019.06.23
@ see : https://github.com/AlanSyue/AppDataNofity
@ descrition : 
this file contain email's HTML and the form of crawl data

"""
def dataTable(thirdPartyData):
	dataTable = """
	<table style="border:3px #cccccc solid;" cellpadding="10" border='1';"">
	    <tr>
	        <th>Android</th>
	        <th>data</th>
	    </tr>
	    <tr>
	        <td>daily acitve user</td>
	        <td>{andro_dau}</td>
	    </tr>
	    <tr>
	        <td>1-Day Retention</td>
	        <td>{andro_retention}</td>
	    </tr>
	    <tr>
	        <td>Google play store rank</td>
	        <td>{andro_rank}</td>
	    </tr>
	    <tr>
	        <th>iOS</th>
	        <th>data</th>
	    </tr>
	    <tr>
	        <td>daily acitve user</td>
	        <td>{iOS_dau}</td>
	    </tr>
	    <tr>
	        <td>1-Day Retention</td>
	        <td>{iOS_retention}</td>
	    </tr>
	    <tr>
	        <td>iOS store rank</td>
	        <td>{iOS_rank}</td>
	    </tr>
	    <tr>
	        <th>APP downloads</th>
	        <th>data</th>
	    </tr>
	    <tr>
	        <td>Android</td>
	        <td>{andro_download}</td>
	    </tr>
	    <tr>
	        <td>iOS</td>
	        <td>{iOS_download}</td>
	    </tr>
	</table>
	""".format(andro_dau=thirdPartyData['andro_dau'],andro_retention=thirdPartyData['andro_retention'],
		andro_rank=thirdPartyData['andro_rank'],iOS_dau=thirdPartyData['iOS_dau'],iOS_retention=thirdPartyData['iOS_retention'],
		iOS_rank=thirdPartyData['iOS_rank'],andro_download=thirdPartyData['andro_download'],iOS_download=thirdPartyData['iOS_download'])
	return dataTable

def getMail(thirdPartyData):
	dataTableValue=dataTable(thirdPartyData)
	TEXT = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="content-language" content="zh-tw" />
	<meta http-equiv="expires" content="-1" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
	<meta http-equiv="last-modified" content="<?=CFG_GMT;?>" />
	</head>
	<body>
	{dataTable}
	</body>
	</html>
	""".format(dataTable=dataTableValue)
	return TEXT
