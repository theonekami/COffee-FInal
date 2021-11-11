import difflib
import xml.etree.ElementTree as ET

file_lst = ["BER", "02.WOT", "BP1", "BP2", "BP3", "COG", "DOC", "FUR", "KAY", "MAD", "SET", "SVP", "TRI"]

# full name dict
card_dict = {}

# word pair dict
card_dict_pair = {}

# one word dict
card_dict_split = {}
 

def parse_xml(xml_file_name):
	tree = ET.parse(xml_file_name + ".xml")
	root, curr_index = tree.getroot(), 0
	while True:
		try:
			card_name_real = root[1][curr_index][0].text
			card_name = card_name_real.lower()
			card_name.replace(',', '')
			card_link = [card_name_real, root[1][curr_index][1].attrib['picURL']]
			card_dict[card_name] = card_link

			card_words = card_name.split()
			if len(card_words) > 1:
				card_pairs = [card_words[i] + " " + card_words[i + 1] for i in range(len(card_words) - 1)]
			else:
				card_pairs = card_words

			for word in card_words:
				if word not in card_dict_split:
					card_dict_split[word] = [card_link]
				else:
					if card_link not in card_dict_split[word]:
						card_dict_split[word].append(card_link)

			for pair in card_pairs:
				if pair not in card_dict_pair:
					card_dict_pair[pair] = [card_link]
				else:
					if card_link not in card_dict_pair[pair]:
						card_dict_pair[pair].append(card_link)


		except Exception as e:
			break
		curr_index += 1
	return

for file in file_lst:
	print(file)
	parse_xml(file)

def return_image(user_string):
	all_links_s, all_links, single = [], [], []

	try:
		all_links_s = card_dict_split[difflib.get_close_matches(user_string, card_dict_split.keys())[0]]
	except Exception:
		print()
	if len(all_links_s) == 1:
		return all_links_s[0]
	else:
		print("Single-word match failed - too ambiguous.")
		try:
			all_links = card_dict_pair[difflib.get_close_matches(user_string, card_dict_pair.keys())[0]]
		except Exception:
			print()
		if len(all_links) == 1:
			return all_links[0]
		else:
			print("Pair-word match failed - too ambiguous.")
			single = [card_dict[x] for x in difflib.get_close_matches(user_string, card_dict.keys())]
			try:
				return card_dict[difflib.get_close_matches(user_string, card_dict.keys())[0]]
			except Exception:
				print()
				print("No matches. Please try again!")

	print()

	to_suggest = []
	print("Did you mean: ")
	if len(all_links_s) <= 3:
		for elem in all_links_s:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)

	if len(all_links) <= 3:
		for elem in all_links:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)

	if len(single) <= 3:
		for elem in single:
			name = elem[0]
			if name not in to_suggest:
				to_suggest.append(name)
				print(name)
