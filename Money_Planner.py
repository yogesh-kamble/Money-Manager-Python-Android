import android
import sqlite3
import urlparse
import json
import datetime,time 
import sys
from Gui import Gui
from data_report import DataReport
import pdb
#Following is fair idea of classes 



class Event:
	
	def __init__(self):
		pass
		
	


class DB_Connection:
	'''
	'''
	def __init__(self):
		'''
		'''
		self.connection=None
		self.cursor=None
		
	def set_db_connection(self):
		
		self.connection=sqlite3.connect("Testing.db")
		cursor=self.connection.cursor()
		return cursor
		
class Items:
	
	def __init__(self):
		'''
		'''
		pass
		
		
	def add_description(self,description):
		self.description=description
	
	def add_item_info(self,cursor,itemname,amount):
		#Add item to database
		query="insert into items(item_name,amount) values(?,?)"
		query_args=(itemname,int(amount))
		cursor.execute(query,query_args) 
		#connection_obj.connection.close()
		
	def get_default_items_list(self,cursor):
		'''
		'''
		query="select itemname from default_items"
		cursor.execute(query)
		result=cursor.fetchall()
		return [item[0] for item in result]
		
	def remove_item_info(self):
		#Remove Item from database
		pass
		






class Money_Planner:
	
	def __init__(self,droid):
		self.droid=droid
		#self.connection_obj=DB_Connection()
		self.gui=Gui()
		self.items=Items()
	
	def add_options(self):
		'''
		'''
		self.droid.addOptionsMenuItem("Off","off",None,"ic_menu_revert")
		self.droid.addOptionsMenuItem("Main Menu",None,"star_on")

	
	def on_save_click(self,default_item_list,cursor):
		'''
		'''
		Amount=self.droid.fullQueryDetail("Amount").result["text"]
		item_index=self.droid.fullQueryDetail("spinner").result["selectedItemPosition"]
		item_name=default_item_list[int(item_index)]
		self.items.add_item_info(cursor,item_name,Amount)
		self.droid.makeToast("Record Inserted")
		
	
	def on_display_click(self):
		
		data_obj=DataReport()
		data_report_tuple_list=data_obj.get_data_report(self.connection_obj,"2012-06-30")
		print data_report_tuple_list
	
	
	
	def start_gui(self,cursor):
		'''
		'''
		
		self.add_options()
		self.droid.fullShow(self.gui.basic_ui_layout)
		
		default_item_list=self.items.get_default_items_list(cursor)
		
		self.droid.fullSetList("spinner",default_item_list)
		
		while True:
			
			
			result=self.droid.eventWait().result
			print result
			print "----> event_name is %s"%(result['name'])  
			
			
			 
				
			if result['name'] == "click":
				
				id=result["data"]["id"]
				if id == "Save":
					self.on_save_click(default_item_list,cursor)
					
				elif id == "Cancel":
					self.droid.makeToast("No Record Inserted")
					self.droid.fullDismiss()
					return
					
				elif id == "Display":
					self.on_display_click()
				
				
			elif result["name"]=="off":
				self.droid.fullDismiss()
				return
			
			elif result["name"]=="key":
				id=result["data"]["key"]
				
				if id == "4":
					self.droid.fullDismiss()
					#self.droid.close()
					return

			
def start(cursor):
	
	'''
	'''
	planner=Money_Planner()
	planner.start(cursor)
	
	#connection_obj.connection.close()
	
	
	
	
	

if __name__ == "__main__":
	
	start()

