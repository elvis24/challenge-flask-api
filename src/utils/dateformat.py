import datetime

class DateFormat():
    
    @classmethod
    def convert_date(selfd,date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')