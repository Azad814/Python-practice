def process_file():
    try:
        f = open('D:\data science practice\python\hook.txt')
        x=1/0

    except UnboundLocalError as e:
        print('inside except')
    finally:
        print('cleaning up file')
        f.close()

process_file()