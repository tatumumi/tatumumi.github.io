---
layout: essay
type: essay
title: "AI is the New Calculator"
# All dates must be YYYY-MM-DD format!
date: 2023-11-20
published: true
labels:
  - AI in education
  - Software Engineering
  
---
<img width="600px" alt="photo" class="text-center p-4" src="../img/AI_photo.jpeg">

## Introduction
### AI is the New Calculator

Some have compared the use of AI in education to the use of a calculator in a classroom. Before calculators, people solved math problems either by hand or using devices, like an Abacus, Mechanical Slide Rule, and Napier's Bones. The process of solving an equation during this time was undoubtedly more cumbersome than using a calculator. For example, a complex math expression can be solved in seconds today using a calculator but would take minutes to hours without one.

The benefits of using a calculator on a math problem parallel using AI to tackle any sort of problem today. Whether you are using AI to solve a math problem or even just answer a simple question, it provides you with an answer in seconds. In software engineering, AI can be especially useful. AI tools allow anyone to write programs, understand existing ones, debug their code, and many other things.

### AI in Education

The introduction of a new technology into society will always come with some resistance. In most of my classes, the use of AI is either highly discouraged or not allowed. In these classes, my teachers fear that the work their students turn in is not their own. However, in my ICS 314 class, the perspective on AI is more positive. Students are `free to make use of AI to inspect code, write code, explain code, and more.

## My Experience with AI

When my instructor notified my class that the use of AI was allowed and even encouraged, I was shocked. Below I describe my experience using AI (Chat GPT) in the course ICS 314 (Software Engineering I).

#### Experience WODs
Given my experience WODs were only graded upon completion I did not find myself heavily relying on AI tools to complete them. Most of the time I would try to complete the WOD as best as I could once (using AI if needed), reference the instructional video, and then try again. For some experiences, however, I did find AI to be very useful to write simple bulk code.

#### In-class Practice WODs
I found AI to be most useful in practice WODs when trying to debug my code. The goal of practice WODs is to help prepare students for their in-class WODs, so I tried to take these as seriously as possible. That said for these experiences I would attempt to do the WOD on my own, without help, and use AI for debugging purposes. To debug my code, I would ask Chat GPT to fix any logical/semantic errors in the section of code I specified.

#### In-class WODs
In-class WODs are the most stressful part of this course. Students must complete certain tasks in a limited amount of time, for a grade. Having AI as a supportive tool during these WODs took some of the pressure off of my shoulders. I found AI to be extremely useful when I had an error (logical or semantic) and I could not find its source or write bulk code that I could alter.

#### Essays
For technical essays, I did not find any use in referencing an AI. Writing a technical essay is a creative effort and involves my experience. That said, I do not trust an AI to write from my experience or carry my opinions.

#### Final project
AI tools offer the most help when you give it all the information it needs to understand the problem completely. For my final project, my group and I used various components to build an application (Meteor, React, Bootstrap, and MongoDB), which made the app very complicated. Unless I were to give Chat GPT all of the files/information it needed to answer my question, it couldn't give me a valuable response. Therefore, I did not find AI tools to be very informative when working on my final project, rather old code provided the most help.
#### Learning a concept/tutorial
AI tools can be very useful to help simplify a very complex concept into words a student can understand. For example, in some of my other classes, I will use Chat GPT to break up a complicated problem into its components so I can understand how to solve it. I did not have to utilize AI to learn concepts in my ICS 314 class, but I found it useful in others.
#### Answering a question in class or in Discord
When I have a question I try my best to first answer it on my own using documentation or AI tools, and ask others as a last resort. So I have found use in AI tools when I have a simple question that usually involves a single file. However, when my questions involve multiple files AI tools become less useful.
#### Asking or answering a smart-question
I have never asked or answered a smart-question on Discord before in ICS 314, so I can offer no personal experience on the use of AI here. By observing the types of questions asked in Discord, I do not think AI would be useful in answering these kinds of questions. This is due to the fact most of the questions asked relate to errors in the instructions given for an assignment or the way one has configured their computer. The best answers for these inquiries come from instructors or other students who have encountered the same problem.
#### Coding example
In my experience, Chat GPT was very useful when writing bulk code that I could alter to what I wanted to do. For example, I could ask GPT to "give me code for an example form using Meteor react bootstrap" and I would get back an outline of what a form should look like.
```
import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';
import { Envelope, Person } from 'react-bootstrap-icons';

const SimpleForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
    // Add your form submission logic here
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formName">
        <Form.Label>Name</Form.Label>
        <Form.Control
          type="text"
          placeholder="Enter your name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <Person className="mt-2" />
      </Form.Group>

      <Form.Group controlId="formEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter your email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <Envelope className="mt-2" />
      </Form.Group>

      <Form.Group controlId="formMessage">
        <Form.Label>Message</Form.Label>
        <Form.Control
          as="textarea"
          rows={4}
          placeholder="Enter your message"
          name="message"
          value={formData.message}
          onChange={handleChange}
          required
        />
      </Form.Group>

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};

export default SimpleForm;
```
I could then edit this form to have the functionality I want, but the bulk of the code is already written. This example does not reflect exactly the code I asked Chat GPT to write, but it demonstrates how AI can be used to write long blocks of code to save time.
#### Explaining code
Most of the time when I'm programming I am at home away from my professors and peers. So when I had questions about the instructions of an assignment or about a segment of code, Chat GPT was very helpful. I found it able to simplify and summarize complex segments of code in a way where I can better understand it.
#### Writing code
Writing code is one of the most useful aspects of using an AI tool. When enough information was provided, Chat GPT was able to write very efficient and readable code. However, the accuracy of the code it would give me was dependent on how specific I would make my instructions. For example, if I were to give Chat GPT an open-ended question like, "Give me code for a function in JavaScript", then the response would not necessarily be the function I was looking for.
```
function calculateRectangleArea(length, width) {
    // Calculate the area of the rectangle
    var area = length * width;
    return area;
}
// Example usage:
var length = 5.0;
var width = 3.0;
var result = calculateRectangleArea(length, width);
console.log("The area of the rectangle with length " + length + " and width " + width + " is: " + result);
```
Rather if I provide a specific prompt like, "Give me a function to find the volume of a cube and takes in 1 parameter in JavaScript", the response follows exactly what I asked for.

```
function calculateCubeVolume(sideLength) {
    // Calculate the volume of the cube
    var volume = Math.pow(sideLength, 3);
    return volume;
}

// Example usage:
var sideLength = 4.0;
var result = calculateCubeVolume(sideLength);
console.log("The volume of the cube with side length " + sideLength + " is: " + result);
```

#### Documenting code
I did not find any use in AI for documenting code. However, I suspect AI tools would be very useful in this area.
#### Quality assurance
Sometimes the code I write is not very efficient and can be quite wordy. Every so often I will ask Chat GPT to simplify or condense my code. The response I receive is usually helpful and can even make my code more efficient.

## Impact on Learning and Understanding
Overall I do not think that my use of AI has hindered my learning in any way. Chat GPT proved to be a helpful tool in almost every aspect of ICS 314. Seeing how the AI broke up problems into subtasks and organized its code taught me how to approach difficult coding problems. The code explanations it would give me helped me understand what I was or was being asked to do better.
## Practical Applications
AI is not only used for educational purposes but for various practical ones as well,
- Personalized Shopping
- AI-Powered Assistants
- Fraud Prevention
- Autonomous Vehicles
- Spam Filters
- Facial Recognition
- Recommendation System
- etc.

The intention of including AI in each of these applications is to improve the experience of users/ customers. However, there is a downside to the use of AI too.


As exciting and innovative as the use of AI is in these areas, it can be kind of scary or unreliable. Facial recognition technology is a great example of where AI can go wrong. For example, security breaches with facial recognition can increase the risk of identity theft, stalking, and harassment.

## Challenges and Opportunities
While I have found AI to be very helpful for ICS 314 I do wish it had better accuracy. Sometimes I found myself spending more time telling Chat GPT what to do than it would take me to do it myself. A good analogy for this is the time difference between solving a problem and trying to teach someone how to solve it for you, it takes way longer. I have also experienced challenges getting valuable responses from AI for other courses. For example, if I give the AI a mathematical expression to solve, it will sometimes make up random numbers which throws off the answer. The final challenge I faced, and probably the largest one, was a moral challenge. I would be lying if I said I didn't feel guilty when I was using Chat GPT to solve a problem. In academia, it has always been frowned upon to look up the answers and AI does just this. I have not yet been able to get over this guilt I have using AI, but I hope that over time using AI will become more normalized so I don't feel this way.


Despite the challenges I experienced using AI, I do think that it can be very valuable in software engineering education. I think using AI to summarize or explain complicated instructions and code can be very useful. In this way, students can check or aid their understanding of the material without asking their professor or TA.


## Comparative Analysis
The teaching method that was adapted for my ICS 314 course focuses on practicing athletic software engineering. For this teaching methodology, students are required to read articles/documentation and then complete work-out-of-the-days or WODs. This forces students to constantly practice skills so that they become second nature. AI poses a small threat to this methodology because if AI can give you the answers then why practice? Students may feel as if they don't have to read the documentation or repeat as many WODs as they should because they will have AI to help them.

## Future Considerations
An issue I experienced with AI is that I would have to give very specific instructions with sometimes multiple pages of code to get a decent answer. A possible solution is to be able to upload multiple files of code to an AI so it can produce a valuable response.
## Conclusion
AI is here and will probably never go away, so we have to adjust. My experience with AI in ICS 314 was very positive and I would recommend others to utilize it as well. However, I do think that there should be guidelines or rules set in place regarding its usage. For example, referencing AI for comprehension rather than for writing code may be more beneficial for a student long term.
