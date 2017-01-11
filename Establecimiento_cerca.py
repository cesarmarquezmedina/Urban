import pandas as pd
import mysql.connector
import sys, json

cnx = mysql.connector.connect(user='cesarmarquez', password='CESAR_2606952_*cmarquez',
                              host='urban-srv.isavanzados.com.mx',
                              database='Scripts'
                              )
cursor=cnx.cursor()
cursor.execute('Select * from Lugares')
df=cursor.fetchall()
cnx.close()
df=pd.DataFrame(df)
df.columns=['X','Y']

try:
    data=json.loads(sys.argv[1])
except:
    print("Error")
    sys,exit(1)


x=21.903378
y=-102.268070

def distancia(x,x1,y,y1):
    a=(x-x1)**2
    b=(y-y1)**2
    c=((a+b)**.5)*10000
    return c

punto=[]
punto2=[]
for index in range(df.shape[0]):
    dis=distancia(df['X'][index],x,df['Y'][index],y)
    if(dis<30):
        x1=df['X'][index]
        y2=df['Y'][index]
        punto.append(x1)
        punto2.append(y2)

result={'status':'yes!'}
        
print (json.dumps(result))