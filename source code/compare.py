import os
import filecmp

correct = os.listdir('labels')
cout = 0
for file in correct:
    with open('labels/' + file) as f_1:
        dic_1 = {}
        content_1 = f_1.readlines()
        for line in content_1[1:-1]:           
            dic_1[line[8:13]] = int(line[18:-1])
        with open('model_x_2_3/labels/' + file) as f_2:
            dic_2 = {}
            content_2 = f_2.readlines()
            for line in content_2[1:-1]:
                try:
                    dic_2[line[8:13]] = int(line[18:-1])
                except ValueError:
                    print(f'{file}')
            if dic_1 != dic_2:
                cout += 1
                print(f'file {file} is not even') 
print(f'{cout} files are different in total')
    # break
        


