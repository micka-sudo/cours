

if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")
    
    
   # Pour vérifier le type d'une variable, on peut utiliser la fonction type ou la fonction isinstance.
#   On préfèrera la fonction isinstance qui gère l'héritage.

    >>> default_dict = {}
     
    >>> type(default_dict)  # Notre dictionnaire est bien de type 'dict'
    <type 'dict'>
     
    >>> class CustomDict(dict):  # On créé une classe custom, qui hérite de la classe 'dict'
    ...     pass
     
    >>> custom_dict = CustomDict()
     
    >>> type(custom_dict)
    <class '__main__.CustomDict'>
     
    # Avec la fonction type(), notre dictionnaire custom n'est pas reconnu comme étant de type 'dict'
    >>> type(custom_dict) == dict
    False                     
     
    # La fonction isinstance en revanche comprend que notre dictionnaire custom hérite de la classe 'dict'
    >>> isinstance(custom_dict, dict)
    True                      