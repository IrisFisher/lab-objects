"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    wirt = User('the_pilgrim')
    greg = User('mr_candy_pants')

    poem = Tweet('the_pilgrim', 'Though I am lost, my wounded heart resides back home, in pieces strewn about the graveyard of my lost love. #forSara')
    wirt.follow()
    wirt.unfollow()
    poem.like()
    poem.unlike()

    reply = Tweet('mr_candy_pants', '#aintThatJustTheWay')
    greg.follow()
    reply.like()
    reply.unlike()

    frog_search = Tweet('mr_candy_pants', "anyways, WHERE IS THAT FROG 'O MINE")
    greg.unfollow()
    frog_search.like()
    frog_search.unlike()

    return [wirt, greg] , [poem, reply, frog_search]


def main():
    users, posts = build_feed()
    for item in users:
        print(item)
        print('')

    for item in posts:
        print(item)
        print (item.hashtags())
        print('')


if __name__ == '__main__':
    main()
