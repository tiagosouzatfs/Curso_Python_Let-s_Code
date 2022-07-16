import datetime as dtm

d = dtm.date(2001, 9, 11) #definir uma data
tday = dtm.date.today() #pegar dia de hoje
print(tday, d)

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = dtm.timedelta(hours=12)
print(tday + tdelta)

bday = dtm.date(2016, 9, 24)
till_bday = bday - tday
print(till_bday.days)

#datetime para string -> strftime
dt_agora = dtm.datetime.now()
print(dt_agora, type(dt_agora))
print(dt_agora.strftime('%B %d, %Y'))
print(dt_agora.strftime('%m %d, %Y'))

# strptime - String para Datetime
dt_str = 'july 24, 2016'
dt = dtm.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

print(dtm.time(12, 6, 21,7), 'Hora:minuto:segundo.microssegundo')
print('------------------------------')

print(dtm.date(2022, 7, 16), 'Ano-mês-dia')
print('------------------------------')

print(dtm.datetime(2022, 7, 16, 12, 6, 21,7), 'Ano-mês-dia Hora:minuto:segundo.microssegundo')
print('------------------------------')

natal = dtm.date(2020, 12, 25)
reveillon = dtm.date(2021, 1, 1)

print((reveillon - natal))
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)