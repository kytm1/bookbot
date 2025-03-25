def text_count(text):
    words = text.split()
    return len(words)


def count_char(text):
	
	
	tmp_list=text.lower()
	temp_dict={}
	for i in tmp_list:
		if i in temp_dict:
			temp_dict[i]+=1
		else:
			temp_dict[i]=1

	return temp_dict



def sort_on(dict):
    return dict["num"]