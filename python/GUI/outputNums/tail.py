import subprocess

def main():
    current = ''
    before = ''
    while(1):
        #current = subprocess.run('tail -n 1 ./outputNums.log', shell = True)
        current = subprocess.check_output('tail -n 1 ./outputNums.log', shell = True, encoding = 'utf-8')
        if before != current:
            print(current)
            before = current
            current = ''

if __name__ == '__main__':
    main()