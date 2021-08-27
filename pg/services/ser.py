from pg.models import *
import calendar;
import time;

class mainService:
	def __init__(self, active = 1):
		self.need_img_status = active

	def getPortfolio(self):
		data = dict()

		portObj = Portfolio.objects.only('id', 'image', 'cat_id_id', 'created_date').filter(status = self.need_img_status).order_by('-id')

		temp_keys = list()
		port_info = dict()
		for port in portObj:
			temp = dict()
			temp['image'] = port.image
			temp['created_date'] = port.created_date

			if port.cat_id_id in temp_keys:
				port_info[port.cat_id_id][port.id] = temp
			else:
				port_info[port.cat_id_id] = dict()
				port_info[port.cat_id_id][port.id] = temp

				temp_keys.append(port.cat_id_id)

		data['port_info'] = port_info

		catObj = Category.objects.all()

		cat_info = dict()
		for cat in catObj:
			cat_info[cat.id] = cat.title

		data['cat_info'] = cat_info

		return data

	def storeMessage(self, request):
		err = dict()

		if not request.POST.get("name"):
			err['name'] = 'Name must be required'

		if not request.POST.get("email"):
			err['email'] = 'Email must be required'

		if not request.POST.get("phone"):
			err['phone'] = 'Mobile must be required'

		if not request.POST.get("message"):
			err['message'] = 'Message must be required'

		if bool(err) == True:
			return 	err

		conObj = Contact()
		conObj.name = request.POST.get("name")
		conObj.email = request.POST.get("email")
		conObj.phone = request.POST.get("phone")
		conObj.message = request.POST.get("message")
		conObj.created_date = calendar.timegm(time.gmtime())
		conObj.save()

		return {'success':'Message send successfully'}
