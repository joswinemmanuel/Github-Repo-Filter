class GitHubRepo:

    def __init__(self, name, language, num_stars, url_data):
        self.name = name
        self.language = language
        self.num_stars = num_stars
        self.url_data = url_data

    def __str__(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars and url {self.url_data}."

    def __repr__(self):
        return f'GitHubRepo({self.name}, {self.language}, {self.num_stars}, {self.url_data})'