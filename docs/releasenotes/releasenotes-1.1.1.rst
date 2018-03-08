#################################
Django cradmin 1.1.1 releasenotes
#################################


************
What is new?
************
``cradmin_legacy.viewhelpers`` can now be imported with ``from cradmin_legacy import viewhelpers``.
Example::

    from cradmin_legacy import viewhelpers

    class MyCreateView(viewhelpers.create.CreateView):
        pass  # more code here ...

The imported ``viewhelpers`` object does not include ``listbuilder``, ``listfilter`` or ``multiselect2``,
they should still be imported using ``from cradmin_legacy.viewhelpers import <module>``.


****************
Breaking changes
****************
There are no breaking changes between 1.1.0 and 1.1.1.
