import time
import names
import proxymanager
import threading
from utils import*
import requests
import random
delay = 0

url = "https://www.excelsiormilano.com/module/antcontactcustom/sendmail"
size = ['8', '8,5', '9', '9,5', '10', '11', '11,5', '12', '12,5', '13']
aptNum = 1

class entry(threading.Thread):
	def __init__(self,taskNum):
		threading.Thread.__init__(self)
		self.taskNum = taskNum
		self.s = requests.Session()
		self.s.headers = {
				'Origin':'https://www.excelsiormilano.com',
				'Referer':'https://www.excelsiormilano.com/content/45-nike-air-jordan-1-x-off-white',
				'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
			}
		self.s.headers.update()

		self.year = random.choice(range(1950, 2001))
		self.month = random.choice(range(1, 13))
		self.day = random.choice(range(1, 29))
		self.bDay = '{}-{}-{}'.format(str(self.year),str(self.month),str(self.day))
		self.phone = self.randomPhone()
		self.firstName = names.get_first_name()
		self.lastName = names.get_last_name()

		if catchall:
			self.email = self.firstName + '.' + self.lastName + '@' + domain
		else:
			self.email = baseEmail + "+{}@gmail.com".format(random.getrandbits(40))

		self.size = random.choice(size)
		self.data = {
			'first_name':self.firstName,
			'last_name':self.lastName,
			'birth':self.bDay,
			'mail':self.email,
			'number':self.phone,
			'size':self.size,
			'state':instagram,
			'country':country,
			'city':city,
			'zip':zipcode,
			'street': self.addyJig(street)
		}
	def run(self):
		self.proxy = random.choice(pm.formattedProxies)
		self.re = self.s.post(url, data=self.data, proxies=self.proxy)
		if self.re.status_code == 200:
			taskCLog(self.taskNum,"[{}] - {} - Succesful".format(self.re.status_code,self.email), "green")
		else:
			taskCLog(self.taskNum,"[{}] - {} - Failed".format(self.re.status_code,self.email), "green")

	def addyJig(self,street):
		global aptNum

		self.street = street + ', Suite {}'.format(str(aptNum))
		aptNum += 1
		return self.street
	def randomPhone(self):

		tempPhone = ''
		for i in range(0,9):
			tempPhone += str(random.randint(0,9))
		return tempPhone


if(__name__ == "__main__"):

	pm = proxymanager
	pm.importProxies('proxies')

	instagram = input('Instagram: ')
	country = input('Country: (full, not abbreviated. United States, Canada, etc) ')
	city = input('City:')
	zipcode = input("Zip: ")
	street = input("Street: ")
	strCatchAll = input('Catchall domain? type "yes" or "no"')
	if strCatchAll.lower() == 'yes':
		catchall = True
		domain = input('domain: (dont include the @) ')

	else:
		gmail = input('What is your full gmail? ')
		baseEmail = gmail.split('@')[0]
		domain = gmail.split('@')[1]
		catchall = False

	entries = input('Number of entries: ')
	delay = float(input('delay: '))

	for taskNum in range(0, int(entries)):
		t= entry(taskNum)
		t.start()
		time.sleep(delay)


