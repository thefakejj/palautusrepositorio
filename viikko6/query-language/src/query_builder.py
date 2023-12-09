from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query_list=All()):
        self.query_list = query_list

    def playsIn(self, team):
        # https://en.wikipedia.org/wiki/Snake_case
        return QueryBuilder(And(self.query_list, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_list, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_list, HasFewerThan(value, attr)))

    def build(self):
        return self.query_list
