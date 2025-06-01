---
title: Discussing Programming Languages
date: 2025-03-12 10:30:00
tags: programming languages, libra, C#, virtual machine
---

"There are two types of programming languages, does everyone complain about, and the ones no one use"

I guess this is true in a way, so I kind of decided to build my own (and it was a crazy idea). It all started in
2023, when I was curious about how programming languages worked, It seemed like magic at that time.

So I developed a small interpreted language called SPL (Simple Programming Language, lol). It was like 1am when
I started the project, and I finished it about 2 hours later because I realised it was already 3am and I needed to sleep.

I must say I learned a thing or two about interpreters and how languages were made, but I implemented it reading the source code
character by character, without even using a Lexer/Tokenizer, it was a mess.

`print "Hello, World!";`<br>
`set x 10;`<br>
`set y 20;`<br>
`print sum x y; // 10+20`<br>

Yeah, not that impressive...

So almost a year later, in University this time, I had a presentation to make, we could choose the topics we're gonna present.
I decided to talk about how programming languages worked under the hood, but I wouldn't stop there, I wanted to create a new 
programming language and showcase it at the presentation.

The idea was to create a programming language with It's syntax entirely in portuguese, basically a portuguese version of Lua (which was also
made by brazilians). The language would be used to teach programming to portuguese speakers in a easier way, instead of conventional languages in english
and full of symbols like semicolons and braces.

`funcao soma(a, b)`<br>
`    retornar a+b`<br>
`fim`<br>
`exibir(soma(1,2))`<br>

This basically creates a function that returns the sum of two numbers, cool.

Well, I won't talk much about it, because the language It's in portuguese, but It's getting pretty advanced tho, it has
classes, methods, functions, variables and constants, and even a standard library.

But I'm planning on developing other languages, I have an idea for a Stack Based Virtual Machine, the portuguese one is a Tree-Walker Interpreter, so It's not
very fast.

I learned a lot by implementing these languages, now I'm reading the Crafting Interpreters book, It is a incredible resource to learn.

## Links
<a href="https://github.com/lucasdcampos/spl/">https://github.com/lucasdcampos/spl/</a>

<a href="https://github.com/lucasdcampos/spl/">https://github.com/lucasdcampos/libra/</a>

<a href="https://github.com/lucasdcampos/spl/">https://craftinginterpreters.com/</a>