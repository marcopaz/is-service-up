import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class Vultr(Service):
	name = 'Vultr'
	status_url = 'https://www.vultr.com/status'
	icon_url = '/images/icons/vultr.png'

	def get_status(self):
		r = requests.get(self.status_url)
		b = BeautifulSoup(r.content, 'html.parser')
		div = b.find('div', {'class': 'row'})
		status = div.findAll('i', {'class': 'zmdi'})
		if all('text-sucess' in str(s) for s in status):
			return Status.ok
		elif (any('text-warning' in str(s) for s in status) 
			or any('text-danger' in str(s) for s in status)):
			return Status.minor
		elif all('text-danger' in str(s) for s in status):
			return Status.critical
		else:
			raise Exception('unexpected status')
