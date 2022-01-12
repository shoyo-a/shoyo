import subprocess
from subprocess import PIPE

def main():
    print('start')
    #subprocess.run('~/python/GUI/20220108/outputNums/output.exe', shell = True)
    #subprocess.Popen('~/python/GUI/20220108/outputNums/output.exe', shell = True, stdout=PIPE, stderr=PIPE)
    before_result = ''
    current_result = ''
    print('loop start')
    print('loop start2')
    while(1):
        #print('[START] loop')
        current_result = subprocess.check_output('tail -n 1 ~/python/GUI/20220108/outputNums.log', shell = True, encoding = 'utf-8')
        if before_result != current_result:
            #print(current_result, flush = True, sep = '')
            print(current_result, sep = '')
            before_result = current_result
        #print('[END] loop')

if __name__ == '__main__':
    main()