#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os, django
import sys
import logging

def main():
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tendresse.settings')
    # django.setup()

    logging.basicConfig(level=logging.INFO,  # Imposta il livello di gravità minimo per i messaggi di log
                        format='%(asctime)s %(levelname)s: %(message)s',  # Formato del messaggio di log
                        datefmt='%Y-%m-%d %H:%M:%S')
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tendresse.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
