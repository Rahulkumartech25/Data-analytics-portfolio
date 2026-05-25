import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "I think, therefore I am.",
]

def measure_accuracy(test_sentence, user_input):
    test_words = test_sentence.split(" ")
    user_words = user_input.split(" ")
    correct_words = sum(1 for t, u in zip(test_words, user_words) if t == u)
    accuracy = (correct_words / len(test_words)) * 100
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(test_sentence)
    input("Press Enter to start...")
    start_time = time.time() # Record the start time
    user_input = input("\nstart typing:\n")
    end_time = time.time() # Record the end time
    time_taken = end_time - start_time # Calculate the time taken
    time_taken_in_seconds = time_taken # No conversion needed
    word_count = len(test_sentence.split(" ")) # Count the number of words in the test sentence

    print("Results:")
    print(f"Time taken: {time_taken_in_seconds:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing speed: {word_count / time_taken_in_seconds * 60:.2f} words per minute")
    accuracy = measure_accuracy(test_sentence, user_input)
    print(f"Accuracy: {accuracy:.2f}%")
    

typing_test()