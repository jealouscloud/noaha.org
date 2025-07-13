---
display: false
---


Semantics and Typography
========================

An Introduction
---------------

This little baseline has ( almost) all of the content flow and phrasing elements. It attempts to use all of those elements according to their defined semantics. It also tries to provide a baseline style for those elements. So this isn't a normalize or a reset, but maybe the first set of styles you'd add before you start branding stuff. Here is the [full list of the elements](https://www.w3.org/TR/html5/).

There's also a [Form Baseline](https://codepen.io/paceaux/pen/mdmBPPx) and a [Table baseline](https://codepen.io/paceaux/pen/KKWwyMa) if that's more of your thing.

Here is a collection of headings
================================

The subheading that should tell you more about it
-------------------------------------------------

### The heading that (probably) explains sections of content

#### The First unimportant heading

##### The Second Unimportant heading

###### The Heading for pedants

* * * * *

### Paragraphs and Styles

#### Text Level Semantics

I'm that paragraph with some *emphasis on the text-level semantics*where I might feel the need to **share some strong opinions**. This paragraph even uses elements that should have been deprecated, but instead the W3C redefined them. And that's dumb, because formerly presentational elements now do silly things like call a thing to your **attention** for no good reason, or tell you that something is mispelled, or the name of a boat --- which makes as much sense as building another *Titanic*. It makes no sense, but ... *c'est la vie*.

#### Editing semantics

This paragraph is all about editing my opinions. Sometimes I have opinions ~~that are no longer relevant~~. Sometimes I mark or highlightsome text so that people notice it. Sometimes I insert some thoughts later. Sometimes I ~~delete those thoughts~~. The user can also select text, so it's important to be sure that the user can discern whether I've highlighted something, or they have.

#### Definitions

The whole point of this paragraph is meaning. Sometimes we need an explanation, or a definition . For those times, you have an element that you can use to tell the user that one word in this paragraph is the term that the paragraph is actually explaining.

Sometimes, we have to define an abbreviation. Take, LASER, which is an acronym for Light Amplification by Stimulated Emition of Radiation. The abbreviation tags don't make much sense unless they have a title, though.

You know what time it is? No, not Howdy-Doody time. It's April 29, 2016.

* * * * *

### Quoting, Citing, scripting

You know how you're saying something, and then you just feel the need to make quick quote, like Hey, I totally want to buy Somnaderpaphil LG for my herpes? But after some reading,you see that small print that says it can give 1 out of 2 users irritable bowel syndrome. Then you read all of scientific things ~(1/0)~or citations ^1^that make you feel better.

> Go, Blockquote. Quote away. Be the blockquote you've always wanted to be. But within reason. Also, don't forget who made you... *The Dude who spoke you into existence*

* * * * *

### Code Semantics

Writing code is hard. You have stuff like variables. Imagine *n*is a variable. Maybe you have some code, like `n = 1`. Now you want to increment it with your `+`on the keyboard, so the result is a sample (e.g.`n == 2`). And maybe there's data, where maybe the browser needs an internal value, but the user needs to see something friendly.

<p> Writing code is hard. You have stuff like variables. Imagine where <var> n</var> is a variable. <br /> Maybe you have some code, like <code> n = 1</code>. Now you want to increment it with your <kbd>+</kbd> on the keyboard, so the result is a sample (e.g.<samp> n == 2</samp>).

</p>

* * * * *

### List semantics

1.  The first item in an ordered list
2.  The second item in an ordered list

-   I am a humble list item, I don't care if I'm first
-   I am a second humble list item, put me wherever yo!

-   [See the Typography Baseline](https://github.com/paceaux/typography-baseline)-   [Look at the Form Baseline](https://github.com/paceaux/form-baseline)-   [Review the Table Baseline](https://github.com/paceaux/table-baseline)

ordered list

a list with numbers, where the items need to be in a particular order

unordered list

a list with bullets or some other indicator, where the items can be in any order

menu

An unordered list with interactive items or commands that the user can use.

definition list

The forgotten list. It has definition terms,`<dt>`and definitions `<dd>`. It's pretty much perfect for listing out the kinds of lists in a subtle, 4th wall-breaking kind of way.

* * * * *

### Language Semantics

Then there's that text where you need to show it in a different language. Like, say you want to know my name, but you speak Korean better than English. Well, I'd tell you my name is Frank 퍼랜케and I hope you'd know how to pronounce it.

Sometimes, though, you need to show something in a semitic language. Maybe you want to say Shalom שלוםin the homeבבית.That's totally fine, just remember that text runs in the opposite direction in Arabic, Farsi, and Hebrew.

With Semitic Languages, though, you need to flip the order of some things. Say you're reading some text like, אני אוהב את ייןand it translates as `Ilikewine`. You have to remember that there's an element for saying a block of text is written in reverse, and another for saying a span of text should be the reverse of its parent.

Another way to understand that text is to look at the word-for-word translation: