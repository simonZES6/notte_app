from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
data =[]
# array waar data opgeslagen moet worden
class note_Data:
    def note():
        data = []


class Note(BaseModel):
    note_id :int
    user_id :int
    name :str
    lastname :str
    titel : str
    chapter :str
    paragraph :str

#opslaan van notes
@app.post("/notes")
def read_user(note: Note):
   data.append(note)
   return {"massage":"Notitie toegevoegd"}

#ophalen van notes
@app.get("/notes")
def get_notes(note: Note):
    data.append(note)
    return {"massage":"Notitie opgehaald"}


#updaten van notes
@app.put("/notes")
def update_notes(note: Note):
   data.append(note)
   return{"massage": "Notities bijgewerkt"}


#verwijderen van notes
@app.delete("/notes")
def delete_note(note:Note):
    data.remove(note)
    return{"massage":"notities verwijderd"}








