class Developer:
    """
    Main class
    """
    def __init__(self, years_experience, name):
        self.years_experience = int(years_experience)
        self.name = str(name)
        self.language = ''

    def about(self):
        if self.years_experience <= 3:
            print("My name is {name} and I am a Junior Developer.".format(name=self.name))
        elif self.years_experience <= 5:
            print("My name is {name} and I am a Middle Developer.".format(name=self.name))
        else:
            print("My name is {name} and I am a Senior Developer.".format(name=self.name))


    def write_code(self):
        print("I am {name} developer and I write code".format(name=self.name))

    def __str__(self):
        return'{name} - {years_experience} years, {language} '.format(name=self.name,
                                                                      years_experience=self.years_experience,
                                                                      language=self.language)

    def __call__(self):
        return "I use {language} to write code".format(language=self.language)


class PythonDeveloper(Developer):
    """
    Class inheritance Developer
    """
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Python'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))

class JavaDeveloper(Developer):
    """
    Class inheritance Developer
    """
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Java'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))

class RubyDeveloper(Developer):
    """
    Class inheritance Developer
    """
    def __init__(self, years_experience, name):
        Developer.__init__(self, years_experience, name)
        self.language = 'Ruby'

    def write_code(self):
        print("I use {language} to write code".format(language=self.language))
