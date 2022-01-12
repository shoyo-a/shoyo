import subprocess

def main():
    result = subprocess.run('~/python/GUI/20220108/outputNums/output.exe', shell = True)
    print(result)

if __name__ == '__main__':
    main()