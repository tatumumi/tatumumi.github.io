---
layout: essay
type: essay
title: "Good Questions Atrract Good Answers"
# All dates must be YYYY-MM-DD format!
date: 2023-09-05
published: true
labels:
  - Questions
  - Answers 
  - StackOverflow
---

<img width="400px" class="rounded float-start pe-4" src="../img/question.png">

## What makes a "good" question in software engineering?

One of a student's worst fears is asking their professor a question, just to be reminded that their question was "ignorant" or "lazy". Even as a senior in college, I am afraid of looking "unintelligent" to my peers and mentors. This fear of mine influences me to "think before I speak" or "think before I ask". 

The idea of formulating a clear, intelligent, and confident question before asking someone is heavily encouraged in software engineering. Asking "good" or "smart" questions on appropriate forums can lead to more insightful and helpful answers from tech professionals. Questions that are regarded as "good" are characterized by:

- meaningful subject-specific headers
- grammatically sound
- a clear description of the problem (in chronological order)
- concise
- accessible
- respectful
- etc..

In addition to forming a "good" question, it is important to choose an effective forum to ask it. Depending on the subject matter of the question it should or should not be posted on a specific forum. For example, sites like Stack Overflow deal with programming questions. A good rule of thumb when deciding on which forum to post your question on is to look at what kind of questions have already been posted (and even at how many responses each post received).

## What is a "bad" question?

Since there are "good" questions, there must exist "bad" questions. Growing up I was fed the idea that there was no such thing as a "bad" question. Any/all questions were encouraged to provoke discussion and understanding. However, when it comes to ask-and-answer forums like Stack Overflow, "bad" questions do exist. 
(When I say "bad" questions I do not necessarily mean bad rather that the question is bad but "lazy" or "inappropriate".) Questions like these usually are:

- too simple (can be looked up easily)
- too lengthy
- disrespctful (requests "Urgent" response)
- unclear
- irrelevant to the web forum
- etc..

## Examples:

### A "good" question:

```
Q: What is the most efficient way to deep clone an object in JavaScript?

What is the most efficient way to clone a JavaScript object? I've seen obj = eval(uneval(o));
being used, but that's non-standard and only supported by Firefox.

I've done things like obj = JSON.parse(JSON.stringify(o)); but question the efficiency.
I've also seen recursive copying functions with various flaws.

I'm surprised no canonical solution exists.

```

While the heading of his question could be better, it does convey what he’s trying to figure out. Usually something as brief as “python date of previous month” is what other users would enter in as search terms on Google, making it easily found. Another good thing about the question is that it’s not just a question. The asker shows what he or she has done and that he or she has put in some effort to answer the question. And while it may not be as important as the question itself, the asker shows courtesy, which does increase the chance of getting an answer.

```
A: datetime and the datetime.timedelta classes are your friend.

1. find today
2. use that to find the first day of this month.
3. use timedelta to backup a single day, to the last day of the previous month.
4. print the YYYYMM string you're looking for.

Like this:

 >>> import datetime
 >>> today = datetime.date.today()
 >>> first = datetime.date(day=1, month=today.month, year=today.year)
 >>> lastMonth = first - datetime.timedelta(days=1)
 >>> print lastMonth.strftime("%Y%m")
 201202
 >>>

```
 
The asker received six possible answers, and he or she was successful in inciting discussion from multiple users. The answers themselves were clear and were devoid of the rumored sarcasm and hostility of “hackers.” Since I myself have referenced this page and found it useful, I can confidently say that it is a good question.

## The foolproof way to get ignored.

While there are decent questions that benefit everyone, there are those one can ask to create an entirely different effect. In the following example, a user asks how he would, in short, create a desktop application with Facebook.

```
Q: Facebook Desktop Notifier

I am a beginner programmer that have never used anything other than what's included in a language.

I am trying to create a desktop application that notifies me anytime I get an update onfacebook. 
How should go about doing this? Thanks in advance.

edit Sorry I was not clear. Is there any way to make a DESKTOP application with facebook?
```

A simple “yes” would have answered the question, but we know that’s not the sort of answer he or she is looking for. Fortunately, someone kindly responded with a link to Facebook’s developer website. The asker should have done more research on his or her potential project. Then further down the road, he or she could have asked more specific and detailed questions that wouldn’t require a thousand-paged response for a sufficient answer.

## Conclusion

When we rely on others’ generosity and expertise to provide answers to our questions, it should hold that the question we ask should be one that leads to efficient and effective help that not only benefits us, but also the people we ask and others who might ask the same question in the future. Thus, if you have a question… make it a smart one! Asking questions may not always get you the best answer, but asking them in a way that will make others want to answer them will increase the success of finding a good solution and make it a positive experience on all sides.
