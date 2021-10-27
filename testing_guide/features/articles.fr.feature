Fonctionnalité: Articles

    Scénario: Accéder au site
        Etant donné la fixture test_articles
        Lorsque j'accède à l'URL index
        Alors je suis redirigé vers list_articles

    Scénario: Accéder a une liste d'articles
        Etant donné la fixture test_articles
        Lorsque j'accède à l'URL list_articles
        Alors j'ai 15 articles de listés
          Et je suis sur la page 1 sur 3

    Scénario: Accéder a une liste d'articles sur la page 2
        Etant donné la fixture test_articles
        Lorsque j'accède à l'URL list_articles sur la page 2
        Alors j'ai 15 articles de listés
          Et je suis sur la page 2 sur 3

    Scénario: Accéder a une liste d'articles filtré
        Etant donné la fixture test_articles
        Lorsque j'accède à l'URL list_articles filtré sur Dev
        Alors j'ai 2 articles de listés

    Scénario: Accéder a un articles sur la page 2
        Etant donné la fixture test_articles
        Lorsque j'accède à l'URL list_articles sur la page 2
          Et que j'ouvre l'article 1
        Alors je suis sur le bon article
          Mais je n'ai plus de liste d'article
