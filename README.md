# phonenumber-words


## phonenumber-words.py has the following functions:

● number_to_words(), which takes as an argument a string representing a US phone number and which outputs a string which has transformed part or all of the phone number into a single "wordified" phone number that can be typed on a US telephone (for example, a valid output of number_to_words("1-800-724-6837") could be "1-800-PAINTER"). Use an English dictionary of your choosing.

● words_to_number(), which does the reverse of the above function (for example, the output of words_to_number("1-800-PAINTER") should be "1-800-724-6837")

● all_wordifications(), which outputs all possible combinations of numbers and English words in a given phone number.("1-800-724-6837") could be "1-800-PAINTER", “1-800-PAIN-837”,”1-800-PAINT-37”, “1-800-72-HOT-37” and possibly others... 
In addition to the main .py file this repo contains Jupyter notebook which has some additional information: usage examples, additional comments, etc.  
  
Notes: 

The script utilises scrabble dictionary. It has a good collection of words in uppercase letters as the requirement.<br />
Regular expression operations (re) is a library used for string operations

Usage: 

1. number_to_words(number, vocab, min_len=1)<br />
  Inputs <br />
   number(string) : phone number<br />
   vocab(dict) : It is a dictionary container storing all the words from the scrabble txt file.<br />
   min_len(int) : Minimum length of a substrict to be considered as a word<br />
  Output<br />
   ans (strig) : Largest valid word possible is replaced in the phone number <br />


2. words_to_number(number)<br />
  Input <br />
   number(string) : phone number<br />
  Output<br />
   ans (string) : numerified version of phone number<br />


3. all_wordification(number, vocab, min_len=1)<br />
  Inputs<br />
   number(string) : phone number<br />
   vocab(dict) : It is a dictionary container storing all the words from the scrabble txt file<br />
   min_len(int) : Minimum length of a substrict to be considered as a word<br />
  Output <br />
   ans (set) : A set of all possible wordified phone numbers(string) is given in a set
   
 Credits : <br />
  Referred https://github.com/zarp/phonewords for usage of re functionalities
