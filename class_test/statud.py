#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class Stautd(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print "%s : %s" % (self.name,self.score)

    def get_score(self):
        if self.score > 90:
            print "%s : A" % (self.name)
        elif self.score > 70:
            print "%s : B" % (self.name)
        else:
            print "%s : C" % (self.name)


a=Stautd("xiaoming",89)
b=Stautd("xiaohong",70)

a.print_score()
b.print_score()

a.get_score()
b.get_score()