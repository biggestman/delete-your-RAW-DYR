import glob
import os



jpglist=[]
raflist=[]
diff=[]

path=r'F:\photo\2020.4.5 anan\DCIM'
cate = [path + '/' + x for x in os.listdir(path) if os.path.isdir(path+'/'+x)]
for i, folder in enumerate(cate):
    jpglist = glob.glob(folder+'/*.jpg')
    jpglist = [x[-8:-4] for x in jpglist]
    print(jpglist)
    raflist = glob.glob(folder+'/*.RAF')
    raflist = [x[-8:-4] for x in raflist]
    print(raflist)
    diff = [x for x in raflist if x not in jpglist]
    print(diff)
    for x in diff:
        os.remove(folder+f'\DSCF{x}.RAF')
