import logging

logging.basicConfig(level=logging.INFO, filename="log.log",filemode="a",
                    encoding='utf-8', format="%(asctime)s %(levelname)s %(message)s")

date_to_prove = input('Введите дату: ')

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    try:
        date, month, year = (int(item) for item in full_date.split('.'))
    except ValueError as error:
        logging.error(f'Дата введена некорректно. {error}')
        return error
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        logging.info(f'Такой даты не существует. {full_date}')
        return False
    if month in (4, 6, 9, 11) and date > 30:
        logging.info(f'В указанном месяце меньше 31 дня. {full_date}')
        return False
    if month == 2 and is_leap(year) and date > 29:
        logging.info(f'Год високосный, но в месяце 29 дней. {full_date}')
        return False
    if month == 2 and not is_leap(year) and date > 28:
        logging.info(f'Год не високосный. {full_date}')
        return False
    logging.info(f'Введенная дата корректна и существует. {full_date}')
    return True

if not valid:
    print(valid(date_to_prove))
else:
    print(valid(date_to_prove))
