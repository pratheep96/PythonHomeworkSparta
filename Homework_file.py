sparta = {}
sparta ={
    'Hero': 'Sparta',
    'Beginning': 'Once upon a time there was a hero called Sparta',
    'Middle': 'He went to war with the Dark Spartan',
    'End': 'This is for you to decide!',
}

print(sparta['Hero'])
print(sparta['Beginning'])
print(sparta['Middle'])
print(sparta['End'])


Your_ending = input('How do you think the story ended?')
Your_hero = input('Who do you think helped our hero?')
New_ending = Your_ending + ' and your hero ' + Your_hero + ' helped Sparta win the war '
print(New_ending)