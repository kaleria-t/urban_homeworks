import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for i in file:
            if i:
                new_str = file.readline()
                all_data.append(new_str)

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start_time = time.time()
# for i in filenames:
#     read_info(i)
# finish_time = time.time()
# print('Время:', (finish_time-start_time)*1000) # 6350.966215133667

if __name__ == '__main__':
    start_time2 = time.time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    finish_time2 = time.time()
    print('Время:', (finish_time2-start_time2)*1000) # 11423.058986663818
# многопроцессный в 2 раза дольше, чего не должно быть