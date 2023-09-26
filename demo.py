from kf_sentence_detector import KFSentenceDetector


words = ['高端班', '应试', '不知道', '高端班', '您只能', '集训']
model_config_path = 'data/re_model_config.json'
kf_detector = KFSentenceDetector(words, model_config_path)


if __name__ == '__main__':

    input_text = [
        {
            "text": "后右下角儿有个高端班次孩子中考分数是多少分呀",
            "begin_time": 1326750,
            "end_time": 1332165
        },
        {
            "text": "看一下题目为什么呢？",
            "begin_time": 1326751,
            "end_time": 1332165
        },
        {
            "text": "你先把题目看一下第三问。",
            "begin_time": 1326752,
            "end_time": 1332165
        }
    ]

    result = kf_detector.predict_text_list_format(input_text)
    print(result)
