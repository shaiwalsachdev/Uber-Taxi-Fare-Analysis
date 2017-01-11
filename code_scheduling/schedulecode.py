import schedule
import time
import os

def job0():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 0 111017'
	print command
	os.system(command)
def job1():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 1 70501'
	print command
	os.system(command)
def job2():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 2 45511'
	print command
	os.system(command)
def job3():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 3 27523'
	print command
	os.system(command)
def job4():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 4 15114'
	print command
	os.system(command)
def job5():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 5 18191'
	print command
	os.system(command)
def job7():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 7 136975'
	print command
	os.system(command)

def job8():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 8 196937'
	print command
	os.system(command)
def job9():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 9 213353'
	print command
	os.system(command)
def job11():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 11 220072'
	print command
	os.system(command)
def job12():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 12 234978'
	print command
	os.system(command)
def job13():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 13 226303'
	print command
	os.system(command)
def job14():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 14 231942'
	print command
	os.system(command)
def job15():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 15 215067'
	print command
	os.system(command)
def job17():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 17 215671'
	print command
	os.system(command)
def job18():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 18 283415'
	print command
	os.system(command)
def job19():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 19 293108'
	print command
	os.system(command)
def job21():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 21 225225'
	print command
	os.system(command)
def job22():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 22 200629'
	print command
	os.system(command)
def job23():
	command = 'source activate geekdon && python /home/bt2/14CS10061/shaiwal/Uber/ByTimezone/code/bulkrunnignScript_any.py 23 160705'
	print command
	os.system(command)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().friday.at("15:00").do(job6)
#schedule.every().friday.at("19:00").do(job10)
#schedule.every().saturday.at("1:00").do(job16)

schedule.every().saturday.at("09:00").do(job0)
schedule.every().saturday.at("10:00").do(job1)
schedule.every().saturday.at("11:00").do(job2)
schedule.every().saturday.at("12:00").do(job3)
schedule.every().saturday.at("13:00").do(job4)
schedule.every().saturday.at("14:00").do(job5)
schedule.every().saturday.at("16:00").do(job7)
schedule.every().saturday.at("17:00").do(job8)
schedule.every().saturday.at("18:00").do(job9)
schedule.every().saturday.at("20:00").do(job11)
schedule.every().saturday.at("21:00").do(job12)
schedule.every().saturday.at("22:00").do(job13)
schedule.every().saturday.at("23:00").do(job14)
schedule.every().saturday.at("23:59").do(job15)
schedule.every().saturday.at("02:00").do(job17)
schedule.every().saturday.at("03:00").do(job18)
schedule.every().saturday.at("04:00").do(job19)
schedule.every().saturday.at("06:00").do(job21)
schedule.every().saturday.at("07:00").do(job22)
schedule.every().saturday.at("08:00").do(job23)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)




while True:
    schedule.run_pending()
    time.sleep(1)