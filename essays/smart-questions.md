---
layout: essay
type: essay
title: "Good Questions Attract Good Answers"
# All dates must be YYYY-MM-DD format!
date: 2023-09-05
published: true
labels:
  - Questions
  - Answers!
  - StackOverflow
---

<img width="400px" class="rounded float-start pe-4" src="../img/question.png">

## What makes a "good" question in software engineering?

One of a student's worst fears is asking their professor a question, just to be reminded that their question was "ignorant" or "lazy". Even as a senior in college, I am afraid of looking "unintelligent" to my peers and mentors. This fear I have causes me to "think before I speak" or "think before I ask". 

The idea of formulating a clear, intelligent, and confident question before asking someone is heavily encouraged in software engineering. Asking "good" or "smart" questions on appropriate forums can lead to more insightful and helpful answers from tech professionals. Questions that are regarded as "good" are characterized by:

- meaningful subject-specific headers
- grammatically sound
- a clear description of the problem (in chronological order)
- concise
- respectful
- etc.

In addition to forming a "good" question, it is important to choose an effective forum to ask it. Depending on the subject matter of the question it should or should not be posted on a specific forum. For example, sites like Stack Overflow deal with programming questions. A good rule of thumb when deciding on which forum to post your question on is to look at what kind of questions have already been posted (and even at how many responses each post received).

## What is a "bad" question?

Since there are "good" questions, there must exist "bad" questions. Growing up I was led to believe that there was no such thing as a "bad" question. Any/all questions were encouraged to provoke discussion and understanding. However, when it comes to ask-and-answer forums like Stack Overflow, "bad" questions do exist. 
(When I say "bad" questions I do not necessarily mean the question is bad but rather that it is "lazy" or "inappropriate".) Questions like these usually are:

- too simple (can be looked up easily)
- too many issues/ topics brought up in one question
- disrespectful (requests "Urgent" response)
- unclear
- irrelevant to the web forum
- etc.

## Examples:

#### A "good" question:

```
Q: What is the most efficient way to deep clone an object in JavaScript?

What is the most efficient way to clone a JavaScript object? I've seen obj = eval(uneval(o)); being
used, but that's non-standard and only supported by Firefox.

I've done things like obj = JSON.parse(JSON.stringify(o)); but question the efficiency.

I've also seen recursive copying functions with various flaws.
I'm surprised no canonical solution exists.

```
[What is the most efficient way to deep clone an object in JavaScript?](https://stackoverflow.com/questions/122102/what-is-the-most-efficient-way-to-deep-clone-an-object-in-javascript)

This question is a perfect example of what tech professionals in software engineering look to answer on web forums like Stack Overflow. The question is thought-provoking and requires more thought than a simple Google search or a reference to the documentation. Its subject header is concise and summarizes the question being asked. The enquirer also gives a specific description of their problem/question and even acknowledges answers they are already aware of. We can confirm how successful this question was by looking at the number of responses it received. This question attracted a lot of attention with 67 answers and most of them being lengthy/detailed responses.  

#### A "bad" question

```
Q: what's wrong with this sql query?

Okay I have two variables in PHP
$username;
$password;

which are initialized to the data retrieved from $_POST variable :)

I have this SQL query

$sql = "SELECT * FROM users WHERE username = '" . $username . "' AND password = '" . $password . "')";
But this doesn't works and returns me nothing :(

Can you instruct me into the right direction. Please?
```
[What's wrong with this sql query?](https://stackoverflow.com/questions/782488/whats-wrong-with-this-sql-query/782499#782499)

This question provides an example of what one should not post/ask, as the enquirer should have done more prior research and reworded the question. Much of the responses to this Stack Overflow post refer the enquirer to resources and suggest they lack understanding of the subject. The question also lacks much of what a "good" question consists of. The subject header is not specific and does not indicate the problem. Additionally, the enquirer asks for instruction when alternate resources could have been used to solve their problem, as prescribed by the respondents. This question also received significantly fewer responses when compared to the "good" question, suggesting the community's disinterest.

## Conclusion
As we have seen "thinking before you ask" makes a difference when engaging with the online community. Making sure your question cannot just be answered with a Google search and then wording it in a concise, specific, and detailed manner before asking others increases your chances of getting a good response. While these guidelines for asking questions should be followed in online web forums, like Stack Overflow, they can also be used as a tool in everyday life. For example, making sure you have tried your absolute best at something before asking for help will prevent you from being viewed as lazy or ignorant. 
Lastly, not only is asking "good" questions helpful for yourself but it also positively impacts the whole online community. For example, whenever I run into issues that I have to look up online, I always look for posts that have detailed/ clear responses. The questions on these posts usually follow what we have described as a "good" question. 


