---
title: "On Useful Digital Tools"
date: 2026-03-30
draft: false
cover:
  image: "/images/sugar-bowl-banner.jpg"
  alt: "Snow-covered trees and ridge at Sugar Bowl"
  caption: "Sugar Bowl, California"
---

Everyone keeps saying that everything has changed for software now that AI is here. This essay discusses:

- why is agentic software different?
- what will differentiate agentic software?

## I.

I define "traditional software" as a set of digital tools that help users complete tasks. To develop such software, teams generally:

- listen to users describe a bunch of things they need to do
- design intuitive digital solutions to help them do those things
- implement those digital solutions in a scalable and stable way

Rinse and repeat: feature ideation, creation and distribution on top of an ever-expanding product surface. The best teams achieve "tasteful expansion," yielding product differentiation.

![Tasteful expansion: User Complexity vs # of Product Features](/images/useful-digital-tools-1-0.png)

To generalize: "traditional software" takes raw inputs (a table), transforms them into an interactive surface (a UI), lets a user act on those inputs (a series of transformations), and then saves the result as a new table.

## II.

I define "agentic software" as a collection of tasks that can be completed at an acceptable accuracy without human intervention, given a set of defined inputs. Quality is measured along three dimensions: what tasks are completed, what inputs are required, and what accuracy is expected.

When developing agentic software, product differentiation is to define 'successful task completion.' I define "successful task completion" as:

- *At minimum*, the expected outcome had someone done the task themselves
- *At best*, the ideal outcome without considering what someone would do themselves

Two things worth underscoring here. First, the minimum can be observed by user actions; the best is a point of view and may conflict with user actions. Second, the minimum can be evaluated immediately with shadow testing; the best can only be evaluated through a combination of domain expertise and available context.

![Model Feature Depth and success rates](/images/useful-digital-tools-2-0.png)

Critically, there is no user experience to consider (i.e., feature depth). All that matters is that the task success rate with input quality held constant is acceptable to the customer.

## III.

Consider a professional monitoring a radar screen. Given object speed, altitude, and heading, an observer can correctly model the decision space for a commercial air traffic controller to route planes safely. Yet with the same inputs a military operator might scramble jets while a meteorologist might log a data point while checking their phone.

Now consider the same scenario but with radar data delayed by five minutes. The air traffic controller communicates proactively but is otherwise calm; the military operator is paralyzed;. the meteorologist does not notice.

## IV.

Useful agentic software will not:

- define a universal approximation of user intent (i.e., those using radar are landing planes)
- evaluate success via a single output (i.e., proper radar use implies safe routing)
- assume input fidelity and reverence (i.e., five minute old radar signals can justify action)

Instead, useful agentic software will articulate successful outputs as a function of variable inputs. User interaction will concentrate on the integration and articulation of inputs because their transformation is assumed to achieve successful outputs.

## V.

This is the fundamental inversion. Traditional software treats inputs as things to be operated on. Agentic software treats inputs as things that shape the operation itself. Inputs now both define the boundaries of what software can do and underwrite its outputs.

Can we reasonably and reliably compress a person or persona to a bounded set of inputs?
