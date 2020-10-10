# Change the indicated letter in a sentence. 

song = '''You look so beautiful in this light
Your silhouette over me.

The way it brings out the blue in your eyes
Is the Tenerife sea.

And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness.'''

word_to_change = 'voices'
voices_start_index = song.find(word_to_change)
voices_end_index = voices_start_index + len(word_to_change)

song_part1 = song[:voices_start_index]
song_part2 = song[voices_end_index:]

new_song = song_part1 + 'sounds' + song_part2

print(new_song)