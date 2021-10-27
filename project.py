import requests

API_END_POINT = 'https://mach-eight.uc.r.appspot.com/'


""" Sort the data """
def sort_data(data: list) -> list:
    return sorted(data, key=lambda x: int(x['h_in']))



""" Get the data from the API """
def get_data() -> list:
    qury = requests.get(API_END_POINT)

    if qury.status_code == 200:
        return sort_data(qury.json()['values'])
    else:
        return []



""" Search index of data matchin the height """
def search(data: list, height: int) -> int:
    first = 0
    last = len(data)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if int(data[mid]['h_in']) == height:
            index = mid
        else:
            if height < int(data[mid]['h_in']):
                last = mid -1
            else:
                first = mid +1
    return index



if __name__ == '__main__':
    height = -1
    data = get_data()
    print('\n')
    
    while height != 0:
        try:
            height = int(input('Enter the height: '))
            print('\n')
        except ValueError:
            print('Invalid height\n')
            continue

        index = search(data, height)

        if index != -1:
            indexb = index -1
            if (indexb < 0):
                while int(data[indexb]['h_in']) == height:
                    print(f"- {data[indexb]['first_name']} {data[indexb]['last_name']}")
                    indexb -= 1
                    if (indexb < 0):
                        break

            print(f"- {data[index]['first_name']} {data[index]['last_name']}")

            indexa = index + 1
            if (indexa < len(data)-1):
                while int(data[indexa]['h_in']) == height:
                    print(f"- {data[indexa]['first_name']} {data[indexa]['last_name']}")
                    indexa += 1
                    if (indexa > len(data)-1):
                        break

            print('\n')

        elif height != 0:
            print('height not found\n')

    print('Bye...')
