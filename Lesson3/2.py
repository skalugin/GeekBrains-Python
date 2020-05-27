def users_data_print(name, surname, birthday, city, email, phone):
    print(f'User data: {name} {surname} {birthday} {city} {email} {phone}')

prop_list = {'name': '', 'surname': '', 'birthday': '', 'city': '', 'email': '', 'phone': ''}
for i in prop_list.keys():
    prop = input('{}: '.format(i))
    prop_list[i] = prop
users_data_print(name=prop_list['name'], surname=prop_list['surname'], birthday=prop_list['birthday'], city=prop_list['city'],
                 email=prop_list['email'], phone=prop_list['phone'])
