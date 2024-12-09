
# Django Invoice and Payslip Generator

This project is a Django-based web application that allows users to generate **Invoices** and **Payslips** dynamically. Users can fill out forms to create these documents and export them as PDF files.

## Features
- **Invoice Generator**: Fill out a form to create detailed invoices.
- **Payslip Generator**: Dynamically generate employee payslips based on input data.
- **PDF Export**: Download invoices and payslips as PDF files for easy sharing and printing.
- **User-Friendly Interface**: Simple forms and styled outputs for professional-looking documents.

---

## Prerequisites

Ensure you have the following installed on your system:
- **Python 3.8+**
- **pip** (Python package manager)
- **Virtualenv** (optional but recommended)
- **WeasyPrint** (PDF rendering engine)

---

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

**`requirements.txt`** should contain:
```plaintext
Django==3.2.20
WeasyPrint==57.2
```

### 4. Configure the Database
By default, the project uses SQLite. You can configure your preferred database in the `DATABASES` section of `settings.py`.

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Usage

### Generating Invoices
1. Go to `/generate-invoice/` in your browser.
2. Fill out the form with invoice details (e.g., recipient name, description, amount, dates).
3. Click **Generate Invoice**.
4. View or download the generated PDF invoice.

### Generating Payslips
1. Navigate to `/generate-payslip/`.
2. Provide employee information, salary details, and payment period.
3. Click **Generate Payslip**.
4. Download the PDF payslip.

---

## Folder Structure
```plaintext
project-directory/
├── templates/
│   ├── generate_invoice.html  # Form for invoice creation
│   ├── generate_payslip.html  # Form for payslip creation
│   ├── invoice_template.html  # Invoice PDF template
│   ├── payslip_template.html  # Payslip PDF template
├── invoices/  # App for invoice generation
├── payslips/  # App for payslip generation
├── manage.py
├── requirements.txt
├── settings.py
```

---

## Exporting PDFs

The application uses **WeasyPrint** for rendering HTML templates as PDFs. Ensure you install the required dependencies for WeasyPrint to work correctly:
- **Linux**: Install `libpango` and `libcairo`.
- **Windows**: WeasyPrint works out-of-the-box.

---

## Deployment

For production deployment:
1. Set `DEBUG = False` in `settings.py`.
2. Use a production-grade WSGI server like Gunicorn or uWSGI.
3. Configure static files using `collectstatic`:
   ```bash
   python manage.py collectstatic
   ```

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Feel free to submit issues and pull requests for improvements or new features.

---

## Contact
For questions or feedback, please reach out to **[Your Name]** at **your-email@example.com**.
