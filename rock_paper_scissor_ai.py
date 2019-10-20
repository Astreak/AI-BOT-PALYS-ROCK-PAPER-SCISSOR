import numpy as np
import pandas as pd
import tensorflow as tf
from tkinter import *
data=np.loadtxt("r.txt",delimiter=",").astype("float64").reshape(-1,1)
inp=np.array([[100, 300],
[300, 200],
[200, 300],
[100, 300],
[100, 100],
[100, 100],
[100, 100],
[200, 200],
[300, 100],
[200, 200],
[100, 100],
[200, 300],
[300, 300],
[200, 100],
[200, 200],
[100, 100],
[300, 200],
[200, 200]]
)
data=pd.DataFrame(data)
ds=pd.DataFrame(inp)
ds=pd.concat([ds,data],axis="columns")
X=ds.iloc[:,[0,1]].values
y=ds.iloc[:,-1].values.reshape(-1,1)
X=tf.keras.utils.normalize(X)



model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128,activation="relu",input_dim=2))
model.add(tf.keras.layers.Dense(34,activation="relu"))
model.add(tf.keras.layers.Dense(3,activation="sigmoid"))
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
model.fit(X,y,epochs=390)

import random
import os

ok=["Rock","scissor","Paper"]
binary=[]
point_val={"Rock":100 ,"scissor":300 ,"Paper":200}
y=[]
pts={"HUMAN":0,"COMPUTER":0}
win=Tk()

win.geometry("600x600")
win.title("STONE PAPER SCISSORS")

def rock():
    while(1):

        s=random.choice(ok)
        
        v=[point_val["Rock"],point_val[s]]
        y.append(v)
        pred=model.predict(tf.keras.utils.normalize(np.array(v)))
        if not max(pred[0])!= pred[0][0]:
            continue
        else:
            print("Rock",s)
            if s=="scissor":
                pts["HUMAN"]+=1
            elif s=="Paper":
                pts["COMPUTER"]+=1
        break
    return pts

def scissor():
    while(1):
        
        s=random.choice(ok)
       
        v=[point_val["scissor"],point_val[s]]
        y.append(v)
        pred=model.predict(tf.keras.utils.normalize(np.array(v)))
        if not max(pred[0])!= pred[0][0]:
            
            continue
        else:
            print("scissor",s)
            if s=="Rock":
                pts["COMPUTER"]+=1
            elif s=="Paper":
                pts["HUMAN"]+=1
            break
    return pts
def Paper():
    while(1):

        s=random.choice(ok)
       
        v=[point_val["Paper"],point_val[s]]
        y.append(v)
        pred=model.predict(tf.keras.utils.normalize(np.array(v)))
        if not max(pred[0])!= pred[0][0]:
            continue
            
            
            
        else:
            print("paper",s)
            if s=="scissor":
                pts["COMPUTER"]+=1
            elif s=="Rock":
                pts["HUMAN"]+=1
        break
    return pts
Label=Label(win,text="HERE GOES THE GAME",fg="Blue")
Label.pack()
stone=Button(win,text="STONE",command=rock,fg="Green")
stone.pack()
paper=Button(win,text="Paper",command=Paper,fg="red")
paper.pack()
scissor=Button(win,text="Scissor",command=scissor,fg="black")
scissor.pack()
win.mainloop()

print(pts)
l=[]
fr={"MATCH_DRAWN":0,"COMPUTER_WINS":2,"HUMAN_WINS":1}
another={"COMPUTER_WINS":2,"HUMAN_WINS":0,"MATCH_DRAWN":1}
for i in pts:
    l.append(pts.get(i,"!"))
if l[0]==l[1]:
    k="MATCH_DRAWN"

    print(k)

elif pts["COMPUTER"]==max(l):
    k="COMPUTER_WINS"
    print(k)
elif pts["HUMAN"]==max(l):
    k="HUMAN_WINS"
    print(k)

    
        
        





