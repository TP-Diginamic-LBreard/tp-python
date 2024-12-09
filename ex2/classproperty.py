class classproperty(property):
    """
    Propriété de classe.

    Transforme la méthode décorée en méthode de classe.
    Appelle la méthode de classe ainsi créée.
    Retourne le résultat de l'invocation.

    (pas besoin de __set__ dans notre cas)
    """
    # 1er paramètre de __get__ est l'instance, on n'en a pas ici.
    def __get__(self, _, cls):
        # self.fget est la méthode décorée par @property
        return classmethod(self.fget).__get__(_, cls)()
