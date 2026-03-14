Topic 1: Python String

স্ট্রিং কি? কিভাবে ব্যাবহার করে? স্ট্রিং হলো টেক্সট উপস্থাপনের জন্য ব্যবহৃত অক্ষরের একটি ক্রম. এটা লিখতে হয় ' ' অথবা " " এর মধ্যে. তবে যদি একাধিক টেক্সট লিখতে চাই তাহলে """ """ এভাবে লিখতে হবে।

1. Python-এ String কেন প্রয়োজন?

Python-এ যখনই আমরা শব্দ, বাক্য, নাম, ইমেইল, মেসেজ বা যেকোনো লেখা নিয়ে কাজ করি, তখন String ব্যবহার করতে হয়।

2. String কিভাবে তৈরি করে ?

text1 = "Python" 

text2 = 'Programming'

text3 = """ This is the first line. 

This is the second line. 

This is the third line. """

3. String accessing

পাইথনে স্ট্রিংগুলি indexing করা হয়। index 0 থেকে শুরু হয়।

word = "Python"

print(word[0]) # P 

print(word[3]) # h

4. String Slicing

একটি স্ট্রিংয়ের একটি নির্দিষ্ট অংশ পেতে স্লাইসিং ব্যবহার করা হয়। String শুরু হয় [start : end : step] দিয়ে. 

text = "Python Programming"

print(text[0:6]) # Python

print(text[7:]) # Programming 

print(text[-3:]) # ing 

print(text[::-1] # String reverse 

print(text[:-1] # last letter access

5. String Method

পাইথন এর অনেক বিল্ট-ইন স্ট্রিং Method আছে। তার মধ্যে spilt(), strip(), join(), replace(), upper(), lower(), capitalize(), title(),find(), index(), isaplha(), isdigit(), isalnum() অন্যতম। 


ext = "hello world"

print(text.upper()) # HELLO WORLD 

print(text.capitalize()) # Hello world 

print(text.replace("world","Python")) 

print(text.split())

6. string length

len() ব্যবহার করে একটি স্ট্রিং এর দৈর্ঘ্য খুঁজে বের করা যায়।

text = "Python" 

print(len(text)) # 6

7. String Formatting

একটা string কে কত সুন্দর করে প্রকাশ করতে চাই সেটা formatting string দিয়ে প্রকাশ করে।

name = "Nahid" age = 25
print(f"My name is {name} and I am {age} years old.")
