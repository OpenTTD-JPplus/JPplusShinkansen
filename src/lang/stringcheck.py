
separator = ':'
languages = ["russian", "japanese", "korean", "simplified_chinese"]
'''
with open("english.lng") as eng:
    english = eng.read().splitlines()
    with open('stringlist.txt', 'w') as w:
        masterlist = []
        w.write('English Lang File Strings\n\n')
        for line in english:
            if not line.startswith('#'):
                if line.strip():
                    string = line.split(separator,1)[0]
                    string = string.strip()
                    w.write(string)
                    w.write('\n')
                    masterlist.append(string)
'''
def StringListFor(language):
    with open(str(language) + ".lng") as lang:
        stringlist = lang.read().splitlines()
        language_strings = []
        for line in stringlist:
            if not line.startswith('#'):
                if line.strip():
                    string = line.split(separator,1)[0]
                    string = string.strip()
                    language_strings.append(string)
    return language_strings

english_strings = StringListFor("english")

with open('stringlist.txt', 'w') as w:
    w.write('English Lang File Strings\n\n')
    for l in languages:
        w.write('\n')
        w.write(str(l) + ' Missing Lang File Strings\n')
        string_list = StringListFor(l)
        missing_strings = list(set(english_strings) - set(string_list))
        if not missing_strings:
            w.write('\tNo Missing Strings')
            w.write('\n')
        else:
            for m in missing_strings:
                w.write(m)
                w.write('\n')
        w.write('\n')
        w.write(str(l) + ' Extra Lang File Strings\n')
        extra_strings = list(set(string_list) - set(english_strings))
        if not extra_strings:
            w.write('\tNo Extra Strings')
        else:
            for e in extra_strings:
                w.write(e)
        w.write('\n')
