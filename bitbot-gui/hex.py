import os, pathlib, binascii, random, time
from os import chdir as cd

# root = pathlib.Path().absolute()

def uniquify(filename, fac=100):
	""" Returns the input path with trailing sequential numbers if such file
		already exists. """

	ext = "." + filename.split('.')[-1]
	file = pathlib.Path(filename).with_suffix('')

	counter = 0
	outpath = f"{file}-{(fac / 100):0.2f}-{counter}{ext}"

	while os.path.isfile(outpath):
		counter += 1
		outpath = f"{file}-{(fac / 100):0.2f}-{counter}{ext}"

	return outpath

def overwrite_str(base, substr, index):
	""" Overwrite base with substr starting at index. """
	if index + len(substr) >= len(base):
		index = len(base) - len(substr)
	new_str = base[:index] + substr + base[index + len(substr):]
	return new_str


def distort(path, ratio, out_dir=f"./out/", photofix=False):
	if not out_dir.endswith('\\'):
		out_dir += '\\'

	with open(path, 'rb') as f:
		data = f.read()

	num_bytes = os.path.getsize(path)
	chunk_size = round(num_bytes / 100)
	margin = chunk_size / 10

	START = round(margin)
	END = round(num_bytes - margin - chunk_size)

	indices = random.sample(range(START, END), ratio) # select n (ratio) indices to override in the byte stream

	#### Method 1: Replace byte streams with random cryptographic hashes.
	for i in sorted(indices):
		new_val = binascii.b2a_hex(os.urandom(chunk_size))
		data = overwrite_str(data, new_val, i)

	#### Method 2: Delete random substreams entirely
	# for i in sorted(indices):
	# 	data = data[:i] + data[i + chunk_size:]

	#### Method 3: Reverse each of the byte substreams and reinsert them. (WIP)
	# def reverse_bits(substring):
	# 	substring = substring.decode()
	# 	return str.encode(substring[::-1])
	#
	# for i in sorted(indices):
	# 	data = data[:i] + reverse_bits(data[i:i + chunk_size]) + data[i + chunk_size:]

	#### Method 4: Perform some other operation on the 'chunk' being selected (TBD)
	# pass


	filename = path.split('\\')[-1]
	with open(uniquify(out_dir + filename, fac=ratio), 'wb') as f:
		f.write(data)

	if photofix:
		pass # TODO: transcode images to rasterize results. use PIL and save all as PNGs?

	return
