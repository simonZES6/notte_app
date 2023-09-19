from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data =[]
Category_data=[]
# array waar data opgeslagen moet worden

class Items(BaseModel):
    category_id:int
    name: str
    description: str
class Category(Items):
    Category_id: int
    name:str
    description:str
    date:str

class Note(Items):
    note_id :int
    user_id :int
    name  :str
    lastname :str
    titel : str
    chapter :str
    paragraph:str
    category_id: int


#opslaan van notes
@app.post("/notes/category")
def read_user(note: Note,category:Category):
   data.append(note,category)
   return {"massage":"Notitie toegevoegd"}

#ophalen van notes
@app.get("/notes/category")
def get_notes(note: Note,category:Category):
    return data
 
#ophalen van category
@app.get("/category")
def get_category(category:Category):
    return data 



#updaten van notes
note = []
@app.put("/notes")
def update_notes(note: Note):
    for note in note:
        if  note.note_id ==note.note_id:
            note.note_id= "0"
            note.user_id= note.user_id
            note.name = note.name
            note.lastname = note.lastname
            note.titel= note.titel
            note.chapter= note.chapter
            note.paragraph=note.paragraph
            
        return{"massage": "Notities bijgewerkt"} 


#verwijderen van notes

@app.delete("/notes")
def delete_note(note:Note):
    for request_data in note:
        if note.note_id == note.note_id:
           data.remove(note)

  


class GoldenRetriver(Dog):
    def speak(self, sound="bark"):
        return super().speak(sound)





