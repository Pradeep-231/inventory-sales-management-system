# Inventory & Sales Management System

## Project Overview

The Inventory & Sales Management System is a web application developed using Python and Django to manage products, track inventory levels, record sales, and analyze sales performance. It helps simplify inventory management and supports better stock control decisions.

## Features

- Product management
- Inventory and stock quantity tracking
- Sales recording and history
- Sales dashboard
- Sales analysis and reporting
- Low-stock monitoring
- Stock prediction and reorder recommendations

## Technologies Used

- Python
- Django
- MySQL
- HTML5
- CSS3
- JavaScript
- Bootstrap

## Project Structure

```text
inventory-sales-management-system/
├── inventory/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── migrations/
│   └── templates/
├── sales/
│   ├── migrations/
│   ├── static/
│   └── templates/
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Pradeep-231/inventory-sales-management-system.git
cd inventory-sales-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv server
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\server\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure MySQL Database

1. Install and start MySQL Server.
2. Open MySQL Workbench.
3. Create the project database:

```sql
CREATE DATABASE inventory_management;
```

4. Copy `.env.example` to `.env` in the project root.

5. Open `.env` and configure the following variables with your local MySQL credentials:

   - `DJANGO_SECRET_KEY`
   - `DB_NAME`
   - `DB_USER`
   - `DB_PASSWORD`
   - `DB_HOST`
   - `DB_PORT`

6. Save the `.env` file. Never upload `.env` or expose your actual credentials on GitHub.


### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Admin Account (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Source Code

[View Inventory & Sales Management System on GitHub](https://github.com/Pradeep-231/inventory-sales-management-system)

## Project Status

Completed

## Author

Pradeep A

GitHub: [Pradeep-231](https://github.com/Pradeep-231)