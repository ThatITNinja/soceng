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
import random,profile
def network(g,node_limit=100):
    country=["america","spain","russia","germany","italy"]
    age=[x for x in xrange(15,80)]
    grade=[x for x in xrange(1,13)]
    sports=["soccer","football","basketball","skateboarding","surfing"]
    for person in range(node_limit):
        x=g.new_node(country=random.choice(country),age=random.choice(age),
                   grade=random.choice(grade),sports=random.choice(sports))
        #print x.attrs
def main():
    graph=Graph()
    network(graph)
    graph.strict_connect_nodes_by(country="italy",sports="surfing")
    graph.loose_connect_nodes_by(age=55)
    for x in graph.unique_matches:
        print x.attrs
    print graph.connections
    return 0

if __name__ == '__main__':
	profile.run('main()')

