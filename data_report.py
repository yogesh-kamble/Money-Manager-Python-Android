import android
import pdb

class DataReport:
	
	def __init__(self,droid):
		self.droid=droid#android.Android()
	
	def get_data_report(self,cursor):
		'''
		'''
		query="select item.item_name,dat.entered_date,sum(item.amount) from date_table as dat,items as item where item.entered_date=dat.id group by item.item_name"
		#query_args=(date)
		cursor.execute(query)
		data_info_tuple=cursor.fetchall()
		
		return list(data_info_tuple)
		
	def start_gui(self,cursor):
		
		xml=open("layout/data_report.xml","r").read()
		data_info_tuple_list=self.get_data_report(cursor)
		print data_info_tuple_list
		#[(u'Shopping', 730), (u'Mobile', 30)]
		self.droid.fullShow(xml)
		data_list=[]
		coloumn_list=["Item_Name","Date","Amount"]
		data_list.append("   ".join(coloumn_list))
		
		
		for data in data_info_tuple_list:
			temp_data=list(data)
			temp_data[-1]=str(temp_data[-1])
			data_str="   ".join(temp_data)
			data_list.append(data_str)
		print data_list
		
		self.droid.fullSetList("mylist",data_list)
		#pdb.set_trace()
		while True:
			result=self.droid.eventWait().result
			if result["name"]=="key":
				id=result["data"]["key"]
				if id == "4":
					self.droid.fullDismiss()
					#self.droid.close()
					return
		

def start_data_report(cursor):
	
	data=DataReport()
	data.start_gui(cursor)
	return
