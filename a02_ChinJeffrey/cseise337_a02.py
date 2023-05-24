import re

# Problem 1
def highlight(pattern, string):
    pattern_obj = re.compile(pattern)
    res = pattern_obj.search(string)
    if res:
        s = string[:res.start()] + "<" + string[res.start():res.end()] + ">" + string[res.end():]
        return s
    return None

# pattern = r'\bbook\B'
# s1 = ["bookstore", "booking", "textbooks",
#  "'returned books'", "audiobook"]
 
# for s in s1:
#     print(highlight(pattern, s))

# highlight(r'[a-zA-Z]\d', "ShepardN7")

# Problem 2
def highlight_all(pattern, string):
    pattern_obj = re.compile(pattern)
    res = pattern_obj.findall(string)
    print(res)
    if res:
        for r in res:
            s = string[:string.find(r)] + "<" + string[string.find(r):string.find(r)+len(r)] + ">" + string[string.find(r)+len(r):]
            string = s
        return s
    return None

# pattern = r'o\w+'
# string = "I'm Commander Shepard and this is my favorite store on the Citadel."

# print(highlight_all(pattern, string))

# Problem 3
def ruin_a_webpage(filename):
    if not (filename.endswith(".html") or filename.endswith(".htm")):
        return None
    else:
        with open(filename, "r") as file:
            s = file.read()
            
        p_pattern = r'(<p[^>]*>)+(.*?)(</p>)+'
        s_pattern = r'(<span[^>]*>)*(.+?)(</span>)*'

        s = re.sub(p_pattern, r'\2<br><br>', s, flags = re.DOTALL)
        s = re.sub(s_pattern, r'\2', s, flags = re.DOTALL)

        with open(filename, "w") as file:
            file.write(s)
        return True
print(ruin_a_webpage("index.html"))

# Problem 4
def decompose_path(path):
    # pattern to find chars before and after colons in a string 
    pattern = r'([^:]+)'
    pattern_object = re.compile(pattern)
    res = pattern_object.findall(path)
    return res

# print(decompose_path("/usr/openwin/bin:/usr/ucb:/usr/bin:/bin:/etc:/usr/local/bin:/usr/local/lib:/usr/shareware/bin:/usr/shareware/lib:."))

# Problem 5
def link_mapper(filename):
    if not (filename.endswith(".html") or filename.endswith(".htm")):
        return None
    else:
        dict = {filename: []}
        with open(filename, "r") as file:
            s = file.read()
            pattern = r'<a href="(.+?)">(.+?)</a>'
            pattern_object = re.compile(pattern)
            res = pattern_object.findall(s)
            for tuple in res:
                new_tuple = (tuple[1], tuple[0])
                dict[filename].append(new_tuple)

        return dict

# print(link_mapper("index.html"))

# Problem 6
def grammarly(text):
    # Fixing "i" instead of "I"
    text = re.sub(r'\bi\b', 'I', text)

    # pattern to check for lowercase letter of first word or letter in more than once sentence
    pattern = r'(^[a-z]).*'
    pattern_lol = r'\.\s*([a-z])'
    pattern_object = re.compile(pattern)
    pattern_object_lol = re.compile(pattern_lol)
    res = pattern_object.findall(text)
    if res:
        text = text[0].upper() + text[1:] 
    
    res_lol = pattern_object_lol.finditer(text)
    if res_lol:
        for match in res_lol:
            text = text[:match.start()+2] + text[match.start()+2].upper() + text[match.start()+3:]

    # pattern to check for lowercase i in i'm
    pattern2 = r'\s(i\'m)\s'
    text = re.sub(pattern2, " I'm ", text)

    # pattern to use an instead of a before a word that starts with a vowel
    # pattern to find and a before a word that starts with a vowel in the beginning of a sentence
    text = re.sub(r'^A\s([aeiou])', r'An \1', text)
    text = re.sub(r'\s[aA]\s([aeiou])', r' an \1', text)

    # pattern to check for repeated word
    pattern4 = r'\b(\w+)(\s+\1)+\b'
    text = re.sub(pattern4, r'\1', text, flags=re.IGNORECASE)

    # pattern to check for missing oxford comma
    text = re.sub(r'\b(\w+\s*(?:,\s*\w+)*)\s+(and|or)\s+(\w+)\b', r'\1, \2 \3', text)

    # unclosed parentheses
    stack = []
    pattern5 = r'[()]'
    pattern_object5 = re.compile(pattern5)
    res5 = pattern_object5.finditer(text)
    if res5:
        for match in res5:
            print(match)
            if match.group() == '(':
                stack.append(match)
            elif not stack:
                text = text[:match.start()] + text[match.start()+1:]
            else:
                stack.pop()
        for match in stack:
            text = text[:match.start()] + text[match.start()+1:]

    return text

# print(grammarly("I have a apple apple, i'm a a eye, too much much of a item and a orange."))
# print(grammarly("Our favorite companions are Garrus, Wrex and Tali."))
# print(grammarly("A apple APPLE apple, a pear and a orange. a boy likes a girl. the girl no like boy. Apple."))
# print(grammarly("This (case (is about parentheses)."))
# print(grammarly("This (is (another (case) about) parentheses."))
# print(grammarly("This is (another case about) parentheses)."))
