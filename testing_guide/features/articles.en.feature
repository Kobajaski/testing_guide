Feature: Articles

    Scenario: Access to the website
        Given the fixture test_articles
        When i access the url index
        Then i am redirected to list_articles

    Scenario: Access to a list of Artciles
        Given the fixture test_articles
        When i access the url list_articles
        Then i have 15 articles listed
          And i am on page 1 over 3

    Scenario: Access to a list of Artciles on the page 2
        Given the fixture test_articles
        When i access the url list_articles on page 2
        Then i have 15 articles listed
          And i am on page 2 over 3

    Scenario: Access to a list of Artciles on the page 2
        Given the fixture test_articles
        When i access the url list_articles filtered on Dev
        Then i have 2 articles listed

    Scenario: Access to a specific article on page 2
        Given the fixture test_articles
        When i access the url list_articles on page 2
          And i open article 1
        Then i am on the good article
          But i don't have article's list
