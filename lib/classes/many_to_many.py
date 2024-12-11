class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        self.author = author
        self.magazine = magazine
        self._title = title  

        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, mag):
        if isinstance(mag, Magazine):
            self._magazine = mag

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string with 2-16 characters.")
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1

        return [author for author, count in author_count.items() if count > 2]

author1 = Author("Joe")
magazine = Magazine("Info Daily", "Technology")

article1 = author1.add_article(magazine, "Tech is the Best")

print(f"Article by: {author1.name}")
for article in author1.articles():
    print(f"  {article.magazine.name}")

print(f"Magazines by: {author1.name}")
for mag in author1.magazines():
    print(f"  {mag.name}")

print(f"Articles in: {magazine.name}")
for article in magazine.articles():
    print(f"  {article.title}")
