import android
import pdb
from Money_Planner import Money_Planner,DB_Connection
from data_report import DataReport #import start_data_report


class Start_App:
	
	def __init__(self):
		
		self.connect=DB_Connection()
		self.droid=android.Android()
		
	def start(self):
		'''
		'''
		self.cursor=self.connect.set_db_connection()
		self.xml_read=open("layout/Start_Gui.xml","r").read()
		self.droid.fullShow(self.xml_read)
		self.eventLoop()
		self.connect.connection.commit()
		
	
		
	
	def add_expenses_click(self):
		'''
		'''
		planner=Money_Planner(self.droid)
		planner.start_gui(self.cursor)
		self.droid.fullShow(self.xml_read)
		del planner
		return
		#pdb.set_trace()
		
	def view_expense_click(self):
		'''
		'''
		data=DataReport(self.droid)
		data.start_gui(self.cursor)
		self.droid.fullShow(self.xml_read)
		del data
		return
	
	
	def eventLoop(self):
		
		while(True):
			
			result=self.droid.eventWait().result
			print result
			
			if result["name"] == "click":
				
				id=result["data"]["id"]
				if id == "wid":
					#droid.fullDismiss()
					self.add_expenses_click()
					
				elif id == "view":
					self.view_expense_click()
			
			elif result["name"]=="key":
				id=result["data"]["key"]
				if id == "4":
					
					self.droid.fullDismiss()
					return





if __name__ == "__main__":
	
	start_app=Start_App()
	start_app.start()
