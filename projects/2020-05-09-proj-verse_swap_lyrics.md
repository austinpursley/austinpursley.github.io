---
layout: post
title: "Song Lyrics Phoneme Swap"
tags: project
---



 Given a line of a famous song:




{% highlight python linenos %}
"Fly me to the moon"
{% endhighlight %}


 We can find the phonemes for the words with
 [CMUdict](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) 
 :




{% highlight python linenos %}
['F L AY1', 'M IY1', 'T UW1', 'DH AH0', 'M UW1 N']
{% endhighlight %}


 Define some new word boundaries (in this case merging two words into one, however more combos are possible):




{% highlight python linenos %}
['F L AY1', 'M IY1 T UW1', 'DH AH0', 'M UW1 N']
{% endhighlight %}


 Replace some of the phonemes with
 [regex](https://en.wikipedia.org/wiki/Regular_expression) 
 wildcards...




{% highlight python linenos %}
['F .{1,3} .{1,3}', '.{1,3} .{1,3} V Y UW1', 'T UW1', 'M .{1,3} N']
{% endhighlight %}


 ...then search for new words that match the pattern:




{% highlight python linenos %}
['F AH1 N D', 'R IY2 V Y UW1', 'T UW1', 'M EY1 N']
{% endhighlight %}


{% highlight python linenos %}
"Fund review to main"
{% endhighlight %}


 (it can take awhile to find a combo of word boundaries and wildcards that works)




 And there you go, the line has had some of its phonemes swapped. To continue the fun, we can do some more lines from the song:




{% highlight python linenos %}

	Let me play among the stars
	['L EH1 T', 'M IY1', 'P L EY1', 'AH0 M AH1 NG', 'DH AH0', 'S T AA1 R Z']
	letter multiple trademarks
	['L EH1 T ER0', 'M AH1 L T AH0 P AH0 L', 'T R EY1 D M AA2 R K S']
	
	And let me see
	['AH0 N D', 'L EH1 T', 'M IY1', 'S IY1']
	and hot tv
	['AH0 N D', 'HH AA1 T', 'T IY1 V IY1']

	what spring is like
	['W AH1 T', 'S P R IH1 NG', 'IH1 Z', 'L AY1 K']
	arts print him like
	['AA1 R T S', 'P R IH1 N T', 'HH IH1 M', 'L AY1 K']

	On a Jupiter and Mars
	['AA1 N', 'AH0', 'JH UW1 P AH0 T ER0', 'AH0 N D', 'M AA1 R Z']
	august open the ads free
	['AA1 G AH0 S T', 'OW1 P AH0 N', 'DH AH0', 'AE1 D Z', 'F R IY1']	
	
{% endhighlight %}


 More examples:




{% highlight python linenos %}

	Boulder colorado
	Take a break at Yaddo*
	Economics
	Put it in my pocket
	(*not in CMUdict, input "Yah doe" instead)
	
	culture girl around oh
	too country key window
	end a techniques
	pay town interest diet
	
{% endhighlight %}


{% highlight python linenos %}

	A B C
	It's easy as, 1 2 3
	As simple as, do re mi
	A B C, 1 2 3
	Baby, you and me girl

	agree see
	it jersey an, UK lee
	desktop oil as, poor army
	agree see, UK lee
	job few a procedures
	
{% endhighlight %}


{% highlight python linenos %}

	Amarillo by morning
	Up from San Antone
	Everything that I've got
	Is just what I've got on

	power al oh regarding
	appear advanced show now
	of re things archives at
	inc ice two style root on
	
{% endhighlight %}


 See
 [GitHub](https://github.com/austinpursley/verse-python/blob/master/swap_lyrics.py) 
 for related code.



