
# 📖 JakBookShelf – A Modern Bookshop Web App

Welcome to **JakBookShelf**, a clean and elegant Django-powered web app for reviewing and selling books, built with love by [Md Jakaria Rahman](https://github.com/mdjakariarahman). This project blends functionality with simplicity — letting users explore, post, and manage book reviews in an intuitive environment.

---

## 🌟 Key Features

- ✍️ **User friendly bookshp** – Add, read, and manage book sells
- 🔐 **Authentication** – Secure login/logout & registration system
- 📚 **Book Management** – Add new books with title, author, description & image
- 🧾 **Clean UI** – Lightweight, fast-loading frontend with responsive design
- 📦 **Modular Structure** – Follows Django best practices for scalability

---

## 🛠 Tech Stack

| Layer        | Tech                          |
|--------------|-------------------------------|
| **Backend**  | Django (Python)               |
| **Frontend** | HTML5, CSS3, Bootstrap (optional) |
| **Database** | SQLite (default for dev)      |
| **Tools**    | Git, GitHub, VS Code          |

---

## 🚀 Setup Instructions

Get JakBookShelf up and running in minutes:

```bash
# 1. Clone the repo
git clone https://github.com/mdjakariarahman/JakBookShelf.git
cd JakBookShelf

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser (optional but recommended)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
````

---

## 🗂️ Project Structure

```bash
JakBookShelf/
├── bookshelf/           # Main Django project config
│   ├── settings.py
│   └── urls.py
│
├── reviews/             # Core app (book reviews)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       └── reviews/
│           ├── base.html
│           ├── home.html
│           ├── book_list.html
│           ├── add_review.html
│           └── ...
│
├── static/              # CSS, JS, images (optional)
├── media/               # Uploaded book cover images
├── db.sqlite3           # Default dev database
├── requirements.txt     # Python dependencies
└── manage.py
```

---

## 🔑 Default Login Info (for demo/testing)

```txt
Username: admin
Password: admin123
```

You can always create your own superuser using `createsuperuser`.

---

## 📸 Screenshots (Add yours here!)


* 🏠 Home page
![Screenshot 2025-05-18 022946](https://github.com/user-attachments/assets/78960cd8-1629-467c-9fc6-736df1209527)

* 📖 Book listing
![Screenshot 2025-05-18 022959](https://github.com/user-attachments/assets/4ff14f07-c6bd-4686-9cd6-9ffba1d5f1d9)

* 🔐 Login page

![Screenshot 2025-05-18 023044](https://github.com/user-attachments/assets/0f61df2c-be43-415f-b106-a231f845b46c)

* 📚 Book listing
![Screenshot 2025-05-18 023117](https://github.com/user-attachments/assets/4a779a37-4a04-4487-8eed-a309bb64800b)



---

## 💡 Future Improvements (Ideas)

* 🗂️ Category/tag-based filtering
* 🌟 User ratings (1–5 stars)
* 📊 Analytics dashboard for admins
* ✨ Dark mode toggle
* 🌐 REST API integration

---

## 🤝 Contributing

Pull requests are welcome! Whether it's a bug fix, UI improvement, or a cool new feature — open an issue or fork and go wild 💻🛠️

---

## 🪪 License

Licensed under the [MIT License](LICENSE) – free to use, fork, remix, and vibe with.

---

## 👨‍💻 About the Developer

**Md Jakaria Rahman**

> *CSE Student | Python & Django Lover | Passionate about Building Cool Stuff*

🔗 [GitHub](https://github.com/mdjakariarahman)
📧 [jakaria.cseofficial@gmail.com](mailto:jakaria.cseofficial@gmail.com)

---

> *"A reader lives a thousand lives before he dies. The one who never reads lives only one." – George R.R. Martin*

---


