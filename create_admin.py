#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_system.settings')

# Setup Django
django.setup()

from django.contrib.auth.models import User
from django.core.management import execute_from_command_line

def create_admin_user():
    try:
        # Check if admin user already exists
        if User.objects.filter(username='admin').exists():
            print("Admin user already exists!")
            return
        
        # Create admin user
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123'
        )
        print(f"Admin user created successfully!")
        print(f"Username: {admin_user.username}")
        print(f"Email: {admin_user.email}")
        print(f"Password: admin123")
        print("\nYou can now log in to Django admin with these credentials.")
        
    except Exception as e:
        print(f"Error creating admin user: {e}")

if __name__ == '__main__':
    create_admin_user() 