from fastapi import FastAPI, HTTPException


app = FastAPI()

information_books = {
    1 : {
        "title" : "Python", 
        "author" : "Joshua Welsh"
        },
    2 : {
        "title" : "C/C++ Prog l : Fund Prog Concepts/C/C++ Prog Ll",
        "author" : "LAD Custom Publishing"
        },
    3 : {
        "title" : "Machine learning",
        "author" : "Ethem Alpaydin"
        },
}

last_book_id = 3


@app.get("/books")
def get_information_books():
    list_name_books = []
    
    for book in information_books.values():
        list_name_books.append(book["title"])
    return list_name_books

@app.post("/books")
def create_book(title_new_book: str, author_new_book: str):
    global last_book_id
    last_book_id += 1
    
    information_books[last_book_id] = {
        "title" : title_new_book,
        "author" : author_new_book,
        }
        
    return {
            "Message" : "The book was successfully registered.",
            "book Information" : information_books[last_book_id],
            }

@app.get("/books/{id_book}")
def get_book(id_book: int):
    try:
        return information_books[id_book]
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
            )
        
    # if id_book in information_books.keys():
    #     return information_books[id_book]
    # raise HTTPException(
    #     status_code=404,
    #     detail="Book not found"
    #     )

@app.patch("/books/{id_book}")
def update_book(id_book: int, title: str=None, author: str=None):
    if id_book in information_books:
        if title is not None:
            information_books[id_book]["title"] = title
        if author is not None:
            information_books[id_book]["author"] = author
            
        return {
            "Message" : "The book was successfully updated.",
            "book Information" : information_books[id_book],
            }
    else:
        raise HTTPException(
            status_code=404,
            detail="Book id not found"
            )

@app.delete("/books/{id_book}")
def delete_book(id_book: int):
    if id_book in information_books:
        information_books.pop(id_book)
        return "The book was successfully deleted."
    else:
        raise HTTPException(
            status_code=404,
            detail="Book id not found"
            )