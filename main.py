from fastapi import FastAPI, HTTPException


app = FastAPI()

information_books = [
    {"title" : "python", "id" : 1},
    {"title" : "C++", "id" : 2},
    {"title" : "Java", "id" : 3},
    ]

last_book_id = 3


@app.get("/books")
def get_information_books():
    list_name_books = []
    
    for item in information_books:
        list_name_books.append(item["title"])
    return list_name_books

@app.post("/books")
def create_book(title_new_book:str):
    global last_book_id
    last_book_id += 1
    
    book_dict = {
        "title": title_new_book,
        "id": last_book_id
    }
    information_books.append(book_dict)
        
    return "The book was successfully registered."

@app.get("/books/{id_book}")
def get_book(id_book:int):
    for book in information_books:
        if book["id"] == id_book:
            return book
    raise HTTPException(
        status_code=404,
        detail="Book not found"
        )

@app.patch("/books/{id_book}")
def update_book(id_book:int, title:str):
    for book in information_books:
        if book["id"] == id_book:
            book["title"] = title
            return "Information successfully recorded."
    raise HTTPException(
        status_code=404,
        detail="Book id not found"
        )

@app.delete("/books/{id_book}")
def delete_book(id_book : int):
    for book in information_books:
        if book["id"] == id_book:
            information_books.remove(book)
            return "The book was successfully deleted."
    raise HTTPException(
            status_code=404,
            detail="Book id not found"
            )