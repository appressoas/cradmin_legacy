Cradmin legacy 4 releasenotes
=============================


4.0.0
=====

## What is new

Updated to Django 3.2.x.

Django 3.2 is an LTS version and is expected to receive security updates for at least the next three years from it's initial 
launch (6. April 2024).

- Requires Django 3.2.x
- Requires ievv-opensource 8.x+
- Requires django-cradmin 9.x+
- Requires python 3.8+


## Migrating to cradmin_legacy 4.0

- Update your own application for Django 3.2. If you're coming from Django 1.11.x, there are plenty of changes through Django 2 and 3 
  that needs to be addressed (you can migrate directly to Django 3 without going through Django 2 first).
- Check out the documentation for cradmin_legacy 3.x (this is the initial Django 3 release) if you're updating from Django 1 or 2.
- Update to cradmin_legacy 4.x.

## 4.0 patch releases

### 4.0.1
- Datetimepicker: Support setting hours and minutes for default "now"-date. The default datetime is the current datetime, but this 
  allows for static hours and minutes if needed.


4.1.0
=====

## What is new?
- standalone-base-internal.django.html: Add block for overriding HTML-lang.


## 4.1 patch releases

### 4.1.1
- Ace-editor: Removed keyboard-trap + accessibility improvements.

### 4.1.2
- Javascript: Add missing build-files.