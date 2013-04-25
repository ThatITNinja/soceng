#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  grapher.py
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

class Node(object):
    def __init__(self):
        self.attrs={}
        self.connected_to=[]
    def clear_connected(self):
        self.connected_to=[]
    def connect_to(self,node):
        self.connected_to.append(node)
    def is_connected(self,node):
        if node in self.connected_to:
            return True
        return False
    def get_connected(self):
        return self.connected_to
class Graph(object):
    nodes=[]
    def __init__(self):
        self.total_connections=0
        self.similar_nodes_amount=0
        self.unique_matches=[]
    def new_node(self,*args,**kwargs):
        node_var=Node()
        node_var.attrs=kwargs
        self.nodes.append(node_var)
        return node_var
    def remove_node(self,node):
        try:
            self.nodes.remove(node)
        except ValueError:
            return 1
    def remove_nodes(self,limit=1,*args,**kwargs):
        n_count=0
        del_count=0
        done=False
        for node in self.nodes:
            if done or del_count==limit:
                break
            for key,value in kwargs.items():
                if del_count==limit:
                    done=True
                if key in node.attrs:
                    if node.attrs[key]==value:
                        del self.nodes[n_count]
                        del_count+=1
            n_count+=1
    def loose_connect_nodes_by(self,*args,**kwargs):
        for a_node in self.nodes:
            for b_node in self.nodes:
                if a_node==b_node:
                    continue
                for k,v in kwargs.items():
                    if k in a_node.attrs and k in b_node.attrs:
                        if a_node.attrs[k]==v and b_node.attrs[k]==v:
                            if not a_node.is_connected(b_node) and not b_node.is_connected(a_node):
                                a_node.connect_to(b_node)
                                b_node.connect_to(a_node)
                                if not a_node in self.unique_matches:
                                    self.unique_matches.append(a_node)
                                if not b_node in self.unique_matches:
                                    self.unique_matches.append(b_node)
                    else:
                        continue
        self.similar_node_amount=len(self.unique_matches)
    def strict_connect_nodes_by(self,*args,**kwargs):
        for a_node in self.nodes:
            bad_a_node=False
            for k,v in kwargs.items():
                if k in a_node.attrs:
                    if a_node.attrs[k]==v:
                        continue
                    else:
                        bad_a_node=True
                        break
                else:
                    bad_a_node=True
                    break
            if bad_a_node:
                bad_a_node=False
                continue
            else:
                for b_node in self.nodes:
                    bad_b_node=False
                    for k,v in kwargs.items():
                        if k in b_node.attrs:
                            if b_node.attrs[k]==v:
                                continue
                            else:
                                bad_b_node=True
                                break
                        else:
                            bad_b_node=True
                            break
                    if bad_b_node:
                        bad_b_node=False
                        continue
                    else:
                        a_node.connect_to(b_node)
                        b_node.connect_to(a_node)
                        self.similar_nodes_amount+=1
                        if not a_node in self.unique_matches:
                            self.unique_matches.append(a_node)
                        if not b_node in self.unique_matches:
                            self.unique_matches.append(b_node)
    
