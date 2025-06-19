from fastapi import FastAPI
import schemas

app = FastAPI()

fakeDatabase = {
    1:{'Task1':'Complete the action'}, 
    2:{'Task2':'Cover the action'}, 
    3:{'Task3':'Update the action'}, 
}
 
@app.get('/')
def getItems():
    return fakeDatabase


@app.get("/{id}")
def idItems(id:int):
    return fakeDatabase[id]

@app.post("/")
def addItem(item:schemas.Item):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {"task": item.task}
    return fakeDatabase

