#!/usr/bin/python3
'''Starter types for the community feed lab.'''
import string

class User:
    def __init__(self, username):
        '''
        Create a user with the given username and zero followers.

        >>> u = User('rtealwitter')
        >>> u.username
        'rtealwitter'
        >>> u.followers
        0
        '''
        self.username = username
        self.followers = 0


    def follow(self):
        '''
        Gain one follower.

        >>> u = User('alice')
        >>> u.follow()
        >>> u.follow()
        >>> u.followers
        2
        '''
        self.followers += 1


    def unfollow(self):
        '''
        Lose one follower, but never drop below zero.

        >>> u = User('alice')
        >>> u.follow()
        >>> u.follow()
        >>> u.unfollow()
        >>> u.followers
        1
        >>> u.unfollow()
        >>> u.unfollow()
        >>> u.followers
        0
        '''
        if self.followers >= 1:
            self.followers -= 1

    def __str__(self):
        '''
        Show a user as an @-handle.

        >>> print(User('alice'))
        @alice
        >>> str(User('bob'))
        '@bob'
        '''
        return ('@' +str(self.username))

    def __eq__(self, other):
        '''
        Two users are equal when they have the same username.

        >>> User('alice') == User('alice')
        True
        >>> User('alice') == User('bob')
        False
        >>> User('alice') == 'alice'
        False
        '''
        try:
            if self.username == other.username:
                return True
            else:
                return False
        except AttributeError:
            return False

class Tweet:
    def __init__(self, author, text):
        '''
        Create a tweet by `author` saying `text`, starting with zero likes.

        >>> t = Tweet('alice', 'hello world')
        >>> t.author
        'alice'
        >>> t.text
        'hello world'
        >>> t.likes
        0
        '''
        self.author = author
        self.text = text
        self.likes = 0

    def like(self):
        '''
        Add one like.

        >>> t = Tweet('alice', 'hello')
        >>> t.like()
        >>> t.like()
        >>> t.likes
        2
        '''
        self.likes += 1

    def unlike(self):
        '''
        Remove one like, but never drop below zero.

        >>> t = Tweet('alice', 'hello')
        >>> t.like()
        >>> t.unlike()
        >>> t.unlike()
        >>> t.likes
        0
        '''
        if self.likes >= 1:
            self.likes -= 1

    def hashtags(self):
        '''
        Return the hashtags in the text, without the leading '#'.

        >>> Tweet('alice', 'learning #python and #oop today').hashtags()
        ['python', 'oop']
        >>> Tweet('bob', 'just a normal tweet').hashtags()
        []
        >>> Tweet('alice', '#Games #Games #BringSnacks! word#inside #').hashtags()
        ['Games', 'Games', 'BringSnacks!', '']
        '''
        
        hashtags = []
        i = 0
        for i in range(len(str(self.text))):
            if str(self.text)[i] == '#' and (i == 0 or (str(self.text)[i-1] in string.whitespace) or str(self.text)[i-2:i-1] == '\n'):
                word_end = len(str(self.text)) + 1
                if self.text.find('\n', i+1) != -1 and self.text.find('\n', i+1) < word_end:
                    word_end = self.text.find('\n', i+1)
                for char in string.whitespace:
                    if self.text.find(char, i+1) != -1 and self.text.find(char, i+1) < word_end:
                        word_end = self.text.find(' ', i+1)
                if word_end != len(str(self.text)) + 1:
                    tag = self.text[i+1:word_end]
                else:
                    tag = self.text[i+1:]
                hashtags.append(tag)
        return hashtags


    def __str__(self):
        '''
        Show a tweet as "@author: text".

        >>> print(Tweet('alice', 'hello world'))
        @alice: hello world
        '''

        return ('@' + str(self.author) + ': ' + str(self.text))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
