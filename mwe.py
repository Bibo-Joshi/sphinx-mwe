class Parent:
    """
    The parent class.
    """

    class _Hidden:
        hidden_attr = 42

        def __repr__(self):
            return 'Instance of a hidden class'

    attr = _Hidden()
    """
    An attribute of the parent class.

    Attributes:
        hidden_attr: An attribute of the hidden class. The link to this is ``mwe.Parent.hidden_attr``
            instead of ``mwe.Parent.attr.hidden_attr``
            
            Attributes:
                foo: Another level. Will be linked as ``mwe.Parent.foo`` instead of
                    ``mwe.Parent.attr.hidden_attr.foo``

    """

    hidden_attr = 7
    """
    An attribute of the Parent class with the same name as an attribute of :attr:`attr`. Because
    :attr:`hidden_attr` above already occupies ``mwe.Parent.hidden_attr``, this will be
    ``id0`` and produce a warning
    
    .. code:: shell
    
        docstring of mwe.Parent.hidden_attr:1: WARNING: duplicate object description of
        mwe.Parent.hidden_attr, other instance in mwe, use :noindex: for one of them

    """

    class Child:
        """
        A class within the parent class
        """

        attr = 2
        """
        An attribute of a nested class
        """