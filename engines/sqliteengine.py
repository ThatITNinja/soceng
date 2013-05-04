#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sqliteengine.py
#  
#  Copyright 2013 ThatITNinja
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sqlite3

class SqliteEngine(class):
    def __init__(self,graph_object,database_path):
        self.db_conn=sqlite3.connect(database_path)
        self.db_cursor=self.db_conn.cursor()
        self.graph=graph_object
    def _unpack(self,list_obj):
        fin=[]
        for v_node in list_obj:
            for sub_val in len(v_node):
                fin.append(sub_val)
        return fin
    def rows_to_node(self,row_limit=None,table_name=None,*args,**kwargs):
        _conn=self.db_conn
        self.db_conn.row_factory=sqlite3.Row
        res=self.db_conn.fetchone()
        col_names=[x[0] for x in self.db_conn.description]
        self.db_conn=_conn
        if table_name != None:
            for r_count,row in enumerate(self.db_cursor.execute("SELECT * FROM (?) WHERE "+"AND ".join("(?)=(?)" for x in xrange(len(kwargs))),[table_name]+self._unpack(kwargs))):
                if row_limit != None and r_count==row_limit:
                    break
                node=self.graph.new_node()
                build_attribs=dict(x for x in zip(col_names,row))
                for k,v in build_attribs.items():
                    node.attrs[k]=v
        else:
            for table_name in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
                for r_count,row in enumerate(self.db_cursor.execute("SELECT * FROM (?) WHERE "+"AND ".join("(?)=(?)" for x in xrange(len(kwargs))),[table_name]+self._unpack(kwargs))):
                    if row_limit != None and r_count==row_limit:
                        break
                    node=self.graph.new_node()
                    build_attribs=dict(x for x in zip(col_names,row))
                    for k,v in build_attribs.items():
                        node.attrs[k]=v
    

