from projects.divable.divisible import Divisible

number_list = [10, 20, 33, 46, 55]
print("Given list:", number_list)
print('Divisible by 5:')
for number in number_list:
    if Divisible.is_divisible_by(number, 5):
        print(number)
