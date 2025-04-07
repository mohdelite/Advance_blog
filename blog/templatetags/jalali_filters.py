from django import template
import jdatetime
from datetime import datetime

register = template.Library()

@register.filter
def to_jalali(date):
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%b. %d, %Y, %I:%M %p')  
        except ValueError:
            return '' 

    if date:
        
        jalali_date = jdatetime.datetime.fromgregorian(year=date.year, month=date.month, day=date.day)
        return jalali_date.strftime('%Y/%m/%d')  
    return ''
