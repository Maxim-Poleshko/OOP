class ItCompany:
    """
    Class company that will keep the developers
    """
    devs_list = []

    def add(self, memb):
        if memb.years_experience < 3:
            print('{name} =*( little experience'.format(name=memb.name))
        else:
            print('{name} added in team'.format(name=memb.name))
            self.devs_list.append(memb)

    def lay_off_emp(self, name):
        for memb in self.devs_list:
            if name == memb.name:
                self.devs_list.remove(memb)
                print('{name} your experience is not enough for us'.format(name=memb.name))



    def sort_team(self):
        self.devs_list = sorted(self.devs_list, key=lambda x: x.years_experience)
        for developer in self.devs_list:
            print('{name} - {years_experience} years, {language}'.format(name=developer.name,
                                                                         years_experience=developer.years_experience,
                                                                         language=developer.language))
