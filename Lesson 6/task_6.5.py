# Дополните приведенный код, используя срезы, чтобы он вывел все элементы кортежа countries, кроме двух последних и трех первых.

countries = ('Russia', 'Argentina', 'Slovakia', 'Canada',
             'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
strip_left = 3
strip_right = 2

print(countries[strip_left:len(countries) - strip_right])
