import codecs

from homework2.tasks import hw1

with codecs.open("data.txt", "r", encoding="unicode-escape") as fi:
    print(get_longest_diverse_words(fi))

    def test_get_longest_diverse_words():
        """Testing that 10 last words are the longest and in ordered fashion instead of random"""
        new_list = get_longest_diverse_words(fi)
        count = -10
        while count != -2:
            assert len(new_list[count]) - len(new_list[count]) >= 0


with codecs.open("data.txt", "r", encoding="unicode-escape") as fi:
    print(get_rarest_char(fi))

    def test_get_rarest_char():
        """Testing that rarest char should appear only 1 time"""
        assert get_rarest_char(fi)[0] == 1


with codecs.open("data.txt", "r", encoding="unicode-escape") as fi:
    print(count_punctuation_chars(fi))

    def test_count_punctuation_chars():
        """Testing that there are 4213 punctuation chars"""
        assert count_punctuation_chars == 4213


with codecs.open("data.txt", "r", encoding="unicode-escape") as fi:
    print(get_most_common_non_ascii_char(fi))

    def test_get_most_common_non_ascii_char():
        """Testing that the most common non ascii char is not ascii"""
        assert not get_most_common_non_ascii_char(fi)[1].isascii()


fi.close()
