import schedule
import time
import os

def job0():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 0 111017 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch0.log &'
	print command
	os.system(command)
def job1():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 1 70501 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch1.log &'
	print command
	os.system(command)
def job2():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 2 45511 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch2.log &'
	print command
	os.system(command)
def job3():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 3 27523 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch3.log &'
	print command
	os.system(command)
def job4():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 4 15114 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch4.log'
	print command
	os.system(command)
def job5():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 5 18191 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch5.log'
	print command
	os.system(command)
def job7():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 7 136975 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch7.log'
	print command
	os.system(command)

def job8():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 8 196937 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch8.log'
	print command
	os.system(command)
def job9():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 9 213353 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch9.log'
	print command
	os.system(command)
def job11():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 11 220072 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch11.log'
	print command
	os.system(command)
def job12():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 12 234978 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch12.log'
	print command
	os.system(command)
def job13():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 13 226303 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch13.log'
	print command
	os.system(command)
def job14():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 14 231942 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch14.log'
	print command
	os.system(command)
def job15():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 15 215067 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch15.log'
	print command
	os.system(command)
def job17():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 17 215671 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch17.log'
	print command
	os.system(command)
def job18():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 18 283415 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch18.log'
	print command
	os.system(command)
def job19():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 19 293108 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch19.log'
	print command
	os.system(command)
def job21():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 21 225225 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch21.log'
	print command
	os.system(command)
def job22():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 22 200629 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch22.log'
	print command
	os.system(command)
def job23():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/mergejson_any.py 23 160705 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/mergelog/sch23.log'
	print command
	os.system(command)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().friday.at("15:00").do(job6)
#schedule.every().friday.at("19:00").do(job10)
#schedule.every().sunday.at("1:00").do(job16)


job0()
job1()
job2()
job3()
job4()
job5()

job7()
job8()
job9()

job11()
job12()
job13()
job14()
job15()

job17()
job18()
job19()

job21()
job22()
job23()


#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)




while True:
    schedule.run_pending()
    time.sleep(1)