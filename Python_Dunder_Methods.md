# Attribute Access
These methods control how attributes are accessed, set, and deleted on objects.
### `__getattr__(self, name)`:
__Description:__ Called when an attribute name is not found in the usual places (instance dictionary, class, parent classes). Useful for dynamic attribute generation or handling misspelled attributes.

__Raises:__ AttributeError if the attribute cannot be handled.
### `__setattr__(self, name, value)`:
__Description:__ Called whenever an attribute is assigned (e.g., obj.name = value). This method is called unconditionally for all attribute assignments. Careful implementation is crucial to avoid infinite recursion (e.g., directly assigning self.name = value inside `__setattr__`).

__Common Usage:__ Use`object.__setattr__(self, name, value)` to set attributes without triggering `__setattr__` recursively.
### `__delattr__(self, name`):
__Description:__ Called when an attribute is deleted (e.g., del obj.name).

__Common Usage:__ Use `object.__delattr__(self, name)` to delete attributes without triggering `__delattr__` recursively.
### `__getattribute__(self, name)`:
__Description:__ Called unconditionally for all attribute accesses (e.g., obj.name). This is even before looking up the attribute in the instance's dictionary. Overriding this can be tricky and lead to infinite recursion if not handled carefully.

__Common Usage:__ Use `object.__getattribute__(self, name)` to get attributes without triggering `__getattribute__` recursively.

__Note:__ If `__getattribute__` is implemented, `__getattr__` will only be called if `__getattribute__` explicitly raises an AttributeError.
### `__dir__(self)`:
__Description:__ Called by dir() on an object to return a list of valid attributes for that object.

__Returns:__ A list of strings.
