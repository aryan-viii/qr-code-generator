QR Code Generator

This is a Django web application that generates QR codes from user input and allows users to download them.
The project uses pure HTML and CSS for the frontend (no Bootstrap or frontend frameworks) and Django for the backend.

The application works by taking user input (URL), generating a QR code image on the server,
saving it inside the media directory, and displaying it on a result page where the user can download it.

--------------------------------------------------

FEATURES

- Generate QR codes from URLs
- Download generated QR codes as image files
- Clean and professional user interface
- Django form handling
- Media file handling for generated QR images
- Beginner-friendly Django project structure

--------------------------------------------------

TECH STACK

- Python
- Django
- HTML5
- CSS3
- SQLite (default Django database)

--------------------------------------------------

SETUP INSTRUCTIONS

1. Clone the repository

```bash
git clone https://github.com/aryan-viii/qr-code-generator.git
cd qr-code-generator
   ```

2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install django qrcode pillow
```

4. Apply database migrations

```bash
python manage.py migrate
```

5. Start the development server

```bash
python manage.py runserver
```

6. Open the application in your browser

```bash
http://127.0.0.1:8000/
```

--------------------------------------------------

HOW THE APPLICATION WORKS

1. The user enters name and a URL on the home page
2. The Django form sends data to the backend
3. A QR code image is generated using Python
4. The image is saved inside the /media directory
5. The result page displays the QR code
6. The user can download the QR image

--------------------------------------------------

NOTES

- Virtual environments (venv, .venv) are excluded using .gitignore
- The SQLite database file is for development only
- Media files are stored locally
- This project is ideal for learning Django fundamentals

--------------------------------------------------

FUTURE IMPROVEMENTS

- QR size and color customization
- SVG QR code downloads
- Dark mode interface
- Online deployment

--------------------------------------------------

LICENSE

This project is created for learning and educational purposes.

