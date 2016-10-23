from django.views.decorators.csrf import csrf_exempt
import os,linecache
import sys
from django.shortcuts import render
from django.core.urlresolvers import resolve,reverse
from django.http import HttpResponseRedirect,HttpResponse, HttpResponseNotFound
import simplejson as json
from django.shortcuts import redirect
import requests
from django.template.loader import render_to_string
import ast


# Create your views here.


class WebRtcView():
	template_name = 'flockathon/webrtc.html'
	def get_queryset(self):
		return {}

class IndexView(BaseViewList):
	context_object_name = 'data'
	# paginate_by = 50

	def render_to_response(self, context, **response_kwargs):
		response = super(IndexView, self).render_to_response(context, **response_kwargs)
		return response

	def get_template_names(self):
		request = self.request
		template_name = 'flockathon/index.html'
		return [template_name]



from django.views.decorators.csrf import csrf_exempt
global users_flock
users_flock = {}
@csrf_exempt
def send(request):
	print ("called send")
	uf = open('/home/ubuntu/flockathon/uf.txt','a')
	ufr = open('/home/ubuntu/flockathon/uf.txt','r')
	try:
		print (request.path)
		print (request.POST)
		print (dir(request))
		print (request)
		print (request.GET)
		print (request.COOKIES)
		print (request.body)
		print(type(request.body))
		print(users_flock)
	except:
		pass
	token = "d2f7bf6e8f1bc88e12bbcb706a41da04b1477147115"
	to = 'u:hqbqssxhb7shrx3r'
	context = {}
	if request.method == 'POST':
		user_data = ast.literal_eval(str(request.body,'utf-8'))
		print (user_data)
		uf.write(user_data.get('userId') + " ---- " +user_data.get('token','null')+"\n")
		uf.close()
	else:
		try:
			gd = ast.literal_eval(request.GET.get('flockEvent'))
			for l in ufr.readlines():
				users_flock[l.split(" ---- ")[0]] = l.split(" ---- ")[1].strip()
			ufr.close()
			token = users_flock.get(gd.get('userId'))
			to = gd.get('chat')
			print (token,to)
		except:
			print ("exception")
			pass
	context['token']= token
	context['to']= to
	return render(request, 'register.html', context)

@csrf_exempt
def saveFile(request):
	print("Inside Save")
	print(request.FILES)
	print(request.FILES.get('file'))
	print(request.POST)
	ftype = request.POST.get('type',"webm")
	f = open("/home/ubuntu/askpopulo/media/fh/flockathon."+ftype,"wb")
	if request.FILES.get('file'):
		f.write(request.FILES.get('file').read())
	else:
		from base64 import b64decode
		import base64
		b64file = request.POST.get('file')
		b64file = b64file.replace('data:image/png;base64,', '').replace( ' ', '+')
#		m_p = len(b64file)%4
#		print(m_p)
#		if m_p != 0:
#			b64file += b'='*(4-m_p)
		image_data = b64decode(b64file)
		f.write(image_data)
	f.close()
	data = {}
	data['url'] ="https://www.askbypoll.com/media/fh/flockathon."+ftype
	return HttpResponse(json.dumps(data), content_type='application/json')

@csrf_exempt
def screen(request):
	token = request.path.split("/")[-1]#get('token')
	to = request.path.split("/")[-2]#GET.get('to')
	print (to,token)
	context = {}
	context['token']= token
	context['to']= to
	return render(request, 'screen.html', context)



