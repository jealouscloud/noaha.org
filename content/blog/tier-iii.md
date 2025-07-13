---
post-date: 5-16-25
slug: tier-iii
id: 3
display: false
---

Take care of your team. Their well-being is your well-being.

I’m writing this because I’ve been thinking a lot about how to organize a Tier 3 
group. 
A lot of what we do relies on unspoken knowledge that deserves to be written
down.

As a team, we are the convergence of technology and strategy.
We are the foundation upon which the company operates.
We are the beacon that guides the next step when that foundation finally develops
a crack.

We operate in infrastructure, which works in domains.

If you don't know how to categorize something, ask the wizard of the castle.
If you don't think they're right, drill down. If all else fails, ask a friend.

**editors note**: a drunk wizard is probably a fair characterization of ai

If you were wondering what the theme implies we are, I like to think we'd be 
dwarves.

The sign post:

### HELP WANTED

- Infrastructure maintainer
- Idea haver
- Rhythm keeper
- Spirit bringer

### HELP NOT WANTED:

- Follower ("I don't follow, but I will agree")
- Poor contributors: Not able to seek own answers. Would do something wrong 
before they would ask for help.
- Disinterested learners: Please take notes.
- Lost, won't tell you.
- Does not use git to annotate audit trail
  - ~~Updated main.py~~
    - What for? A code format? Syntax/logic simplification?
  - ~~code refactor~~
    - Why did you do this? Are you prepping for another change? 

---

Imposter syndrome is a common experience in technical teams. I highlight here
what is undesired because truly what we want is a team mate.

---

So. You passed the hiring trial and made it into our tavern.
Shortly after, you're assigned to the queue. 
It’s a long one, and there’s a lot they didn’t tell you. Some of the cobwebs are
older than your entire tenure.

And you thought you could help.
You can, just not like you thought.
So day after day, week after week, month after month.

Your soul gets beaten into a pulp
As you molt into a rigid steel gear that turns the corpo calendar forward
one mechanistic moment into the other.

---

We don't want that to happen to you.
You were bright and interested when you walked through the door.
That's what we wanted. That's why we took you.

---

This is how we do it.

# Quality Constraints

Every work unit must obey quality constraints.
Green field work is especially hard to qualify.
Tools must be inventoried and cataloged. The bill of requirements cannot be infinite.

Prescriptions

- Tool use must not be mechanistically constrained as to stifle innovation
- Tool selection must satisfy domain requirements

# Domain Definitions

A common understanding of a domain paves the way for structured work.
A domain should be defined with as many of these properties fleshed out as is
reasonably possible.

- Name / identity
- Terms, properties, lingo
- Boundaries of scope
- Tools
- Dependencies and interfaces with other domains
- Key metrics / Success indicators
- Pitfalls, gotchas
- Lessons "I was here so you dont have to"
- Contribution guidelines
- Governance model: Ownership, approval, stakeholders, review frequency
  - If a frequency is mandated but not scheduled it is lip service.

The above list is a strong suggestion but may not always be a perfect fit.

Some key questions to answer when looking at a domain definition:

- How do I find [my component] in [this domain]
- How do I troubleshoot [this issue]
- Where is documentation maintained
- What projects interface with this domain
- What are standard maintenance procedures
- What monitoring exists and what metrics matter
- What are the primary interfaces/APIs for this domain

Structured Work
===============

Dwarves.
We have our tools. Our axe. Our codex.
We like tasks with all the information we need to complete.

### A task
* Definition | Estimate
* Comprehension
* Attempt
* Result

Achieving excellence in this core unit is paramount.
<!-- Getting better at this core unit is something we can discuss as a team. -->

<!-- I would like to use this as the core unit.
Tasks are punched in.
You may end up on a tangent.
Log where your tangent took you.
If the task deviates as written, you:
* Remove the estimate
* Give a comment regarding the deviation
* Change the task status to pending review

 -->


# Solid Contributions

Ideally, a structure exists. We contribute to this ideal to improve our quality of life.

## Domain contributions
Solid contributions don't scramble the domain. They add to it.

* Follow patterns within the domain, if they exist
* Prefer the domain's native way to accomplish something when reasonable 
i.e. `procutil` vs `subprocess.run("ps")`
* If you deviate from the typical pattern, document why
* Update domain knowledge as you learn


## Interfaces in code
We hope for our code to be pluggable as it evolves. Adaptability is a major
feature in repositories. Between shipping for multiple distros, configuration
agnosticism, database ORM, there are many common ways we prioritize allowing
any component we produce to adapt to change as it happens. 

Some tips:
* Separate logic types where you can: databases, endpoints, application logic, 
process calls
* Define variables where you could reasonably use them later and implementing 
correctly now is relatively simple. An example of this would be writing a 
function with parameters that make the function flexible. i.e. 
  ```python
  def run(cmd, shell=True):
      subprocess.run(cmd, shell=shell)
  ```
  instead of

  ```python
  def run_cmd(cmd):
    subprocess.run(cmd, shell=True)
  ```

## Leaving a trail
We might have to follow our own footsteps one day to understand why a change 
went wrong.


## Performing Simple Assignments
Scoping is key in change requests. Simple assignments often include all the 
information you need. Sometimes they are quite lacking. If you are having 
difficulty scoping a change or problem, it's usually a good time to ask the 
team for input.

While doing the task itself:
* Log your understanding as you can
* Create a branch for any repo change matching the ticket ID.
* Note when expectation and reality don't converge
* If a task feels harder than it should be, maybe it is - if you notice this, 
vocalizing it helps expose neglected systems, like CI/CD.


## Pattern observation
When a system isn't working, reporting the problem as a ticket with the information
you can quickly acquire helps the team act effectively.


## Individual Initiative
Sometimes you must create a new component yourself.

When doing this:
* Ensure the component fits well into its environment. Beyond your own reasoning,
checking in with team members can help with this goal.
* Try to use git early, including using a branch when you start work.
* Ensure there's accurately placed documentation.
* Remember that it is quite rare for a component to be set-and-forget. 
  Dilligence pays dividends