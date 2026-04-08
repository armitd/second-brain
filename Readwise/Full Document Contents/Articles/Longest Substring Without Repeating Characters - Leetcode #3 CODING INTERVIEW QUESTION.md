# Longest Substring Without Repeating Characters - Leetcode #3 | CODING INTERVIEW QUESTION

![rw-book-cover](https://i.ytimg.com/vi/8UthLlvh0gM/maxresdefault.jpg)

## Metadata
- Author: [[WeAreTechies]]
- Full Title: Longest Substring Without Repeating Characters - Leetcode #3 | CODING INTERVIEW QUESTION
- Category: #articles
- Document Tags: [[ifttt]] [[twitter]] 
- Summary: The video explains how to solve the Leetcode problem of finding the length of the longest substring without repeating characters. It uses a sliding window approach with two pointers to track unique characters in the substring. The method involves adding characters to a set and adjusting the pointers when duplicates are found.
- URL: https://www.youtube.com/watch?v=8UthLlvh0gM&feature=youtu.be

## Full Document
hey folks this is praveen and today we're gonna see the another lead code problem longest substring without repeating character so problem statement says given a string s find the length of the longest sub string without repeating characters so here if we see the first example we have got the string a b c a b c b b and the output is three and the reason is 

if we see any sub this string with the non-repeating character the length is the longest length is three so abc it will include a there would be two a so will not include a here we'll check the another substring b c a here again the sub string length is three if we'll include b then we'll be having two substring the another example says here b b b b so here five time b's are there and uh as we know we can only create a 

sub string with one length uh here we have got this string and here also the answer is coming three because the longest sub string is w k e um without uh non repeating characters and if we don't get anything or we'll get the null we can have zero as the response so okay this is the problem to solve this problem we'll gonna use this sliding window approach 

so how this sliding window approach will gonna work let's try to understand this by this example i'll keep two pointer left pointer and the right pointer and also i'll have one set where we're gonna store the unique characters value so initially both left and right pointer will point to the same position and then we'll keep incrementing our right pointer by one position until we'll get the repeating character 

so here initially we'll be having a b and c in our set as soon as we'll get the a what we're gonna do we'll gonna delete the character at the earth index so here health index we are having a and we'll increment our l by one and then we'll gonna add the character so now we we don't have any repeating character in our side again we'll increase and the right point and we'll see the character at the right pointer 

and here we have the b so what we're gonna do we're gonna delete the uh uh character uh at the uh left pointer so we'll delete it and again we're gonna write the b so we'll keep doing this till the time our r will reach to the end of the string so let's write the code for this so as i mentioned we'll be having one 

right pointer i'll call it as right we'll be having the left pointer i'll call this as an l left and i'll initialize both as in zero now we need the variable to store the longest uh substring length so we'll initialize this as zero as als as i mentioned we need this side as well to keep track of the all the 

character in the sub string so we can create a set of type character and we can call it as uni 

now we have all our variable initialized and created now as i mentioned we'll have to keep increment our right pointer till the time will reach to the uh end of our string uh so when right is less than s dot length we'll run this loop now what we're gonna check we're gonna check our unique character 

set whether this contains um the uh carrot right there uh right pointers our right pointer is right okay at right so i'll say not contents if it is not there that means we have a unique value now so we will add here in our unique 

we'll simply add whatever the value is there start care caret right now we have added the value what we're gonna do we're gonna implement our right pointer now we're gonna see the next value and is this point of time will also capture the longest uh service string length so that would be mat dot 

max so we'll check whatever the current value of the longest substring we are having that is the uh the longest service string length or the current set size so whatever is the maximum will capture that if this is not true that means we already have the character which now 

our right pointer is pointing to so what we're gonna do as i mentioned we'll gonna remove the character uh the left position character so s dot cap at left so we're gonna remove the character available at the left position and we'll increment our left pointer as 

well not left pointer will also move forward to the one position now when this loop will execute completely will reach to the end of the uh string and at the end we'll return our longest service tree to a longest service string now hopefully this code should work let's run it 

ah some problem i miss dc here this goes let's submit this yep this code is working so this is how we can solve the longest 

sub string without repeating character problem if you like this video please like and subscribe to the channel thank you thank you so much for watching
