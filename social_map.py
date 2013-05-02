#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  social_map.py
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
from grapher import *
import random,profile,time
def network(g,node_limit=100):
    name_list=[]
    sports=["soccer","baseball","football","skateboarding","surfing",
            "longboarding","swimming"]
    grades=[x for x in xrange(1,12)]
    age_grade_assoc={1:[5,6],
                     2:[6,7],
                     3:[7,8],
                     4:[8,9],
                     5:[9,10],
                     6:[10,11],
                     7:[11,12],
                     8:[12,13],
                     9:[13,14],
                     10:[14,15],
                     11:[15,16],
                     12:[16,17]}
    countries=["US","Russia","Cuba","Iran","Algeria"]
    t=[0 for x in range(3)]
    print "Populating name list with [x,x,x], total names: 24^3..."
    for x in xrange(97,123):
        t[0]=chr(x)
        for y in xrange(97,123):
            t[1]=chr(y)
            for z in xrange(97,123):
                t[2]=chr(z)
                name_list.append("".join(t))
    print "Names generated:",str(len(name_list))
    print "Deallocating temp buffer..."
    t=[]
    print "Generating nodes..."
    for x in xrange(0,1000):
        node=g.new_node(sport=random.choice(sports),
                        grade=random.choice(grades),
                        name=random.choice(name_list))
        name_list.remove(node.attrs['name'])
        node.attrs['age']=random.choice(age_grade_assoc[node.attrs['grade']])
    print "Deallocating unused names..."
    name_list=[]
def simulate_outbreak(g,*args,**kwargs):
    g.clear_nodes_connections()
    print "Connecting nodes..."
    eval('g.strict_connect_nodes_by(%s)'% ",".join("%s=%s"%(k,v) for (k,v) in kwargs.items()))
    print "Infecting %s nodes..." % str(len(g.unique_matches))
    for node in g.unique_matches:
        node.attrs["infected"]=True
def main():
    graph=Graph()
    network(graph)
    simulate_outbreak(graph,grade=8)
    for x in graph.unique_matches:
        print x.attrs
    print graph.connections
    graph.remove_all_nodes()
    raw_input("...")
    return 0

if __name__ == '__main__':
	#profile.run('main()')
    main()
    #time.sleep(1)

