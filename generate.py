import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

STYLES = {
  'Crystals': '''Great ice oceans radiant of light
Were turning their faces to the eternal sun.
In the hell of vulcano the fire scattered
Fiery roses of helium and hydrogen.
Crystals great like the earth's towns
Hanging on the threads of liquid Atmosphere
Stunned me with their indecent forms.
Entering the crystal spheres
I was shouting my name
Which then spread, echoing,
Into the most distant corners of the Universe. '''

, 'Grasshoppers': '''My arrival
Has excited just the green-yellow grasshoppers
Of unimaginable size.
Catching with their hind legs
The sticky morning light
They were making very skillfully
Barricades
Of the numberless cubes of quartz
Closing access to me
To the planet's center. '''

, 'Metals': '''
I listened to breathing of metals
Similar to breathing of beasts
Metals warred against air
Moved through underground corridors like moles,
undermining stability of the planet
Air entered the crevices on the crust
And attacked them trying to cause
Chemical changes in their characters
They swallowed it greedily
And then digested for a long time. '''

, 'Egg': '''
On the leaf of a copper-colored herb
A butterfly laid an egg
Of human eye size.
That egg is a little planet
That will wake up
In three light years.
Then so woken
It will orbit around a flower
Like around its own Sun. '''

, 'Machines': '''
Machines were catching us
With their sharp gears
And ground slowly meat and bones.
Blood flew away by special drains
For irrigation of carnivore herbs
It was a systematic destruction of our bodies
But our spirit even more curiously
Continued research into stars. '''

, 'Out of order': '''
A year ago i bought miroljub todorovic of
czechoslovakian production. at the purchase
i didn't get written warranty, but i considered
it unnecessary anyway, for a miroljub todorovic
is not an easily spoilt good. immediately after
the purchase i found its eye is out of order and
that therefore miroljub todorovic is not precise.
i tried to repair it, but my effort was useless.
so now i have a miroljub todorovic i can not use. '''

, 'Alphabet of crippled wolf': '''I'm burrowing through you. You bone-breaking
Cave of Serbian language. Blood and graves.
Bee bread and honey. Curse in fertile land. Scepter
in maneuver. I'm covering my face with soil.
I rejoyce at the birth. Olympus and Rome among
your teeth. Alphabet of crippled wolf. Cruel and
shaggy. By sticky spit you shackle up the contagious
deities. You bless with fetid urea. '''

, 'Vid': '''In lakes of the north. In Baltic fogs.
Time dismembers itself. I have woken up.
Descended from the mountain. In the beginning
of summer. Light. War. And Vid. Your breath
is ruddy. Like a wild rose flower. You supreme
deity. Of ancient Serbian religion. Axes smell.
Blood. And burning sacrifices. In a horn. Honey
brandy. Foretells a harvest. '''

, 'Ruddy magician': '''From Spasm. Hissous word. Stairway
toward sanctuary. All my beaters.
Downpours wash poems away.
From walls. From books. You made
Homer blind. You crazy warrior. Ice
conquers. Fever from steel.
Mercury cools. Jupiter
explodes. Slavs in front of
purple towers of Constantinople.
They gnaw my skull. Wild
Thracian dogs. Water nymphs from
whirlpools. You stand in air. With one leg.
In the Mediterranean Sea. October
closes roads. You ruddy magician.
Neither in the sky. Nor on the earth. '''

, 'Dark blue demon': '''By the way. Mortuary. Rain. Wavering. Germ
of speech. You are lying under a sunflower.
Seductive swan. Apotheosis of the unconsciousness.
Human turmoil. You dark blue demon. Am I a bead.
Or a god. In a wild paradise. Closed. In innocent words
Play of green pebbles. Spring. Spring. Strong sinews
of the world. Yuu are tempting the language. Foaming
of lymph. They rise from abbys. Firm snow and morning
star. Monster watches. Interior and burn. It is a time of
decision. In a ruddy morning song. Graves freeze. Flower
field. Entropy. They are more and more away. Chasers.
Hostel burns. Under the mask of hellebore. You shiver
noisily. Skin has emptied. Where is the end? In innocent
words. Ocean boils. '''
}

def generate (style, input, output_len):

	tokenizer = GPT2Tokenizer.from_pretrained('./tokenizer')
	model = TFGPT2LMHeadModel.from_pretrained('./model', pad_token_id=tokenizer.eos_token_id)

	tf.random.set_seed(42)

	prefix = STYLES[style]

	input_ids = tokenizer.encode(prefix + input, return_tensors='tf')
	input_ids_len = input_ids.shape.as_list()[1]

	if output_len < input_ids_len:
		output_len = input_ids_len

	output = model.generate(
		input_ids,
		do_sample=True,
		max_length=output_len,
		top_k=60,
		top_p=0.95,
		num_return_sequences=1
	)

	return tokenizer.decode(output[0], skip_special_tokens=True)[len(prefix):] + ' ...'

