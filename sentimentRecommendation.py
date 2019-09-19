from textblob import TextBlob
import emoji
import re
import requests


class sentiment_recommendation():

    def clean_text(self, raw_user_text):
        """
        Regular expression and emoji interpretation on the raw user tex.
        :param tweet: str
            User text.
        :return: str
            User text.
        """
        # print(raw_user_text)
        # user_text = raw_user_text
        user_text = emoji.demojize(raw_user_text)  # interpret emoji
        # return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", user_text).split())).lower()
        # return (' '.join(user_text).split()).lower()
        return (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z '\t])|(\w+:\/\/\S+)", " ", user_text).split())).lower()

    def sentiment_analysis(self, user_text):
        # print(user_text)
        analysis = TextBlob(user_text)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def keyword_extraction(self, user_text, keyword_list):

        def list_intersection(lst1, lst2):
            return set(lst1).intersection(set(lst2))
        words = list(map(str.strip, user_text.split(' ')))
        # print(list(list_intersection(words, keyword_list)))
        return list(list_intersection(words, keyword_list))

    def generate_keywords(self,raw_user_text):
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

        user_text = self.clean_text(raw_user_text)
        def list_subtract(lst1, lst2):
            return list(set(lst1) - set(lst2))

        def get_keword_id_list(keywords):
            return [keyword_dic[x] for x in keywords]

        sentiment = self.sentiment_analysis(user_text)
        print(sentiment)
        keywords = self.keyword_extraction(user_text, keyword_list)

        if sentiment == 1:
            final_keywords = keywords
        elif sentiment == -1:
            final_keywords = list_subtract(keyword_list, keywords)
        else:
            final_keywords = keyword_list

        return get_keword_id_list(final_keywords)

    def generate_category(self, time):
        # Breakfast = 1
        # Dinner = 10
        # Cafes = 3
        # Lunch = 9
        # Bar = 11
        # Club = 14

        if 5 <= time <= 11:
            return [1, 3]
        elif 11 < time <= 16:
            return [3, 9]
        elif 16 < time <= 20:
            return [3, 10]
        elif 20 < time < 22:
            return [10, 11, 14]
        else:
            return [11, 14]

    def request_for_result(self, lat, lon, text, time):
        cuisine_ids = self.generate_keywords(text)
        print(cuisine_ids)
        categorie_id = self.generate_category(time)

        SEARCH_URL = 'https://developers.zomato.com/api/v2.1/search'

        search_headers = {
            'user-key': 'afbb0f02471c0acb2ac10d6ff9bcda9b',
            'Accept': 'application/json'
            }

        payload = {
            'count': 10,
            'lat':lat,
            'lon':lon,
            'radius':2000,
            'cusines':cuisine_ids,
            'categories':categorie_id,

        }


        r = requests.get(SEARCH_URL, headers=search_headers, params=payload)
        restaurants = r.json()['restaurants']
        return self.resolveResult(restaurants)

    def resolveResult(self, restaurants):
        restaurant_list = []
        for restaurant in restaurants:
            restaurant_list.append({'Name': restaurant['restaurant']['name'], "cuisines": [x.strip() for x in restaurant['restaurant']['cuisines'].split(',')],
            "lat": restaurant['restaurant']['location']['latitude'], "long": restaurant['restaurant']['location']['longitude'], "highlights": restaurant['restaurant']['highlights'], "Thumb": restaurant['restaurant']['thumb'],
            "user_Rating": restaurant['restaurant']['user_rating']['aggregate_rating'],"phone_Numbers": restaurant['restaurant']['phone_numbers']})
        res = {"restaurants":restaurant_list }
        return res


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


# analysis1 = sentiment_recommendation()
# print(analysis1.request_for_result(-37.813629,144.963058, 'I like Japnese food',14))
# print(analysis1.generate_keywords(test_text1))
# print(analysis1.generate_category(10))
#
#
# analysis2 = sentiment_recommendation()
# print(analysis2.generate_keywords(test_text2))
# print(analysis2.generate_category(17))
#
# analysis3 = sentiment_recommendation()
# print(analysis3.generate_keywords(test_text3))
# print(analysis3.generate_category(22))
