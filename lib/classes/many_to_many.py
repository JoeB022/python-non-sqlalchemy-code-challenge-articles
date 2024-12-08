class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        self.author = author
        self.magazine = magazine
        self._title = title  #making the attribute private for access in the property method when modifying

        # Maintaining relationships
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title  #Immutable


class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Author name must be a string.")
        self._name = value

    def articles(self):
        """Returns all articles written by the author."""
        return self._articles

    def magazines(self):
        """Returns unique magazines the author has contributed to."""
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        """Creates and associates a new article."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns unique categories of magazines the author has contributed to."""
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be a string with 2-16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        """Returns all articles published in the magazine."""
        return self._articles

    def contributors(self):
        """Returns unique authors who contributed to the magazine."""
        return list({article.author for article in self._articles})

    def article_titles(self):
        """Returns titles of all articles in the magazine."""
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Returns authors with more than 2 articles in the magazine."""
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1

        return [author for author, count in author_count.items() if count > 2]
