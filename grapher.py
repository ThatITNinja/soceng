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
    def __init__(self):
        self.connections=0
        self.unique_matches=[]
        self.nodes=[]
    def clear_nodes_attrs(self):
        for x in self.nodes:
            x.attrs={}
    def clear_nodes_connections(self):
        for x in self.nodes:
            x.clear_connected()
        self.unique_matches=[]
        self.connections=0
    def remove_all_nodes(self):
        self.nodes=[]
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
    def loose_remove_nodes(self,limit=1,*args,**kwargs):
        del_count=0
        done=False
        def _():
            pass
        for n_count,node in enumerate(self.nodes[::]):
            if done or del_count==limit:
                break
            for k,v in kwargs.items():
                if k in node.attrs:
                    if node.attrs[k]==v:
                        del self.nodes[n_count]
                        del_count+=1
                        break_out=True
                        break
                    elif type(v)==type(_):
                        if v(node):
                            del self.nodes[n_count]
                            del_count+=1
                            break_out=True
                            break
            if break_out:
                continue
    def strict_remove_nodes(self,limit=1,*args,**kwargs):
        del_count=0
        done=False
        def _():
            pass
        for n_count,node in enumerate(self.nodes[::]):
            if done or del_count==limit:
                break
            bad_node=True
            for k,v in kwargs.items():
                if k in node.attrs:
                    if node.attrs[k]==v:
                        continue
                    elif type(v)==type(_):
                        if v(node):
                            continue
                        else:
                            bad_node=False
                            break
                    else:
                        bad_node=False
                        break
                else:
                    bad_node=False
                    break
            if not bad_node:
                continue
            else:
                del self.nodes[n_count]
                del_count+=1
                        
    def loose_connect_nodes_by(self,node_connect_limit=None,*args,**kwargs):
        bad_nodes=[]
        def _():
            pass
        for a_node in self.nodes:
            if a_node in bad_nodes:
                continue
            if node_connect_limit != None and node_connect_limit==len(a_node.get_connected()):
                bad_nodes.append(a_node)
                continue
            for k,v in kwargs.items():
                if k in a_node.attrs:
                    if a_node.attrs[k]==v:
                        continue
                    elif type(v)==type(_):
                        if v(a_node):
                            continue
                        else:
                            bad_nodes.append(a_node)
                            continue
                    else:
                        bad_nodes.append(a_node)
                        continue
                else:
                    bad_nodes.append(a_node)
                    continue
            for b_node in self.nodes:
                if b_node in bad_nodes or b_node==a_node:
                    continue
                if node_connect_limit != None and node_connect_limit==len(b_node.get_connected()):
                    bad_nodes.append(b_node)
                    continue
                for k,v in kwargs.items():
                    if k in b_node.attrs:
                        if b_node.attrs[k]==v:
                            if not b_node.is_connected(a_node):
                                b_node.connect_to(a_node)
                                self.connections+=1
                            if not a_node.is_connected(b_node):
                                a_node.connect_to(b_node)
                                self.similar_nodes_amount+=1
                            if not a_node in self.unique_matches:
                                self.unique_matches.append(a_node)
                            if not b_node in self.unique_matches:
                                self.unique_matches.append(b_node)
                        elif type(v)==type(_):
                            if not b_node.is_connected(a_node):
                                b_node.connect_to(a_node)
                                self.similar_nodes_amount+=1
                            if not a_node.is_connected(b_node):
                                a_node.connect_to(b_node)
                                self.connections+=1
                            if not a_node in self.unique_matches:
                                self.unique_matches.append(a_node)
                            if not b_node in self.unique_matches:
                                self.unique_matches.append(b_node)
                        else:
                            bad_nodes.append(b_node)
                            continue
                    else:
                        bad_nodes.append(b_node)
                        continue
        self.similar_nodes_amount=len(self.unique_matches)
    def strict_connect_nodes_by(self,node_connect_limit=None,*args,**kwargs):
        bad_nodes=[]
        def _():
            pass
        for a_node in self.nodes:
            if a_node in bad_nodes:
                continue
            if node_connect_limit != None and node_connect_limit==len(a_node.get_connected()):
                bad_nodes.append(a_node)
                continue
            bad_a_node=False
            for k,v in kwargs.items():
                if k in a_node.attrs:
                    if a_node.attrs[k]==v:
                        continue
                    elif type(v)==type(_):
                        if v(a_node):
                            continue
                        else:
                            bad_a_node=True
                            break
                    else:
                        bad_a_node=True
                        break
                else:
                    bad_a_node=True
                    break
            if bad_a_node:
                bad_nodes.append(a_node)
                continue
            else:
                for b_node in self.nodes:
                    if b_node in bad_nodes or b_node==a_node:
                        continue
                    if node_connect_limit != None and node_connect_limit==len(b_node.get_connected()):
                        bad_nodes.append(b_node)
                        continue
                    bad_b_node=False
                    for k,v in kwargs.items():
                        if k in b_node.attrs:
                            if b_node.attrs[k]==v:
                                continue
                            elif type(v)==type(_):
                                if v(b_node):
                                    continue
                                else:
                                    bad_b_node=True
                                    break
                            else:
                                bad_b_node=True
                                break
                        else:
                            bad_b_node=True
                            break
                    if bad_b_node:
                        bad_nodes.append(b_node)
                        continue
                    else:
                        if not a_node.is_connected(b_node):
                            a_node.connect_to(b_node)
                            self.connections+=1
                        if not b_node.is_connected(a_node):
                            b_node.connect_to(a_node)
                            self.connections+=1
                        if not a_node in self.unique_matches:
                            self.unique_matches.append(a_node)
                        if not b_node in self.unique_matches:
                            self.unique_matches.append(b_node)
        self.similar_nodes_amount=len(self.unique_matches)
    
