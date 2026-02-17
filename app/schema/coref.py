from pydantic import BaseModel, HttpUrl
from typing import List

class item(BaseModel):
    sent: str | None = None
    label: str | None = None
     

class Article(BaseModel): # the schema for the input request for coreference api. change this according to orchestration method

    content: str | None = None
    url: HttpUrl
    

class Coref_Article(BaseModel): # the schema for the input request for preprocessing api. change this according to orchestration method

    content: str | None = None
    url: HttpUrl
    chains: list | None = None # this will hold the coreference chains in string format. change this according to orchestration method   
    ner_list: list[item] | None = None # this will hold the ner list in string format. change this according to orchestration method
