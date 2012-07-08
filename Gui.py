class Gui:
	
	def __init__(self):
		
		'''
		'''
		self.basic_ui_layout="""<?xml version="1.0" encoding="utf-8"?>
						<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
						android:id="@+id/background"
						android:orientation="vertical" android:layout_width="match_parent"
						android:layout_height="match_parent" android:background="#ff000000">
						
						<LinearLayout android:layout_width="match_parent"
						android:layout_height="wrap_content" android:id="@+id/linearLayout1">
						
						<TextView android:id="@+id/label"  
			              android:layout_width="wrap_content"  
			              android:layout_height="wrap_content"  
			              android:text="Select Item:" />
						
						<Spinner 
					        android:id="@+id/spinner"
					        android:layout_width="wrap_content"
					        android:layout_height="wrap_content"
					        android:prompt="Select Item from List"
				        />
				        </LinearLayout>
				        
				        
				        <LinearLayout android:layout_width="match_parent"
						android:layout_height="wrap_content" android:id="@+id/linearLayout2">
				        
				        <TextView android:id="@+id/label1"  
			              android:layout_width="wrap_content"  
			              android:layout_height="wrap_content"  
			              android:text="Select Amount" />
				        
				        <EditText android:layout_width="match_parent"
                         android:layout_height="wrap_content" android:id="@+id/Amount"
                          android:tag="Tag Me" android:inputType="textCapWords|textPhonetic|number">
                         <requestFocus></requestFocus>
                        </EditText>
                        
                        </LinearLayout>
                        
                        <LinearLayout android:layout_width="match_parent"
						android:layout_height="wrap_content" android:id="@+id/linearLayout3">
						
						<Button android:id="@+id/Save" android:layout_width="wrap_content"
								android:layout_height="wrap_content" android:text="Save"></Button>
								
						<Button android:id="@+id/Cancel" android:layout_width="wrap_content"
								android:layout_height="wrap_content" android:text="Cancel"></Button>
						</LinearLayout>  
						         
						
						</LinearLayout>"""
						
		
		
						
		
