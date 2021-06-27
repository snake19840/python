import os
from posixpath import join
import pandas as pd


df = None
filePath = r'D:\桌面\新建文件夹 (2)'
localpath=os.getcwd()
localfile=os.path.join(localpath,'test.xlsx')
for basepath, subfiles, allfiles in os.walk(filePath):
    allfiles = allfiles
    basepath = basepath
    break
for filename in allfiles:
    fullFileName = os.path.join(basepath, filename)
    df_new = pd.read_excel(fullFileName)
    print(df)
    if  df is None:
        df=df_new
        continue
    else:
        df=pd.concat([df,df_new])

df.to_excel(localfile,index=False)

