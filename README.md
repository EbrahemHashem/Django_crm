# Django CRM

This is a basic **Customer Relationship Management (CRM)** project built with Django.

## 📁 Project Structure

- `dcrm/`: Contains the core Django application, including views, models, and settings.
- `virt/`: Your virtual environment (not included in Git).
- `.gitignore`: Includes ignored files such as the virtual environment and sensitive configuration.

## 🔐 Sensitive Files

> `dcrm/settings.py` has been excluded from version control for security reasons.  

To run this project locally, you'll need to create your own `settings.py` file inside the `dcrm/` folder.

You can do this by copying a template:

```bash
cp dcrm/settings_example.py dcrm/settings.py


🚀 Getting Started
1.Install dependencies:
pip install -r requirements.txt

2.Apply migrations:
python manage.py migrate

3.Run the server:
python manage.py runserver