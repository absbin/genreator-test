class Time:
	def __init__(self, year,month):
		self.year = year
		self._month = month
		self.__day=1

class TimeSubclass(Time):
	def __init__(self, century,year,month):
		super().__init__(year,month)
		self.year = 2021
		self.__day=1
		self.century=century

def main():
	time=Time(2021,7)
	time._month=1
	print('time._month',time._month)
	print('time.year',time.year)
	time._Time__day=100
	print('time._Time__day',time._Time__day)
	
	print('*************')

	time_subclass=TimeSubclass(20,2022,12)
	print('time_subclass._TimeSubclass__day',time_subclass._TimeSubclass__day)
	print('time_subclass._Time__day',time_subclass._Time__day)

if __name__ == '__main__':
	main()


		