'''
f=open('sample_file.txt','r')
if f:
    print('file successfully opened..')


f=open('sample_file.txt',mode='w')
if f:
    print('file successfully opened...')

'''

#  Other Arguments for opening
# f=open('sample_file.txt', 'r', 10, 'utf-8')
f = open('sample_file.txt', mode='r', buffering=10, encoding='utf-8')

if f:
    print('Opened')

print(f)
f.close()
