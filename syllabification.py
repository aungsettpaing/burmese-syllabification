import re

def phonetic_syllabification(sentence):
    # break syllables
    result = syllable_break(sentence)
    print(" + ".join(result))


def orthographic_syllabification(sentence):
    # pre-process the sentence by replacing virama sign with athat
    sentence = re.sub("်္", "်", sentence)
    sentence = re.sub("(?<!်)္", "်", sentence)

    # break syllables
    result = syllable_break(sentence)
    print(" + ".join(result))



def syllable_break(sentence):
    # myanmar character list
    special = "[ဣဤဧဩဿဪ၌၍၏ဥဦ၎ဿ]"
    consonants = "[က-အ]"

    counter = 0
    previous = 0
    result = []

    # remove all spaces
    sentence = re.sub("\s+", "", sentence)

    # change typing order
    sentence = re.sub("့်", "့်", sentence) 
    sentence = re.sub("ဥ်", "ဉ်", sentence)

    while counter < len(sentence):
        if re.search(consonants, sentence[counter]):
            if re.search("[္]", sentence[max(0, counter - 1)]) or re.search("[္်]", sentence[min(len(sentence) - 1, counter + 1)]):
                pass
            else:
                if previous != counter:
                    result.append(sentence[previous: counter])
                    previous = counter
        elif re.search(special, sentence[counter]):
            if previous != counter:
                result.append(sentence[previous: counter])
            previous = counter
        counter += 1

    result.append(sentence[previous: counter])

    return result


def main():
    test_sentence = "ရန်ကုန်မှမန္တလေးသို့"
    phonetic_syllabification(test_sentence)
    orthographic_syllabification(test_sentence)


if __name__ == "__main__":
    main()