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
- HTML5
- CSS3
- JavaScript
- SQLite

## Project Structure

```text
inventory-sales-management-system/
├── inventory/
├── products/
│   ├── migrations/
│   └── templates/
├── sales/
│   ├── migrations/
│   └── templates/
├── .gitignore
└── manage.py
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

Install any additional Python packages required by the project.

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Source Code

[View Inventory & Sales Management System on GitHub](https://github.com/Pradeep-231/inventory-sales-management-system)

## Project Status

Completed

## Author

Pradeep A

GitHub: [Pradeep-231](https://github.com/Pradeep-231)
