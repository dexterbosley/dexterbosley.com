---
title: "On Unserious Thinking"
date: 2026-10-09
draft: false
type: essay
description: "A price paid is the general form of verification."
home_recent: true
aliases:
  - "/essays/on-useful-digital-tools/"
cover:
  image: "/images/placeholders/essay-story-banner-placeholder.jpg"
  alt: "Soft ridgeline under a pale sky"
  caption: "White Mountains, United States"
---

## Thesis and definitions

**Claim:** A price paid is the general form of verification. Paying means someone checked the thing well enough to give up money for it, and paying again checks it twice. Unserious thinking substitutes a forecast of that price for the price itself.

| Term | What it is | How you measure it |
| --- | --- | --- |
| Narrative value | A signal to capital that you will capture a future market | Valuation, attention, fundraising |
| Net user value | Benefit minus everything it costs the user: price, effort, verification, risk | Retention, repeat purchase, willingness to pay |

- **Why price is the arbiter:** Lean verifies a proof; payment verifies everything else. Prices aggregate millions of private "was this worth it?" checks that no single opinion, including an investor's, can match.
- **Not every price verifies the same thing.** A repeat purchase verifies experienced value. An equity price is also a price paid, but for a forecast: it verifies what investors expect other investors to believe. Section 2 explains that gap.
- **A price only verifies what the payer can check.** In B2B the user and payer differ, so ask whose payment is doing the verifying. The memo example turns on this.
- **Watch for counterfeit prices:** attributed revenue, compute spent, demos shipped. They look like prices, but nobody chose to pay.
- **The verification term matters most for AI.** Output the user must check is not free output. If checking costs more than doing, net value is negative even when the demo is impressive.
- **The operating rule: keep a fare ledger.** Track what customers chose to pay for, repeatedly, net of the checking cost they carried, separately from what the story is worth. The rest of the essay explains why.

## 1. The confusion and its tell

Capital and customers run on different clocks, and the vocabulary of the slower one leaks into the faster one.

- Capital rewards a credible story about a future market today. That is fine for capital.
- The failure is when roadmaps start citing "this is where things are going" instead of "this saves X hours for Y team."
- **The tell: the argument has no subject.** Eric Seufert's critique of agentic commerce is the cleanest diagnostic: who are the "people," what is the "stuff," and why won't "they" use the incumbent's agent? Steal its shape for the whole essay.
- Beat to land: inevitability claims skip the step where someone decides it was worth it.

## 2. The mechanism: equity sets the agenda

Equity value is a forecast priced today, so leaders are rewarded for moving the forecast rather than the thing it forecasts. That makes chasing the narrative rational for every individual and unserious for the system.

**The transmission chain (top down):**

1. A company's equity value is the present value of expected future cash flows. In a platform shift, most of that value sits in the future, so the story about future markets moves the number more than this quarter's user value does.
2. Equity is the currency for everything leadership needs: capital, recruiting, retention and acquisitions. A higher mark makes all of it cheaper. For a private company the mark is set at funding rounds and tenders.
3. So leadership allocates toward what moves the mark: positioning, launches and demos that investors recognize as the winning theme.
4. That flows down as roadmap priority. Teams get measured on shipping the theme, and net value at the payer becomes a secondary check.
5. The feedback loops run at different speeds. The mark responds to a story within one round; net value shows up in retention and expansion over quarters or years. The fast loop wins the planning meeting.

**Why it's rational (say this plainly; the audience will respect it):**

- **Reflexivity.** If investors believe the AI-positioned company wins, it gets cheaper capital and better talent, which helps it win. The narrative partly fulfills itself.
- **Competition.** If rivals are rewarded for the story and you aren't, you lose the capital and talent race before the product race starts. Investors are pricing what other investors will believe.
- **Asymmetric blame.** No executive is faulted for chasing the consensus theme. Missing it is the career risk.
- **Everyone holds equity.** Employees are paid partly in the same mark, so the incentive runs all the way down the org chart.

**Why it's still unserious:**

- **Goodhart.** The mark is a forecast of net user value. Optimizing the forecast instead of the thing it forecasts breaks the measure.
- **It's borrowed against the future.** Multiples eventually converge on cash flows. Narrative without delivered value is a loan the company repays later, at the next round or at the public-market reckoning.
- **The cost lands on someone else.** The memo example is this chain in miniature: the theme ships, the employee is happy, and the payer inherits the verification cost.
- **Weisenthal said the quiet part out loud.** Reading the math results as a signal to investors is this mechanism described honestly.

**The serious version is not to ignore equity.** That would be naive. Instead:

- Label narrative bets as options: size them, cap them, and don't grade them on user value.
- Grade product work on net value at the payer.
- Look for the overlap. Memo automation done right (facts from data, humans only for the why) is a better story for a finance buyer than prose generation, because it reads as stronger controls.

## 3. Precedent: railroads, where the debt and the fares diverged

Railroads are the cleanest historical test of the thesis. Capital priced the story of the network; fares priced its use. The track was real and still runs, but many who financed it on the story lost, and the value went to users and to whoever bought the assets cheap.

| Episode | What capital did | What the fares said | Outcome |
| --- | --- | --- | --- |
| [Britain, 1840s](https://en.wikipedia.org/wiki/Railway_Mania) | 263 Acts for new railway companies in 1846 alone, proposing 9,500 miles; shares bought on a 10% deposit | Many lines proved unviable once running | About a third of authorized lines never built; many middle-class families lost their savings |
| [US, 1873](https://en.wikipedia.org/wiki/Panic_of_1873) | 33,000 miles laid from 1868 to 1873, much of it bond-financed with land grants; most capital in projects with no early returns | Jay Cooke & Co. could not sell Northern Pacific bonds | Cooke failed Sept. 18, 1873; 55 railroads failed by November and 60 more within a year; construction fell from 7,500 miles in 1872 to 1,600 in 1875 |
| [US, 1893](https://en.wikipedia.org/wiki/Panic_of_1893) | An 1880s railroad bubble left the network overbuilt | Rates kept falling: the rail rate for a bushel of wheat went from 14.70¢ in 1893 to 9.92¢ by 1901 | A quarter of all US rail mileage went into receivership; Northern Pacific, Union Pacific and Santa Fe failed |

**Who lost, who won:**

- **Lost: those who financed the story.** Shareholders and bondholders, including British savers and European buyers of American railroad bonds.
- **Won: users.** Falling rates passed the network's value to shippers. The fare is where value is verified, and it went to the people paying it.
- **Won: whoever bought after the reset.** In Britain, Great Western and Midland bought failed lines for a fraction of their value, and many became viable inside the larger network.
- **Won: builders who built against fares.** [Great Northern](<https://en.wikipedia.org/wiki/Great_Northern_Railway_(U.S.)>) was built in stages, profitable lines first. It took no land grants, bought land from the government and resold it to settlers, recruiting the traffic it would carry.

**The sharper cut: the people running the railroads got rich on the raise, not the fares.** Raising was rational for them and operating was unserious, because the two paid out separately.

- **[Crédit Mobilier](https://en.wikipedia.org/wiki/Cr%C3%A9dit_Mobilier_scandal).** Union Pacific insiders set up their own construction company and sat on both sides of every contract. Congress paid Union Pacific about $94.7 million against roughly $50.7 million paid to Crédit Mobilier, leaving about $43.9 million in profit for the same directors.
- **Why they built it that way.** The insiders didn't expect profits from operating the railroad, so they took them in the construction phase. After the 1872 exposé, Union Pacific and other investors were left nearly bankrupt.
- **[George Hudson](https://en.wikipedia.org/wiki/Railway_Mania), the British "Railway King,"** paid dividends out of capital: returns to earlier investors funded by new money rather than by fares.
- **Keep it fair.** Historian Maury Klein concluded the builders did not defraud the government, though bribery was a qualified yes. The point isn't the crime; it's where the profit sat.

**The mechanism with the mask off.** When the raise itself pays the people running the enterprise, the fares stop mattering to them. That is section 2's logic taken to its end: rational for the insider, unserious for the enterprise.

**The question for any AI plan, including ours:** who gets paid on the raise, and who only gets paid on the fare? Aim this at the mechanism, not at people. Every company paid partly in marks has the same exposure, and the defense is to keep a fare ledger.

**What still exists.** The track. About 6,220 miles were built from projects authorized in 1844–46, against roughly 11,000 miles in the UK network today. In the US, [BNSF](https://en.wikipedia.org/wiki/BNSF_Railway) descends from Great Northern, Northern Pacific, Burlington and Santa Fe; Berkshire Hathaway bought it in 2010 in a deal valued at $44 billion including debt. BNSF and Union Pacific share a duopoly on western transcontinental freight. Two of the railroads that failed in 1893 now sit inside the survivor. Infrastructure outlives its financing.

**Map it to now.**

- Debt raised is narrative value: priced on the network's future. Fares are the price paid per use. When fares couldn't service the debt, the debt reset to what fares could carry.
- AI's version: compute built on the story, with token prices as the fares. The open question is whether fares can service what was raised.
- **The prediction the essay can make:** the AI is probably real, like the track. That doesn't mean everyone who financed it on the story gets paid. Value flows to users through falling prices, and to whoever owns the assets after the reset.
- **Ramp's position:** closer to the shipper than the railroad. Falling token prices are our falling freight rates, but only if we pass the value to customers and price it in a way they can verify (section 7).

## 4. Example 1, external: agentic commerce

The evidence says agents create value when intent is fully specified, and that the platform owning the relationship captures it. Neither supports "a startup builds the next Amazon with agents."

**The specimen.** Paul Graham: Amazon banning agents is the first opening for an Amazon competitor since its founding, because people will want agents to buy stuff for them. It is asserted as inevitable. Seufert's rebuttal asks the missing questions: who, what stuff, and why not Amazon's own agent?

**What actually happened (the facts the essay can lean on):**

- Amazon blocked Meta's Muse agent in September 2026. Its stated reasons: Meta never notified it, the agent doesn't identify itself, and it appears to store customer credentials. [VKTR](https://www.vktr.com/ai-platforms/amazon-blocks-metas-muse-ai-agent-from-shopping-on-its-platform/)
- The legal route narrowed first. The Ninth Circuit ruled on Aug. 4, 2026 that the user, not the AI company, is the one accessing Amazon under anti-hacking law, so Amazon now enforces through its Conditions of Use. [VKTR](https://www.vktr.com/ai-platforms/amazon-blocks-metas-muse-ai-agent-from-shopping-on-its-platform/)
- The motive is the ad business: more than $68 billion last year, which depends on people browsing sponsored pages. [VKTR](https://www.vktr.com/ai-platforms/amazon-blocks-metas-muse-ai-agent-from-shopping-on-its-platform/)
- Amazon's own agent is the counterexample to "nobody wants this." It reports Rufus drove nearly $12 billion in incremental annualized sales in 2025 across 300 million users, roughly $40 per user per year. [PPC Land](https://ppc.land/amazons-ai-shopping-assistant-drove-12-billion-in-sales-for-2025/)

**Run the net-value test.**

| Use case | Is intent specified? | Who bears the risk? | Verdict |
| --- | --- | --- | --- |
| "Buy me a good jacket" | No; browsing is part of the utility | User, via returns | Unpriced |
| Rufus price alert: buy this item at this price | Yes | Low; 24-hour cancel window | Works: users average 20% savings ([PPC Land](https://ppc.land/amazons-ai-shopping-assistant-drove-12-billion-in-sales-for-2025/)) |
| Third-party agent on Amazon | Varies | Platform, which blocks it | Blocked by the party that owns the relationship |
| Policy-bound business purchasing | Yes: specs, budgets, approvers | Company, with controls | Hypothesis to test (the Ramp angle) |

**What it proves.**

- Even the $12 billion is narrative-shaped. It is Amazon's own counterfactual attribution, and PPC Land notes the method rests on behavioral assumptions. Use it to show that the "real" number also needs the net-value test.
- The agent ↔ retailer plumbing commoditizes while fulfillment, returns and support costs stay with the retailer. That is Seufert's point and it holds.
- Flip, don't dunk: name where the test passes. Delegation pays when the buyer can fully specify what they want, which describes most of business spend better than most of consumer shopping.

## 5. Example 2, external: theoretical math

The math releases are a clean case study because verification is measurable. When volume went up, the verified share went down, and the checking cost moved to everyone else.

**Why labs do it (Weisenthal's read).** Theoretical math is mostly an intellectual pursuit. Its function is a signal: a lab that solves open problems can beat others to commercially valuable breakthroughs in pharma or chip design. Read that way, the "pre-IPO hype" critics and Weisenthal agree on what the math is for. It is narrative value, and a legitimate investment thesis.

**What the record shows:**

| Release | What shipped | Verified share |
| --- | --- | --- |
| [Ten advances](https://openai.com/index/ten-advances-in-mathematics/), Aug. 1, 2026 | 10 results | All 10 shipped with Lean certificates |
| [Navier–Stokes](https://openai.com/index/navier-stokes-solution/), Sep. 8, 2026 | 1 Millennium Prize claim | Lean-formalized; whether the formal statement matches the Clay problem is still being checked ([NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/)) |
| [openai/math](https://github.com/openai/math), Oct. 6, 2026 | 719 manuscripts in 372 families, from \~4,000 problems posed | \~42% of top-line results formalized |

- The repo's own README says not all results have Lean formalizations and some unformalized ones could have issues. [GitHub](https://github.com/openai/math)
- Each result cost about three hours of ChatGPT Pro-equivalent compute. [OpenAI](https://openai.com/index/sharing-ai-progress-in-mathematics/) Producing a claim is now cheap; checking one is not. Navier–Stokes is the outlier; see the crude version below ([NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/)).
- Dan Roberts' Oct. 8 update: 6 new formalizations, 19 modifications, 3 withdrawals. Lucas Beyer's reaction: why ship the batch and check half afterward?

**The crude version: Navier–Stokes.** The prize is $1 million. The final run used about 10,000 agents over 88 hours, at compute OpenAI put in the millions of dollars, and that figure excludes training the model. OpenAI then said it won't claim the prize. ([NYU Shanghai RITS](https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/))

- **Read as a product, it's absurd.** They spent more than the only posted price for the result, then declined the payment. Nobody else is a buyer for the proof itself.
- **Read as marketing, it's cheap.** Millions in compute is a rounding error against the equity value it signals. This is section 2 in one transaction: the spend is rational because the return is booked in the valuation, not in anyone's use of the result.
- **The unserious part is the framing.** Calling it a math breakthrough is fine. Implying the proof is where the value lies is the confusion. The value bought is a narrative, and the bill for checking it goes to the fluid-dynamics community.
- **Keep the claim honest.** The sourced figures show compute at a multiple of the prize, not orders of magnitude. Training costs would widen the gap, but no public number covers them, so don't assert one.

**The causal insight.** "42% formalized" is a ledger of net value delivered. The unformalized 58% is a liability moved onto mathematicians, who now carry the verification cost. That is the net-value equation from the definitions, with real numbers.

**Where it goes if nobody prices verification.** Steven Glinert's joke is the extrapolation: billions in tokens produce far more mathematics than humanity has ever written, an unknown share of it is wrong, and checking can't keep up. A reply says the AIs will verify it for us, which is the 42% in the repo, still trailing.

- **The fair counter (Noah Smith):** this already existed. Humans have long produced math nobody else understands that might be wrong.
- **The answer:** the difference is the cost ratio. Human output was rate-limited by human effort, so production and checking scaled together. The author was the first verifier, and reputation priced the rest. AI breaks that link: production gets near-free while verification stays expensive and human.
- **The theme to carry forward:** when production gets cheap, verification becomes the price. Unserious thinking is ignoring who pays it.

**What it proves.** A capability demo is an option on future value, not value. Building it is fine. Booking it as delivered is the unserious move. Note the fair counterpoint: the August release showed the lab can ship fully verified work, so the October batch was a choice about speed, not a limit of the method.

## 6. Example 3, at Ramp: memo automation (hypothetical)

Memo automation is the same pattern inside our own product: it creates value for the employee and destroys it for the admin who pays us. The two external examples make the pattern easy to see from a distance; this one shows the audience it applies to them.

**The hypothetical.** AI writes every expense memo. The employee does less work, a clear win. The admin, who buys Ramp and advocates for it internally, now gets memos that say nothing.

**Why it breaks.** The memo was never the product. It was a costly signal: the effort of writing one deterred marginal purchases and carried information to the reviewer. Automate the writing and the cost drops to zero, and the signal goes with it.

| Party | Before | After automating the prose |
| --- | --- | --- |
| Employee | Writes a short justification | Writes nothing: gain |
| Admin (the payer) | Reads a human reason | Audits fluent text that may be wrong: verification cost moves to them |
| Company spend | Writing deters marginal purchases | Deterrent gone |

**What happens next.** The admin does one of three things:

1. Ignores memos and loses control.
2. Adds friction back through approvals or receipt rules, which undoes the employee's gain.
3. Concludes Ramp weakened their controls, which is churn risk at the person who signs the contract.

**What it proves.** In B2B the user and the payer are different people. Net value has to clear at the payer, not just the user.

**Tie it to the math example.** Generated prose is the unformalized 58%: plausible, unchecked, and someone else's problem. Facts drawn from data are the Lean-verified 42%.

**The serious version.** Automate what the memo stood in for, not the prose.

- Fill the facts from data: merchant, attendees from the calendar, trip context, policy match. These are grounded and checkable.
- Ask a human only for the irreducible "why," and only when the data can't explain the spend.
- Flag exceptions loudly, so the admin reviews the few cases that matter instead of skimming many plausible ones.

**Correct the premise.** Perfect memos are not the goal. Correct spend decisions at the lowest total cost are, and memos were one means to that.

## 7. At Ramp, for real: how we price AI

Ramp prices its AI per seat, so the price we charge cannot verify the AI we ship. By this essay's own thesis, we have switched off our best instrument.

**What the pricing page says** ([ramp.com/pricing](https://ramp.com/pricing), accessed Oct. 9, 2026):

| Tier | Label on the page | Price unit |
| --- | --- | --- |
| Free | "AI-assisted" | $0 per user per month |
| Plus | "AI-powered" | $15 per user per month, plus a platform fee based on team size |
| Enterprise | "AI-tailored" | Custom, billed annually |

- The AI ships inside the seat. AI-driven expense reviews, AI coding for every field, and AP-agent approval recommendations and line-item coding are all listed as Plus features.
- The labels are narrative; the unit is a seat. Almost nothing is metered beyond small items like $0.65 per IRS 1099 filing.
- **Keep the critique precise.** The card business already earns per transaction through interchange, so Ramp does run on a usage price where most of the money is. The gap is narrower: software and AI are priced per seat.

**Why a seat price can't verify AI:**

- An AP agent that codes 10,000 invoices and one that codes 10 earn the same. The price doesn't move when value does, so it can't tell us which agent work is worth anything.
- It can run backwards. AI that removes work reduces the number of people who need to touch Ramp. If seats track people, delivering the value shrinks the base we price on.
- It hides the memo problem. If generated memos made the admin's job worse, no line item would show it until renewal.

**Why it's rational (section 2 again):**

- Seat revenue is predictable and recurring, the revenue shape investors reward most. Usage revenue swings with customer activity.
- Usage pricing forces a hard question every month: did this unit of work earn its price? Seat pricing defers that question to renewal.
- So staying on seats is rational, and it is also the choice not to be verified.

**The serious version:**

- Meter what the AI does where the payer can check it: invoices coded correctly, memos accepted without edits, policy exceptions caught.
- If the price stays per seat, instrument as if it weren't. Keep an internal shadow price per agent action and watch which ones customers would pay for on their own.
- Make the ask small. The essay doesn't need to win the pricing argument; it needs leadership to agree to measure as if the price were real.

## 8. Steelman: what we concede

Narrative value is not fake value; it funds the work that later becomes real value. The essay has to concede this to be credible.

- **The strongest objection:** some things look worthless until they suddenly don't. The math demos may well be the R&D that produces the pharma result Weisenthal describes.
- **Amazon proves agents can pay.** Rufus is real usage at real scale, so "agentic commerce is fake" is simply wrong.
- **Response:** agreed on both. The essay is not anti-AI and not anti-investor. Its claim is narrower: keep two ledgers, and never let the narrative ledger pay the product ledger's bills.
- **Where operators slip:** they ship the demo and count it as the outcome. Ask which ledger a project is on before it starts, not after.

## Conclusion: keep a fare ledger

You don't have to settle whether AI is fundamentally worth it. Economics only asks about the change: did someone end up better off by more than it cost them, and will they come back?

**Rational is not the same as serious.** Rational means the incentives pay the person deciding. Serious means the outcome is verified by what customers pay. Every example in this essay sits somewhere on those two axes.

&#91;embedded content: rational vs serious · four quadrants\]

Most AI work drifts to the bottom right: rational for the decider, priced on narrative. The essay argues for the top right, and that it beats the bottom right on the bottom right's own terms.

**Why serious and rational wins on its own terms:**

- **Marks converge to fares.** Multiples eventually meet cash flows, so the fare ledger is the forecast the mark will be judged against (section 2).
- **Fares compound; raises don't.** Repeat purchase funds the next unit of work without anyone's permission. A raise has to be won again every round.
- **The assets go to whoever can carry them on fares.** After every railroad reset, operators who could run the lines on fares bought them cheap, and Berkshire later paid $44 billion for the survivor (section 3).
- **A fare ledger is the best story you can tell capital.** It's the one story that has already been checked, so serious is also the most rational pitch.

**Why it's the human thing:**

- **A price paid is a person's judgment.** Keeping a fare ledger treats customers as judges, not as an audience for a story.
- **Unserious work moves the checking cost onto people who never agreed to carry it:** mathematicians auditing unformalized proofs, admins auditing generated memos. Serious work carries its own verification.
- **It respects the team's time.** Work graded on fares outlasts the theme it launched under.

* That debate about fundamental worth is unwinnable and beside the point. Prices settle the marginal question without anyone having to win it.
* All three examples resolve the same way. Agents pay where intent is specified, math pays where it is verified, and memo automation pays where the payer still gets a signal. Everywhere else, the value is still a promise or a cost moved onto someone else.

**The through-line.** In every example, AI made production cheap and left verification expensive. The math community checks the 58%, the retailer absorbs the agent's returns, the admin audits the generated memo. The serious question is always who now holds the checking cost, and whether they agreed to.

**The fare ledger, as four questions anyone can run on an AI feature:**

1. Who, specifically, uses it?
2. What do they stop doing or paying for?
3. Who bears the verification cost, and what does it cost them?
4. Would they pay for it if "AI" weren't in the name?

## Open items and sources

- [ ] Link the original posts by Weisenthal, Seufert, Graham, Roberts, Beyer, Glinert and Smith. They are quoted here from your screenshots, not opened.
- [ ] Find Weisenthal's full newsletter piece on the math breakthroughs if you want his argument beyond the posts.
- [ ] Decide whether to use independent research claiming Rufus favors Amazon's own products. It surfaced in search but couldn't be opened, so it stays out until verified.
- [ ] Pull internal evidence for the business-purchasing hypothesis before presenting it as the flip.
- [ ] Check whether any in-flight agent-payments work reads the agentic commerce section as criticism.
- [ ] Confirm with finance how much of revenue is interchange versus software before publishing the pricing section.
- [ ] Pull internal counts of AI actions per seat (invoices coded, memos generated) to make the seat-versus-value gap concrete.
- [ ] Confirm Great Northern avoided receivership in 1893; it would make the strongest contrast with Northern Pacific, but the opened sources don't state it.
- [ ] Decide whether to add current AI data-center debt figures to the railroad section; they aren't sourced here yet.

**Sources (pages opened):**

- [VKTR: Amazon blocks Meta's Muse AI agent](https://www.vktr.com/ai-platforms/amazon-blocks-metas-muse-ai-agent-from-shopping-on-its-platform/) (Sep. 22, 2026)
- [PPC Land: Amazon's AI shopping assistant drove $12 billion in sales for 2025](https://ppc.land/amazons-ai-shopping-assistant-drove-12-billion-in-sales-for-2025/) (Feb. 7, 2026)
- [OpenAI: Sharing AI progress in mathematics](https://openai.com/index/sharing-ai-progress-in-mathematics/) (Oct. 6, 2026)
- [GitHub: openai/math README](https://github.com/openai/math)
- [NYU Shanghai RITS: OpenAI claims a Navier–Stokes proof, amid a dispute over credit](https://rits.shanghai.nyu.edu/ai/openai-navier-stokes-proof-credit-dispute/) (Sep. 9, 2026)
- [Crypto Briefing: OpenAI releases new mathematical results](https://cryptobriefing.com/openai-solved-math-problems-github-release/) (Oct. 6, 2026)
- [Ramp: Pricing and plans](https://ramp.com/pricing) (accessed Oct. 9, 2026)
- [Wikipedia: Railway Mania](https://en.wikipedia.org/wiki/Railway_Mania)
- [Wikipedia: Panic of 1873](https://en.wikipedia.org/wiki/Panic_of_1873)
- [Wikipedia: Panic of 1893](https://en.wikipedia.org/wiki/Panic_of_1893)
- [Wikipedia: Great Northern Railway (U.S.)](<https://en.wikipedia.org/wiki/Great_Northern_Railway_(U.S.)>)
- [Wikipedia: BNSF Railway](https://en.wikipedia.org/wiki/BNSF_Railway)
- [Wikipedia: Crédit Mobilier scandal](https://en.wikipedia.org/wiki/Cr%C3%A9dit_Mobilier_scandal)
