#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType
import pymysql as MySQLdb


import pyqtgraph as pq
import numpy as np

ui,_= loadUiType('plot.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        self.Handle_Buttons()
        
        
        
    
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.show_data)
        self.pushButton.clicked.connect(self.show_graph)
    
    def show_data(self):
        self.db=MySQLdb.connect(host='localhost', user='root', password='', db='data')
        self.cur=self.db.cursor()
        
        Query='''SELECT * FROM record '''
        
        if self.cur.execute(Query):
            data=self.cur.fetchall()
            
            self.tableWidget.insertRow(0)
            
            for row, row_data in enumerate(data):
                for col, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row,col,QTableWidgetItem(str(col_data)))
                    
                    col+=1
                
                row_position=self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                
    
    def show_graph(self):
        self.db=MySQLdb.connect(host='localhost', user='root', password='', db='data')
        self.cur=self.db.cursor()
        
        Query1='''SELECT house_size FROM record'''
        Query2='''SELECT price FROM record'''
        
        if self.cur.execute(Query1):
            house_size=self.cur.fetchall()
            
        if self.cur.execute(Query2):
            house_price=self.cur.fetchall()
            
        
        self.dataplot=self.graphicsView.addPlot(title="Price vs Size")
        
        housePrice=np.asarray(house_price)
        housePrice1D_Array=housePrice.flatten()
        
        
        houseSize=np.asarray(house_size)
        houseSize1D_Array=houseSize.flatten()
        
        self.dataplot.plot(houseSize1D_Array,housePrice1D_Array)
        
        
    
                

        
    

    
def main():
    app=QApplication(sys.argv)
    
    window=MainApp()
    window.show()
    app.exec_()
    
  
if __name__ == '__main__':
    main()


# In[ ]:




