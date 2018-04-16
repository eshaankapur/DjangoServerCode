from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, render
from django.template import RequestContext
import datetime
import mysql.connector

from django.http import HttpResponseRedirect, HttpResponse

DB = 'tempdb'

def index(request):
    #return render_to_response('index2.html')
    return HttpResponse("sfs")
    #return render(request, 'index.html')

def getRestaurantList(request):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	rlist =[]
	srlist =" "
	cursor = cnx.cursor()
	query = ("select restaurant_name from myapp_restaurants")
	cursor.execute(query)
	for name in cursor:
		rlist.append(name)
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	return HttpResponse(rlist)
	#return HttpResponse([['abc','/','tand','/','sf'],['grg']])


def getRestaurantType(request, restaurant):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	rtype = ""
	cursor = cnx.cursor()
	query = ("select type from myapp_restaurants where restaurant_name = '%s'")
	cursor.execute(query % restaurant)
	for x in cursor:
		rtype = x
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	return HttpResponse(rtype)
	#return HttpResponse(["want " , restaurant])

def checkReservation(request,restaurant,date,time):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	found = 0
	cursor = cnx.cursor()
	query = ("select type from myapp_reservations where restaurant_name = '%s' AND date = '%s' AND time = '%s'")
	cursor.execute(query % restaurant % date % time)
	for x in cursor:
		found=found+1
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	if found ==0:
		return HttpResponse("Available")
	else:
		return HttpResponse("Booked")
	#return HttpResponse([restaurant , " on " , date , " at " , time])

def bookReservation(request,restaurant,date,time,username):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	cursor = cnx.cursor()
	query = ("select restaurant_id from myapp_restaurants where restaurant_name = '%s'")
	cursor.execute(query % restaurant)
	restaurant_id =""
	for x in cursor:
		restaurant_id =x
	query = ("insert into myapp_reservations (restaurant_id, date, time, username) values ('%s','%s','%s','%s')")
	done = cursor.execute(query % restaurant_id % date % time % username)
	cursor.close()
	cnx.close()
	return HttpResponse(done)
	#return HttpResponse([restaurant , " on " , date , " at " , time])

def authentication(request,username,password):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	found = 0
	cursor = cnx.cursor()
	query = ("select * from users where username='%s' AND password = '%s'")
	cursor.execute(query % username % password)
	for x in cursor:
		found=found+1
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	if found ==0:
		return HttpResponse("Incorrect")
	else:
		return HttpResponse("Correct")
	#return HttpResponse("good")

def getmenu(request,restaurant):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	menu =[]
	query = ("select restaurant_id from myapp_restaurants where restaurant_name = '%s'")
	cursor.execute(query % restaurant)
	restaurant_id =""
	for x in cursor:
		restaurant_id =x
	#srlist =" "
	cursor = cnx.cursor()
	query = ("select * from myapp_menu_items where restaurant_id_id = %s")
	cursor.execute(query % restaurant_id)
	for name in cursor:
		menu.append(name)
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	return HttpResponse(menu)

def checkusername(request,username):
	cnx = mysql.connector.connect(user='root', password='123',
                              host='localhost',
                              database='DB')
	found = 0
	cursor = cnx.cursor()
	query = ("select * from myapp_users where username='%s'")
	cursor.execute(query % username)
	for x in cursor:
		found=found+1
		#srlist = srlist + (String) name
	cursor.close()
	cnx.close()
	if found ==0:
		return HttpResponse("Available")
	else:
		return HttpResponse("Taken")
	#return HttpResponse("")

