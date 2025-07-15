#!/usr/bin/env python3
"""
Migration script to create and apply database migrations for model changes.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'colyak_ankara.settings')

# Setup Django
django.setup()

from django.core.management import call_command

def main():
    """Create and apply migrations."""
    print("Creating migrations...")
    call_command('makemigrations', 'users')
    
    print("Applying migrations...")
    call_command('migrate')
    
    print("Migration completed successfully!")

if __name__ == "__main__":
    main()
