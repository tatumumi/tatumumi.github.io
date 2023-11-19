---
layout: essay
type: essay
title: "Today's Calculator is AI"
# All dates must be YYYY-MM-DD format!
date: 2023-11-20
published: true
labels:
  - AI in education
  - Software Enigneering
  
---
## Introduction
### AI the New Calculator

Some have compared the use of AI in education to the use of a calculator in a classroom. Before calculators people solved math problems either by hand or using devices, like an Abacus, Mechanical Slide Rule, and Napier's Bones. The process of solving an equation during this time was undoubtedly more cumbersome then using a calculator. For example, a complex math expression can be solved in seconds today using a calculator, but would take minutes to hours without one. 

The benefits of using a calculator on a math problem then parallels using AI to tackle any sort of problem today. Whether you are using AI to solve a math problem or even just answer a simple question, it provides you with an answer in seconds. In software engineering AI can be especially useful. AI tools allow anyone to write programs, understand existing ones, debug their code, and many other things. 

### AI in Education
    
The introduction of a new technology into society will always come with some resistance. In most of my classes the use of AI is either highly discouraged or not allowed. In these classes my teachers fear that that work their students turn in is not their own. However, in my ICS 314 class the perspective on AI is more positive. Students are `free to make use of AI to inspect code, write code, explain code, and more. 

## My Experience with AI

When my instructor notified my class that the use of AI was allowed and even encouraged I was shocked, and excited. Below I describe by experience using AI (Chat GPT) in the course ICS 314 (Software Engineering I).

#### Experience WODs
Given experience WODs were only graded upon completion I did not find myself heavily relying on AI tools to complete them. Most of the time I would try to complete the WOD as best as I could  once (using AI if needed), reference the instructional video, then try again. For some experiences, however, I did find AI to be very useful to write simple bulk code. 

#### In-class Practice WODs
I found AI to be most useful in practice WODs when trying to debug my code. The goal of practice WODs is to help prepare students for their in-class WODs, so I tried to take these as seriously as possible. That said for these experiences I would attempt to do the WOD on my own, without help, and use AI for debugging purposes. To debug my code, I would ask Chat GPT to fix any logical/semantic errors in the section of code I specified. 

#### In-class WODs
In-class WODs are the most stressful part of this course. Students must complete certain tasks in a limited amount of time, for a grade. Having AI as a supportive tool during these WODs took some of the pressure off of my shoulders. I found AI to be extremely useful when I had an error (logical or semantic) and I could not find its source or to write bulk code that I could alter 

#### Essays
For technical essays, I did not find any use in referencing an AI. Writing a technical essay is a creative effort and involves my experience. That said, I do not trust an AI to write from my experience or carry my opinions. 

#### Final project
AI tools offer the most help when you give it all the information it needs to understand the problem completely. For my final project, my group and I were using various components to build an application (Meteor, React, Bootstrap, and MongoDB), which makes the app very complicated. Unless I were to give Chat GPT all of the files/information it needed to answer my question, it couldn't give me a valuable response. Therefore, I did not find AI tools to be very informative when working on my final project rather old code provided the most help. 
#### Learning a concept / tutorial
AI tools can be very useful to help simplify a very complex concept into words a student can understand. For example, in some of my other classes I will use Chat GPT to break up a complicated problem into its components so I can understand how to solve it. I did not have to utilize AI to learn concepts in my ICS 314 class, but I found it useful in others. 
#### Answering a question in class or in Discord
When I have a question I try my best to first answer it on my own using documentation or AI tools, and ask others as a last resort. So I have found use in AI tools when I have a simple question that usually involves a single file. However, when my questions involves multiple files AI tools become less useful. 
#### Asking or answering a smart-question
I have never asked or answered a smart-question on the Discord before in ICS 314, so I can offer no personal experience on the use of AI here. By observation of the types of questions asked in Discord, I do not think AI would be useful in answering these kinds of questions. This is due to the fact most of the questions asked relate to errors in the instructions given for an assignment or the way one has configured their computer. The best answers for these inquires come from instructors or other student who have encountered the same problem. 
#### Coding example
In my experience, Chat GPT was very useful when writing bulk code that I could alter to what I wanted to do. For example, I could ask GPT to "give me code for an example form using meteor react bootstrap" and I would get back an outline of what a form should look like.
```import React, { useState } from 'react';
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
Most of the time I spent working on assignment/writing code was at home, away from class. So if I did not understand  
#### Writing code
#### Documenting code
#### Quality assurance
#### Other uses in ICS 314 not listed

## Impact on Learning and Understanding

## Practical Applications

## Challenges and Opportunities

## Comparative Analysis

## Future Considerations

## Conclusion

