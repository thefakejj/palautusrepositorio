from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = (
    query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
    query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()

    # matcher = Or(
    # HasAtLeast(45, "goals"),
    # HasAtLeast(70, "assists")
    # )

    # matcher = (
    #   query
    #   .playsIn("NYR")
    #   .hasAtLeast(10, "goals")
    #   .hasFewerThan(20, "goals")
    #   .build()
    # )

    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
