import html_compose as ht

from .. import models
from . import blog, common


def demo():
    return ht.div()[
        ht.section()[
            ht.h1()["Semantics and Typography"],
            ht.h2()["An Introduction "],
            ht.p()[
                "This little baseline has ( almost) all of the content flow and phrasing elements. It attempts to use all of those elements according to their defined semantics. It also tries to provide a baseline style for those elements. So this isn't a normalize or a reset, but maybe the first set of styles you'd add before you start branding stuff. Here is the ",
                ht.a(href="https://www.w3.org/TR/html5/")[
                    "full list of the elements"
                ],
                ". ",
            ],
            ht.p()[
                "There's also a ",
                ht.a(href="https://codepen.io/paceaux/pen/mdmBPPx")[
                    "Form Baseline"
                ],
                "and a ",
                ht.a(href="https://codepen.io/paceaux/pen/KKWwyMa")[
                    "Table baseline"
                ],
                "if that's more of your thing. ",
            ],
        ],
        ht.section()[
            ht.h1()["Here is a collection of headings "],
            ht.h2()["The subheading that should tell you more about it"],
            ht.h3()["The heading that (probably) explains sections of content"],
            ht.h4()["The First unimportant heading"],
            ht.h5()["The Second Unimportant heading"],
            ht.h6()["The Heading for pedants"],
        ],
        ht.hr(),
        ht.h3()["Paragraphs and Styles"],
        ht.h4()["Text Level Semantics"],
        ht.p()[
            "I'm that paragraph with some ",
            ht.em()["emphasis on the text-level semantics"],
            "where I might feel the need to ",
            ht.strong()["share some strong opinions"],
            ". This paragraph even uses elements that should have been deprecated, but instead the W3C redefined them. And that's dumb, because formerly presentational elements now do silly things like call a thing to your ",
            ht.b()["attention"],
            "for no good reason, or tell you that something is ",
            ht.u()["mispelled"],
            ", or the name of a boat — which makes as much sense as building another ",
            ht.i()["Titanic"],
            ". It makes no sense, but … ",
            ht.i()["c'est la vie"],
            ". ",
        ],
        ht.h4()["Editing semantics"],
        ht.p()[
            "This paragraph is all about editing my opinions. Sometimes I have opinions ",
            ht.s()["that are no longer relevant"],
            ". Sometimes I ",
            ht.mark()["mark or highlight"],
            "some text so that people notice it. ",
            ht.ins()["Sometimes I insert some thoughts later"],
            ". Sometimes I ",
            ht.del_()["delete those thoughts"],
            ". The user can also select text, so it's important to be sure that the user can discern whether I've highlighted something, or they have. ",
        ],
        ht.h4()["Definitions"],
        ht.p()[
            "The whole point of this paragraph is meaning. Sometimes we need an explanation, or a ",
            ht.dfn(title="Definition")["definition "],
            ". For those times, you have an element that you can use to tell the user that one word in this paragraph is the term that the paragraph is actually explaining. ",
        ],
        ht.p()[
            "Sometimes, we have to define an abbreviation. Take, ",
            ht.dfn()[
                ht.abbr(
                    title="Light Amplification by Stimulated Emition of Radiation"
                )["LASER"]
            ],
            ", which is an acronym for Light Amplification by Stimulated Emition of Radiation. The abbreviation tags don't make much sense unless they have a title, though. ",
        ],
        ht.p()[
            "You know what time it is? No, not Howdy-Doody time. It's ",
            ht.time()["April 29, 2016"],
            ". ",
        ],
        ht.hr(),
        ht.h3()["Quoting, Citing, scripting"],
        ht.p()[
            "You know how you're saying something, and then you just feel the need to make quick quote, like ",
            ht.q()[
                "Hey, I totally want to buy Somnaderpaphil LG for my herpes"
            ],
            "? But after some reading,you see that small print that says ",
            ht.small()["it can give 1 out of 2 users irritable bowel syndrome"],
            ". Then you read all of scientific things ",
            ht.sub()["(1/0)"],
            "or citations ",
            ht.sup()["1"],
            "that make you feel better. ",
        ],
        ht.blockquote()[
            "Go, Blockquote. Quote away. Be the blockquote you've always wanted to be. But within reason. Also, don't forget who made you... ",
            ht.cite()["The Dude who spoke you into existence"],
        ],
        ht.hr(),
        ht.h3()["Code Semantics"],
        ht.p()[
            "Writing code is hard. You have stuff like variables. Imagine ",
            ht.var()["n"],
            "is a variable. ",
            ht.wbr(),
            "Maybe you have some code, like ",
            ht.code()["n = 1"],
            ". Now you want to increment it with your ",
            ht.kbd()["+"],
            "on the keyboard, so the result is a sample (e.g.",
            ht.samp()["n == 2"],
            "). And maybe there's ",
            ht.data(value="one,two,three")["data"],
            ", where maybe the browser needs an internal value, but the user needs to see something friendly. ",
        ],
        ht.pre()[
            "\n<p> Writing code is hard. You have stuff like variables. Imagine where <var> n</var> is a variable.",
            ht.wbr(),
            " <br /> Maybe you have some code, like <code> n = 1</code>. Now you want to increment ",
            ht.wbr(),
            "it with your <kbd>+</kbd> on the keyboard, so the result is a sample (e.g.<samp> n == 2</samp>).\n\n</p>\n\n",
        ],
        ht.hr(),
        ht.h3()["List semantics "],
        ht.ol()[
            ht.li()["The first item in an ordered list"],
            ht.li()["The second item in an ordered list"],
        ],
        ht.ul()[
            ht.li()["I am a humble list item, I don't care if I'm first"],
            ht.li()["I am a second humble list item, put me wherever yo!"],
        ],
        ht.menu()[
            ht.li()[
                ht.a(
                    href="https://github.com/paceaux/typography-baseline",
                    target="_blank",
                    rel=["noopener"],
                )["See the Typography Baseline"]
            ],
            ht.li()[
                ht.a(
                    href="https://github.com/paceaux/form-baseline",
                    target="_blank",
                    rel=["noopener"],
                )["Look at the Form Baseline"]
            ],
            ht.li()[
                ht.a(
                    href="https://github.com/paceaux/table-baseline",
                    target="_blank",
                    rel=["noopener"],
                )["Review the Table Baseline"]
            ],
        ],
        ht.dl()[
            ht.dt()["ordered list"],
            ht.dd()[
                "a list with numbers, where the items need to be in a particular order "
            ],
            ht.dt()["unordered list"],
            ht.dd()[
                "a list with bullets or some other indicator, where the items can be in any order"
            ],
            ht.dt()["menu"],
            ht.dd()[
                "An unordered list with interactive items or commands that the user can use. "
            ],
            ht.dt()["definition list"],
            ht.dd()[
                "The forgotten list. It has definition terms,",
                ht.code()["<dt>"],
                "and definitions ",
                ht.code()["<dd>"],
                ". It's pretty much perfect for listing out the kinds of lists in a subtle, 4th wall-breaking kind of way. ",
            ],
        ],
        ht.hr(),
        ht.h3()["Language Semantics"],
        ht.p()[
            "Then there's that text where you need to show it in a different language. Like, say you want to know my name, but you speak Korean better than English. Well, I'd tell you my name is ",
            ht.ruby(lang="en")["Frank ", ht.rt(lang="ko")["퍼랜케"]],
            "and I hope you'd know how to pronounce it. ",
        ],
        ht.p()[
            "Sometimes, though, you need to show something in a semitic language. Maybe you want to say ",
            ht.ruby()["Shalom ", ht.rt(lang="he")[ht.bdi()["שלום"]]],
            ht.ruby()["in the home", ht.rt(lang="he")[ht.bdi()["בבית"]]],
            ".That's totally fine, just remember that text runs in the opposite direction in Arabic, Farsi, and Hebrew. ",
        ],
        ht.p()[
            "With Semitic Languages, though, you need to flip the order of some things. Say you're reading some text like, ",
            ht.bdi()["אני אוהב את יין"],
            "and it translates as ",
            ht.samp()[
                ht.bdo(dir="rtl")[
                    ht.bdi()["I"], ht.bdi()["like"], ht.bdi()["wine"]
                ]
            ],
            ". You have to remember that there's an element for saying a block of text is written in reverse, and another for saying a span of text should be the reverse of its parent. ",
        ],
        ht.p()[
            "Another way to understand that text is to look at the word-for-word translation: "
        ],
        ht.hr(),
    ]


def home():
    return common.create(
        content=ht.section[
            ht.article(class_="o-card")[
                ht.div["Welcome to the Hypertext World!"],
                ht.a(href="/blog")["Go to the Blog"],
            ]
        ]
    )


def blog_page(post: models.blog.Post):
    return common.create(content=blog.post(post))
