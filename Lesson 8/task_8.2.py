n, m, k, x, y, z, t, a = (
    int(input()), int(input()), int(input()),
    int(input()), int(input()), int(input()),
    int(input()), int(input())
)
first_and_second = n + m - x - t
second_and_third = m + k - y - t
first_and_third = n + k - z - t
first = n - first_and_second - first_and_third - t
second = m - first_and_second - second_and_third - t
third = k - second_and_third - first_and_third - t
one_book = first + second + third
two_books = first_and_second + second_and_third + first_and_third
zero_books = a - one_book - two_books - t
print(one_book, two_books, zero_books, sep='\n')
