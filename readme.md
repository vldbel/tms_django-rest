## TMS DRF test project #01
### What's insode
single table django model with two endpoints:
* /api/books/ - get returns all books, post creates new book
* /api/books/{book_id}/ get - returns book by its id, put - update book, delete - deletes book
Created with help of AI. I'm not completely understand how it works :)

### Postman tests
Extremely primitive. Just to check how it works.
Feel free to import collection to your postman.

### Notes
django key and database settings aren't in settings.py. You have to add your own.
