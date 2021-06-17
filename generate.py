import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

PREFIX = '''Great ice oceans radiant of light
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

PREFIX_LEN = len(PREFIX)

def generate (input, output_len):

	tokenizer = GPT2Tokenizer.from_pretrained('./tokenizer')
	model = TFGPT2LMHeadModel.from_pretrained('./model', pad_token_id=tokenizer.eos_token_id)

	tf.random.set_seed(42)

	input_ids = tokenizer.encode(PREFIX + input, return_tensors='tf')
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

	return tokenizer.decode(output[0], skip_special_tokens=True)[PREFIX_LEN:]

