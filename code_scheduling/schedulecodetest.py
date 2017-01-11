import schedule
import time
import os

def job6():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/external_test.py 10 1 6 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/testing1/sch6.log &'
	print command
	os.system(command)
def job10():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/external_test.py 11 1 10 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/testing1/sch10.log &'
	print command
	os.system(command)
def job16():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/external_test.py 12 1 16 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/testing1/sch16.log &'
	print command
	os.system(command)
def job20():
	command = 'nohup time python -u /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/external_test.py 13 1 20 > /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/testing1/sch20.log &'
	print command
	os.system(command)

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().friday.at("15:00").do(job6)
#schedule.every().friday.at("19:00").do(job10)
#schedule.every().sunday.at("1:00").do(job16)


#schedule.every().wednesday.at("15:20").do(job6)
#schedule.every().wednesday.at("19:20").do(job10)
#schedule.every().wednesday.at("01:20").do(job16)
schedule.every().wednesday.at("05:20").do(job20)

#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)




while True:
    schedule.run_pending()
    time.sleep(1)