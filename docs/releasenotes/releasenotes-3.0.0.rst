#################################
Cradmin legacy 3.0.0 releasenotes
#################################

************
What is new?
************
 - Updated to Django 3.1


#####
3.1.0
#####
 - Restrict Django to >=3.1 < 3.2 due to breaking changes in Django 3.2
 - Configure pytest
 - Replace model-mommy with model-bakery


3.1.1
#####
- Fix Aria-pressed values
- Upgrade grunt
- Update yarn.lock


#####
3.2.0
#####
- listbuilder-view: Default listbuilder-view now supports either the load more 
 option (as before) or load all. Enabled by overriding method `use_pagination_load_all` and return ``True``.
- translations