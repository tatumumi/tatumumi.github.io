---
layout: essay
type: essay
title: "Patterns that Govern Us"
# All dates must be YYYY-MM-DD format!
date: 2023-11-29
published: true
labels:
  - Design Patterns
  - Software Engineering
  
---
<img width="600px" alt="photo" class="text-center p-4" src="../img/design.png">

A design pattern "describes a problem that occurs over and over again in our environment, and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over, without ever doing it the same way twice" - Christopher Alexander, 1977

# Design Patterns

In software engineering, a design pattern is meant to explain a general design solution to a recurring design problem in object-oriented programming. It identifies the design issue, its solution, when it's needed, and its consequences. These patterns are well-tested design paradigms meant to speed up the development process, and make code more reusable/flexible.

More generally we can think of a design pattern as a template or guide to doing something in the most efficient way possible. A real-world analogy (outside of software engineering) of a design pattern, is news subscription. When one subscribes to the news, they and all the other subscribers are notified whenever the news publishes something. This is analogous to the Observer pattern (or the Publish/Subscribe pattern). In the Observer Pattern, a class will hold a list of observers and when it wants to broadcast something, it calls upon a method on all observers.

## Types of Design Patterns
There are three main types of design patterns: creational, structural, and behavioral design patterns.

### 1. Creational Design Patterns
These patterns focus on class instantiation or object creation. They can be broken into two categories, class-creation patterns or object-creation patterns. Creational design patterns include Factory Method, Abstract Factory, Builder, Singleton, Object Pool, and Prototype.

### 2. Structural Design Patterns
These patterns organize different classes and objects to create larger structures with new functionality. They aim to optimize the functionality of the classes involved without heavily altering their composition. Structural design patterns include Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Private Class Data, and Proxy.

### 3. Behavioral Design Patterns
These patterns identify common communication patterns amongst objects. Behavioral design patterns include Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Null, Object, Observer, State, Strategy, Template method, and Visitor.

# My Experience Using Design Patterns
My use of design patterns has been quite trivial. After looking into what design patterns are and which ones are out there, I realized I have been using them since the beginning of my ICS 314 course. For example, in the first couple weeks of ICS 314, we learned how to code in JavaScript. In JavaScript, the Prototype pattern is a fundamental concept and is frequently used. When using the Prototype pattern, objects are cloned instead of creating new ones with a constructor. [JavaScript](https://www.javascript.com/) follows this pattern with prototype inheritance, where objects inherit properties and methods from other objects. The use of this pattern minimizes the complexity of object creation in JavaScript. Another design pattern I used was the Observer pattern, specifically when using [Meteor](https://guide.meteor.com/v1.3/structure.html). The Observer design pattern maintains and defines a dependency between objects. A simple example of the Observer pattern is Model/View/Controller, in this example the views are observers of the model and are notified when the model's state changes. Meteor uses this design pattern because it is built on the principles of reactivity and automation. For example, in various coding exercises, I would use Meteor to automatically update the user interface in response to changes in data. Some other design patterns that I have used in my code include the Front Controller (with Mongo DB), Singleton (using Collections), and Factory (define () methods).

Overall I think design patterns are an extremely useful tool and are somewhat already ingrained into society. Outside of software engineering, they allow us to live practical and productive lives. In software engineering, they help us write code faster and more efficiently. 
