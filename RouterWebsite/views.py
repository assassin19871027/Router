from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from RouterWebsite.models import Device, Notification, Rule, Traffic, SSID
import crypt


import re
# Create your views here.

def show_login(request):
  message_signup = ''
  error_message = ''
  if request.method == 'POST':
    postdata = request.POST.copy()
    if postdata['submit'] == 'login':
      email = postdata['email']
      password = postdata['password']
      username = ''
      try:
        user = get_object_or_404(User, email=email)
        username = user.username
      except:
        error_message = 'user does not exist.'
        return render_to_response('RouterWebsite/login.html', locals(), 
          context_instance=RequestContext(request))
      
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/home/')
           
        else:
            error_message = 'user is not active.'
            return render_to_response('RouterWebsite/login.html', locals(), 
              context_instance=RequestContext(request))
      else:
        error_message = 'username or password incorrect.'
        return render_to_response('RouterWebsite/login.html', locals(), 
          context_instance=RequestContext(request))

  if request.user.is_authenticated():
    return redirect('/home/')
  else:
    return render_to_response('RouterWebsite/login.html', locals(), 
      context_instance=RequestContext(request))

def show_logout(request):
  logout(request)
  return redirect('/login/')

@login_required(login_url='/login/')
def show_home(request):
  devices = Device.objects.all()
  devices_favo = devices[0:4]
  notifications = Notification.objects.all()
  notify = {}
  key_no = {}
  flag_notify = {}
  i = 0

  for device in devices:
    temp_notify = Notification.objects.filter(dev=device)
    if temp_notify:
      flag_notify[i] = device.domain
      for no in temp_notify:
        notify[i] = no.content
        key_no[i] = device.domain
        i = i + 1

  traffics = Traffic.objects.all()
  summar = 0
  for traffic in traffics:
    temp = (traffic.bandwidth * traffic.time * 60) / 1024
    summar = summar + temp
  return render_to_response('RouterWebsite/index.html', locals(), context_instance=RequestContext(request))

def show_register(request):
  request.session['message_register'] = ''
  error_message = ''
  if request.method == 'POST':
    postdata = request.POST.copy()
    if postdata['submit'] == 'signup':
      email = postdata['email']
      password = postdata['password']
      repeatpassword = postdata['repeat_password']
      if password == repeatpassword:
        if not re.match(r'^[A-Za-z0-9]{7}$',password) :
          error_message = "Password should be 7 charactors without special keys."
          return render_to_response('RouterWebsite/register.html', locals(), 
            context_instance=RequestContext(request))
        else:
          flag_user = 0
          username = ''
          try:
            user = get_object_or_404(User, email=email)
            username = user.username
            user.password = password
            user.save()
            flag_user = 1
          except:
            username = email
          if flag_user == 1:
            error_message = 'Username already exists. But you can now login using the new password'
            return redirect('/login/?message=Username already exists. But you can now login using the new password')
          else:
            error_message = 'Sucessfully added user.'
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('/login/?message=Sucessfully added user.')
      else:
        error_message = "Password and Repeat Password should be same."
        return render_to_response('RouterWebsite/register.html', locals(), 
          context_instance=RequestContext(request))
  return render_to_response('RouterWebsite/register.html', locals(), 
    context_instance=RequestContext(request))

@csrf_exempt
def show_signup(request):
  flag_success = 0
  postdata = request.POST.copy()

  email = postdata['email']
  password = postdata['password']
  repeatpassword = postdata['repeat_password']
  if password == repeatpassword:
    if not re.match(r'^[A-Za-z0-9]{7}$',password) :
      error_message = "Password should be 7 charactors without special keys."
      flag_success = 0
    else:
      flag_user = 0
      username = ''
      try:
        user = get_object_or_404(User, email=email)
        username = user.username
        user.password = password
        user.save()
        flag_user = 1
      except:
        username = email
      if flag_user == 1:
        error_message = 'Username already exists. But you can now login using the new password'
        flag_success = 1
      else:
        error_message = 'Sucessfully added user.'
        user = User.objects.create_user(username, email, password)
        user.save()
        flag_success = 1
  else:
    error_message = "Password and Repeat Password should be same."
    flag_success = 0
        
  return HttpResponse(error_message)

@login_required(login_url='/login/')
def show_user(request):
  devices = Device.objects.all()
  notifi = {}

  notify = {}
  key_no = {}
  flag_notify = {}
  i = 0

  for device in devices:
    temp_notify = Notification.objects.filter(dev=device)
    counter = temp_notify.count()
    notifi[device.id] = counter
    
    if temp_notify:
      flag_notify[i] = device.domain
      for no in temp_notify:
        notify[i] = no.content
        key_no[i] = device.domain
        i = i + 1
  
  return render_to_response('RouterWebsite/user.html', locals(), 
    context_instance=RequestContext(request))


@login_required(login_url='/login/')
def show_device(request, device_name):
  devices = Device.objects.filter(username=device_name)
  notifi = {}

  notify = {}
  key_no = {}
  flag_notify = {}
  i = 0

  for device in devices:
    temp_notify = Notification.objects.filter(dev=device)
    counter = temp_notify.count()
    notifi[device.id] = counter

    if temp_notify:
      flag_notify[i] = device.domain
      for no in temp_notify:
        notify[i] = no.content
        key_no[i] = device.domain
        i = i + 1

  return render_to_response('RouterWebsite/devices.html', locals(), 
    context_instance=RequestContext(request))

@login_required(login_url='/login/')
def show_ssid(request):
  if request.method == 'POST':
    postdata = request.POST.copy()
    if postdata['submit'] == 'Delete':
      ssid_id = postdata['ssid_id']
      ssid = get_object_or_404(SSID, id=ssid_id)
      ssid.delete()
    if postdata['submit'] == 'Create':
      ssid_name = postdata['ssid_name']
      ssid_network = postdata['ssid_network']
      ssid_password = postdata['ssid_password']
      if postdata['opt_password']:
        ssid = SSID(ssid_name=ssid_name,ssid_network=ssid_network,ssid_password=ssid_password,ssid_type=True)
        ssid.save()
      else:
        ssid = SSID(ssid_name=ssid_name,ssid_network=ssid_network,ssid_password=ssid_password,ssid_type=False)
        ssid.save()
  ssids = SSID.objects.all()
  return render_to_response('RouterWebsite/ssid.html', locals(),
    context_instance=RequestContext(request))

