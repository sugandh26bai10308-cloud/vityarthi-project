# Library Book Management System

# Store books in a dictionary
# title -> author, available copies, total copies
books = {}


def add_book(title, author, copies):
    """Add a new book or increase copies of an existing book."""

    if copies <= 0:
        return "Number of copies must be greater than 0."

    if title in books:
        books[title]["available"] += copies
        books[title]["total"] += copies
    else:
        books[title] = {
            "author": author,
            "available": copies,
            "total": copies
        }

    return "Book added successfully."


def borrow_book(title):
    """Borrow a book if a copy is available."""

    if title in books and books[title]["available"] > 0:
        books[title]["available"] -= 1
        return "Book borrowed successfully."

    return "Book not available."


def return_book(title):
    """Return a previously borrowed book."""

    if title not in books:
        return "Book not found."

    if books[title]["available"] < books[title]["total"]:
        books[title]["available"] += 1
        return "Book returned successfully."

    return "All copies of this book are already in the library."


def list_books():
    """Return a list of all books."""

    if not books:
        return ["No books available in the library."]

    result = []

    for title, info in books.items():
        result.append(
            f"{title} | {info['author']} | "
            f"Available: {info['available']} | "
            f"Total: {info['total']}"
        )

    return result


def main():
    """Main program."""

    print("======================================")
    print("   Library Book Management System")
    print("======================================")

    while True:
        cmd = input(
            "\nCommand (add / borrow / return / list / quit): "
        ).strip().lower()

        if cmd == "add":
            title = input("Enter title: ").strip()
            author = input("Enter author: ").strip()

            try:
                copies = int(input("Enter number of copies: "))
            except ValueError:
                print("Invalid number!")
                continue

            print(add_book(title, author, copies))

        elif cmd == "borrow":
            title = input("Enter title: ").strip()
            print(borrow_book(title))

        elif cmd == "return":
            title = input("Enter title: ").strip()
            print(return_book(title))

        elif cmd == "list":
            print("\nBooks in Library:")
            for book in list_books():
                print(book)

        elif cmd == "quit":
            print("Exiting system.")
            break

        else:
            print("Invalid command! Please try again.")


# Start the program
if __name__ == "__main__":
    main()
