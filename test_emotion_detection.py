from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    # test function for emotion analyzer of text
    def test_emotion_analyzer(self):
        """
        asserts result for analysis of text
        """

        # test case for input string - 'I am glad this happened'
        result_1 = emotion_detector('I am glad this happened')
        result = self.assertEqual(result_1['dominant_emotion'], 'joy')
        print(f"Statment: 'I am glad this happened', Dominant Emotion: {result_1['dominant_emotion']}")

        # test case for input string - 'I am really mad about this'
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        print(f"Statment: 'I am really mad about this', Dominant Emotion: {result_2['dominant_emotion']}")        

        # test case for input string - 'I feel disgusted just hearing about this'
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')        
        print(f"Statment: 'I feel disgusted just hearing about this', Dominant Emotion: {result_3['dominant_emotion']}")                

        # test case for input string - 'I am so sad about this'
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')        
        print(f"Statment: 'I am so sad about this', Dominant Emotion: {result_4['dominant_emotion']}")                

        # test case for input string - 'I am really afraid that this will happen'
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')        
        print(f"Statment: 'I am really afraid that this will happen', Dominant Emotion: {result_5['dominant_emotion']}")                

unittest.main()                