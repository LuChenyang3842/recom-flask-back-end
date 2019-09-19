from textblob import TextBlob
import emoji
import re


class sentiment_recommendation():

    def __init__(self, keyword_list):
        self.keyword_dic = keyword_dic
        self.keyword_list = list(keyword_dic.keys())

    def clean_text(self, raw_user_text):
        """
        Regular expression and emoji interpretation on the raw user tex.
        :param tweet: str
            User text.
        :return: str
            User text.
        """
        user_text = emoji.demojize(raw_user_text)  # interpret emoji
        # return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", user_text).split())).lower()
        # return (' '.join(user_text).split()).lower()
        return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z '\t])|(\w+:\/\/\S+)", " ", user_text).split())).lower()

    def sentiment_analysis(self, user_text):
        analysis = TextBlob(self.clean_text(user_text))
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            print(analysis.sentiment.polarity)
            return 0
        else:
            return -1

    def keyword_extraction(self, user_text):
        def list_intersection(lst1, lst2):
            return set(lst1).intersection(set(lst2))
        words = list(map(str.strip, self.clean_text(user_text).split(' ')))

        return list(list_intersection(words, self.keyword_list))

    def generate_keywords(self, user_text):
        def list_subtract(lst1, lst2):
            return list(set(lst1) - set(lst2))

        def get_keword_id_list(keywords):
            return [self.keyword_dic[x] for x in keywords]

        sentiment = self.sentiment_analysis(user_text)
        keywords = self.keyword_extraction(user_text)

        if sentiment == 1:
            final_keywords = keywords
        elif sentiment == -1:
            final_keywords = list_subtract(self.keyword_list, keywords)
        else:
            final_keywords = self.keyword_list

        return get_keword_id_list(final_keywords)


# if __name__ == '_main__':

test_text1 = "I like Japanese food and bbq hahaha."
test_text2 = "I enjoy korean food."
test_text3 = "I hate chinese food."

keyword_dic = {
        'chinese': 25,
        'australia': 201,
        'french': 45,
        'bar': 225,
        'bbq': 193,
        'tea': 247,
        'cafe': 1039,
        'coffee': 161,
        'desserts': 100,
        'drink': 268,
        'fish': 298,
        'chips': 298,
        'korean': 67,
        'pub': 983,
        'vegetarian': 308,
        'yumcha': 978,
        'thai': 95,
        'tea': 163,
        'steak': 171,
        'sichuan': 128,
        'spanish': 89,
        'pho': 1020,
        'icecream':233,
        'indian': 148,
        'japanese': 60
        }


keyword_list = list(keyword_dic.keys())
# keyword_list = ['japanese','chinese','korean','australia']

analysis = sentiment_recommendation(keyword_list)


print(analysis.generate_keywords(test_text1))
print(analysis.generate_keywords(test_text2))
print(analysis.generate_keywords(test_text3))

# print(TextBlob('hate japnese food').sentiment.polarity)
