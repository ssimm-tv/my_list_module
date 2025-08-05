An odoo module that demonstrates how to get json data from a controller and insert it 
into a template.  

This uses the old Ajax RPC method, which is good enough for relatively simple sites.

It is compatible with Odoo v18 (odoo libraries have been moved around)

Put this module in a directory called my_list_module (this name is hard-coded in the source code.)

Launch it like this:
py odoo-bin [database-coordinates] --addons-path="addons,{where-your-modules-are}" -u my_list_module --dev xml &

http://localhost:8069/my_main_page

You should see content like this:
....
Dynamic List (AJAX)
Asynchronous Item A (ID: 1)
Asynchronous Item B (ID: 2)
Asynchronous Item C (ID: 3)
Asynchronous Item D (ID: 4)
...
