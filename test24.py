# coding: utf-8
from state import curr, switch, stateful, State, behavior

def workday():
    print('work hard!')

def weekend():
    print('play harder!')

#class People(object):
#    pass

#people = People()
#while True:
while False:
    for i in xrange(1, 8):
        if i == 6:
            people.day = weekend
        if i == 1:
            people.day = workday
        people.day()
####################################

@stateful
class People(object):
    class Workday(State):
        default = True
        @behavior
        def day(self):
            print('work hard.')

    class Weekend(State):
        @behavior
        def day(self):
            print('play harder!')

people = People()
while True:
    for i in xrange(1, 8):
        if i == 6:
            switch(people, People.Weekend)
        if i == 1:
            switch(people, People.Workday)
        people.day()
