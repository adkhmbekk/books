# -*- coding: utf-8 -*-
"""Analytical content for the 'Attached Analysis' PDF.

Independent analytical synthesis of adult attachment theory.
Does not reproduce the source book's text or illustrations.
"""


def _h1(B, t): B.append(("h1", t))
def _h2(B, t): B.append(("h2", t))
def _h3(B, t): B.append(("h3", t))
def _p(B, t):  B.append(("p", t))
def _b(B, t):  B.append(("bullet", t))
def _q(B, t):  B.append(("quote", t))
def _s(B, t):  B.append(("small", t))
def _br(B):    B.append(("pagebreak", ""))
def _title(B, t): B.append(("title", t))


def build_blocks():
    B = []
    add_cover(B)
    add_toc(B)
    add_ultra_short(B)
    add_power_ideas(B)
    add_part1_foundations(B)
    add_part2_three_styles(B)
    add_part3_pairings(B)
    add_part4_protest(B)
    add_part5_dating(B)
    add_part6_communication(B)
    add_part7_change(B)
    add_part8_hidden_assumptions(B)
    add_part9_critique(B)
    add_part10_map(B)
    add_part11_practical_plan(B)
    add_part12_pareto(B)
    add_appendix(B)
    return B


def add_cover(B):
    _title(B, "Attached: A Deep Analytical Guide")
    _p(B, "An applied breakdown of adult attachment theory - the framework "
          "popularized by Amir Levine and Rachel Heller in their book "
          "Attached: The New Science of Adult Attachment.")
    _p(B, "This document is an independent analysis. It explains, extends, "
          "applies, and critiques the underlying theory. It is not a "
          "reproduction or translation of the book.")
    _p(B, "Reader profile: someone who wants to actually use these ideas - "
          "to understand themselves, read partners earlier, communicate "
          "better, and choose more wisely. Not a theoretical overview.")
    _p(B, "Author of this analysis: Kiro (AI analyst). Format: structured "
          "study guide. Language: English.")
    _br(B)


def add_toc(B):
    _h1(B, "Table of Contents")
    _b(B, "1. Ultra-short summary (read this first)")
    _b(B, "2. The most powerful ideas in one list")
    _b(B, "3. Foundations: where attachment theory comes from")
    _b(B, "4. The three styles, properly understood")
    _b(B, "5. How styles interact: the dynamics of pairings")
    _b(B, "6. Protest behavior and the anxious-avoidant trap")
    _b(B, "7. Dating: how to read a partner early")
    _b(B, "8. Effective communication: a practical method")
    _b(B, "9. Can you change your style? What is realistic")
    _b(B, "10. What the authors quietly assume")
    _b(B, "11. Where the authors are right - and where the logic bends")
    _b(B, "12. A connection map of all key ideas")
    _b(B, "13. A practical 6-week plan")
    _b(B, "14. The 20% that gives 80% of the results")
    _b(B, "15. Appendix: glossary, self-assessment prompts, red/green flags")
    _br(B)


def add_ultra_short(B):
    _h1(B, "1. Ultra-Short Summary")
    _p(B, "Adult humans, just like children, have a built-in attachment "
          "system - a set of emotional and behavioral programs that "
          "regulate closeness with a romantic partner. This system is "
          "not pathology, not weakness, not bad psychology. It is "
          "biology, the same way hunger and fear are biology.")
    _p(B, "People differ in how their attachment system reacts to "
          "closeness, distance, and conflict. Decades of research "
          "compress this variation into three working patterns:")
    _b(B, "Secure - comfortable with closeness and with autonomy. "
          "Reads partner signals accurately. Recovers from conflict.")
    _b(B, "Anxious - hyper-tuned to signs of distance. Closeness "
          "calms; perceived distance triggers protest behavior.")
    _b(B, "Avoidant - hyper-tuned to signs of engulfment. Distance "
          "calms; closeness triggers deactivating strategies.")
    _p(B, "A fourth pattern (disorganized / fearful-avoidant) blends "
          "anxious and avoidant features and usually reflects more "
          "complex early experience or trauma.")
    _p(B, "The single most consequential idea in this whole field: "
          "many problems people interpret as 'we are incompatible' "
          "or 'something is wrong with me' are actually predictable "
          "interactions between two attachment systems. Once you can "
          "name the pattern, the situation stops being personal "
          "drama and becomes legible.")
    _p(B, "The single most consequential practical move: when choosing "
          "a long-term partner, weight attachment style at least as "
          "heavily as chemistry, looks, status, or shared interests. "
          "A secure partner is a force multiplier for your life. An "
          "avoidant partner paired with anxious style is a slow, "
          "painful loop that reliably damages both people.")
    _p(B, "Everything else in this guide is the unpacking of those "
          "two sentences.")
    _br(B)


def add_power_ideas(B):
    _h1(B, "2. The Most Powerful Ideas (Quick List)")
    _p(B, "If you read nothing else, read these. Each one is a lever "
          "that, used correctly, changes outcomes in your love life.")
    _b(B, "Idea 1. Attachment style is descriptive, not destiny. It "
          "predicts your default reactions, not your fate.")
    _b(B, "Idea 2. The 'dependency paradox': in a healthy bond, "
          "having a reliable partner makes you more independent in "
          "the world, not less. Needing someone is not weakness.")
    _b(B, "Idea 3. Anxious and avoidant styles are mirror images. "
          "Both are activated by the same threat (loss of "
          "equilibrium in closeness) but solve it in opposite ways.")
    _b(B, "Idea 4. Anxious + avoidant pairings are statistically "
          "common and emotionally addictive. The intensity feels "
          "like love; it is mostly the attachment system flailing.")
    _b(B, "Idea 5. Secure people are systematically undervalued in "
          "early dating because their nervous systems do not "
          "generate the spikes we mistake for chemistry.")
    _b(B, "Idea 6. Most 'communication problems' in couples are "
          "really protest behavior or deactivation in disguise. "
          "Fix the attachment-level signal and the words follow.")
    _b(B, "Idea 7. Effective communication is direct, specific, "
          "non-blaming, and focused on needs - not on the partner's "
          "personality. This is a learnable skill.")
    _b(B, "Idea 8. You can shift toward more secure functioning. "
          "It is slow and uncomfortable, not a personality "
          "transplant. The fastest path is a relationship with a "
          "secure partner plus deliberate self-work.")
    _b(B, "Idea 9. Early in dating, patterns are visible within "
          "weeks if you know what to look for. Most people see the "
          "signals but rationalize them away.")
    _b(B, "Idea 10. The relationship is the unit of analysis, not "
          "the individual. 'Are they good for me' beats 'are they "
          "a good person'.")
    _br(B)


def add_part1_foundations(B):
    _h1(B, "3. Foundations: Where Attachment Theory Comes From")
    _p(B, "To use attachment theory well in adult life, you need to "
          "see what it actually is - and what it is not. The popular "
          "version often gets flattened into a personality test. It "
          "is more interesting and more useful than that.")

    _h2(B, "3.1 The biological core")
    _p(B, "Attachment theory began with John Bowlby in the 1950s-60s. "
          "Working with separated and orphaned children after WWII, "
          "Bowlby observed that infants do not just need food and "
          "warmth - they need a specific caregiver and reliably "
          "fall apart without one. He proposed that humans, like "
          "other mammals, evolved an attachment system: a set of "
          "behaviors (crying, clinging, seeking proximity) whose "
          "evolutionary job is to keep the young close to a "
          "protector. This is not learned. It is hardware.")
    _p(B, "Mary Ainsworth turned Bowlby's ideas into measurable "
          "research with the Strange Situation procedure. Toddlers "
          "were briefly separated from caregivers and observed on "
          "reunion. Three reproducible patterns emerged - secure, "
          "anxious-ambivalent, and avoidant - plus a later fourth "
          "(disorganized) added by Mary Main.")
    _p(B, "The leap that made the field relevant to adults came in "
          "1987, when Cindy Hazan and Phillip Shaver showed that "
          "the same patterns appear in adult romantic relationships. "
          "Romantic partners function as attachment figures the "
          "same way caregivers do for children. The implication is "
          "uncomfortable and true: adult love is not only about "
          "compatibility, values, or chemistry. It is also about "
          "two attachment systems trying to regulate each other.")

    _h2(B, "3.2 Why the system matters more than you think")
    _p(B, "When the attachment system is activated - by separation, "
          "ambiguity, fear of loss, conflict - it overrides almost "
          "everything else. Smart people make stupid relationship "
          "choices not because they are stupid, but because the "
          "attachment system is older and faster than the prefrontal "
          "cortex. You cannot reason yourself out of it in real time. "
          "You can only build a life and a relationship that "
          "activate it less catastrophically.")
    _p(B, "This is why willpower-based advice ('just do not text "
          "him') usually fails. It tells the modern brain to win a "
          "fight against ancient circuitry that has had millions of "
          "years of practice. The realistic move is to set up "
          "conditions where the attachment system is satisfied, "
          "not to pretend it is not there.")

    _h2(B, "3.3 The dependency paradox")
    _p(B, "A central, counterintuitive finding: secure attachment "
          "produces more independent functioning, not less. People "
          "with a reliably available partner take more risks, "
          "explore more, perform better, and recover from setbacks "
          "faster. The cultural script that says 'do not need "
          "anyone' is biologically backwards. Humans are wired to "
          "venture out from a base, not to operate alone.")
    _p(B, "Implication: when you tell yourself that needing a "
          "partner is weakness, you are not being wise. You are "
          "internalizing a story that fights your biology and that "
          "tends to leave you either chronically anxious or "
          "chronically distant.")
    _br(B)


def add_part2_three_styles(B):
    _h1(B, "4. The Three Styles, Properly Understood")
    _p(B, "Most popular write-ups of attachment styles flatten them "
          "into personality cliches: anxious people are needy, "
          "avoidant people are cold, secure people are unicorns. "
          "That is wrong in a way that matters. Each style is a "
          "coherent strategy - it solves a real problem, just at a "
          "high cost.")

    _h2(B, "4.1 Secure (roughly 50-55% of adults)")
    _p(B, "Core experience: closeness is safe; autonomy is safe. "
          "Conflict does not feel like a threat to the bond. "
          "Disagreement does not flip the system into emergency.")
    _p(B, "How they actually behave: they ask for what they want, "
          "in plain language, without weaponizing it. They listen "
          "without immediately defending. They assume good intent "
          "until shown otherwise. They do not panic over delayed "
          "replies. They do not punish small distance with big "
          "withdrawal. They give partners the benefit of context.")
    _p(B, "What feels weird about them in early dating: their "
          "nervous system is calm, so the relationship does not "
          "produce the spikes that anxious or avoidant people read "
          "as 'real' chemistry. People often call secure partners "
          "'boring' for the first few weeks, then realize three "
          "months later that nothing has gone wrong and that the "
          "calm itself is the gift. This is the most expensive "
          "misreading in dating.")
    _p(B, "Important nuance: 'secure' is not the same as 'has no "
          "issues.' A secure person can be insecure in other "
          "domains (career, family, anxiety). The label refers to "
          "the attachment dimension only.")

    _h2(B, "4.2 Anxious (roughly 20% of adults)")
    _p(B, "Core experience: closeness is the goal; perceived "
          "distance is danger. The system reads ambiguity as "
          "rejection by default.")
    _p(B, "Internal logic, expressed honestly: 'If I do not stay "
          "vigilant about the connection, I will lose it. The cost "
          "of overreacting is small; the cost of missing a real "
          "loss is catastrophic.' That trade-off is not crazy. It "
          "is the rational behavior of a system that has learned, "
          "early or repeatedly, that closeness is unreliable.")
    _p(B, "Strengths people miss: anxious individuals are often "
          "the most attuned partners in the room. They notice "
          "shifts in tone, body language, and emotional weather. "
          "In a calm, secure pairing, that sensitivity becomes "
          "warmth, not surveillance.")
    _p(B, "Costs: a never-resting threat detector is exhausting. "
          "False positives produce protest behavior (we will "
          "unpack that). Self-worth becomes hostage to partner "
          "responsiveness. Choices skew toward partners who "
          "trigger the system the most - which is usually the "
          "wrong partner.")

    _h2(B, "4.3 Avoidant (roughly 25% of adults)")
    _p(B, "Core experience: autonomy is the goal; closeness is "
          "engulfment. The system reads emotional demand as a "
          "threat to selfhood.")
    _p(B, "Internal logic: 'If I let the closeness fully in, I "
          "will lose myself, owe too much, or be controlled. "
          "Distance keeps me intact.' Like the anxious logic, it "
          "is not stupid. It is the rational behavior of a system "
          "that has learned, early or repeatedly, that closeness "
          "comes at a cost to autonomy.")
    _p(B, "Strengths people miss: avoidant individuals are often "
          "self-reliant, capable solo, good at boundaries with the "
          "outside world, and steady under stress that does not "
          "involve emotional intimacy. In a relationship with a "
          "secure partner, those traits become an asset.")
    _p(B, "Costs: avoidants tend to underestimate how much they "
          "rely on the partner emotionally, and overestimate their "
          "satisfaction. Common giveaways: idealizing past or "
          "unavailable partners, finding flaws to justify distance, "
          "avoiding 'us' language, treating vulnerability as risk. "
          "These are not character flaws; they are deactivating "
          "strategies, and they have a name because they are "
          "predictable.")

    _h2(B, "4.4 Disorganized / fearful-avoidant (smaller slice)")
    _p(B, "Core experience: I want closeness AND closeness is "
          "dangerous. Both systems fire at once. People flip "
          "between pursuit and withdrawal, sometimes within the "
          "same conversation.")
    _p(B, "This pattern is more common when early caregivers were "
          "themselves the source of fear - inconsistent, scary, "
          "or directly harmful. It is also more associated with "
          "trauma. It is harder to navigate because the conflict "
          "is internal, not just relational. Self-help frameworks "
          "are useful here, but professional support is often "
          "the more honest recommendation.")
    _br(B)


def add_part3_pairings(B):
    _h1(B, "5. How Styles Interact: The Dynamics of Pairings")
    _p(B, "Attachment style is not a fixed label on a person. It "
          "is a tendency that comes alive in interaction. Two "
          "anxious people behave differently together than an "
          "anxious paired with an avoidant. Map the pairings, and "
          "a lot of relationship behavior stops looking mysterious.")

    _h2(B, "5.1 Secure + anyone")
    _p(B, "A secure partner has a stabilizing effect across the "
          "board. With another secure, the relationship is calm "
          "and low-drama; conflict is resolved by talking. With an "
          "anxious partner, the secure absorbs the spikes, "
          "responds reliably, and over time the anxious nervous "
          "system de-escalates. With an avoidant partner, the "
          "secure does not chase, does not punish distance, and "
          "does not destabilize on small withdrawals - which "
          "paradoxically makes the avoidant safer to step in.")
    _p(B, "Bottom line: secure partners are not exotic. They are "
          "underweighted in dating because they generate fewer "
          "fireworks. The shift you can make today is to stop "
          "filtering them out as boring.")

    _h2(B, "5.2 Anxious + anxious")
    _p(B, "Two threat-detecting systems pointed at each other. "
          "Often very close, very intense, with frequent reassurance "
          "rituals. Can work, but the relationship spends a lot of "
          "energy on the connection itself rather than on living. "
          "Risk: the bond becomes the entire world; outside life "
          "thins out.")

    _h2(B, "5.3 Avoidant + avoidant")
    _p(B, "Two distance-keeping systems. Looks low-conflict from "
          "outside; can quietly starve emotionally. Often works "
          "for practical partnership (logistics, household, kids) "
          "but lacks the felt closeness that makes a relationship "
          "regenerative. Risk: drift, parallel lives, low "
          "satisfaction reported only after years.")

    _h2(B, "5.4 Anxious + avoidant: the pattern that hurts")
    _p(B, "This is the pairing the field talks about most because "
          "it is common, intense, and reliably miserable. It is "
          "worth understanding in detail because, statistically, "
          "this is the loop people get stuck in.")
    _p(B, "Why it is common: in single-person dating pools, secure "
          "people pair off earlier and more stably. Anxious and "
          "avoidant people stay in circulation longer, so they meet "
          "each other more often. Selection bias, not romance.")
    _p(B, "Why it feels intense: each system pushes the other's "
          "buttons. Anxious closeness-seeking activates avoidant "
          "distance-seeking, which activates anxious protest, "
          "which activates more avoidant distance, and so on. The "
          "highs of reconnection feel huge because the lows of "
          "perceived loss were huge. The brain learns to read "
          "this oscillation as 'passion'. It is not. It is "
          "intermittent reinforcement, the same mechanism that "
          "makes slot machines addictive.")
    _p(B, "Why it stays stuck: each partner keeps the other from "
          "experiencing what would update their model. The "
          "anxious never gets reliable closeness, so the model "
          "'closeness is unreliable' is confirmed. The avoidant "
          "never gets non-demanding closeness, so the model "
          "'closeness is suffocating' is confirmed. The pairing "
          "is a self-reinforcing simulation of each person's "
          "worst case.")
    _p(B, "Diagnostic signs you are in this loop:")
    _b(B, "Big, dramatic reconciliations after small triggers.")
    _b(B, "A persistent feeling of walking on eggshells, or a "
          "persistent feeling of being walked on eggshells around.")
    _b(B, "One partner constantly calibrates messages, timing, "
          "tone to avoid 'pushing' the other.")
    _b(B, "Conversations about the relationship itself escalate "
          "fast and resolve slowly.")
    _b(B, "Outsiders see the problem more clearly than you do.")
    _br(B)


def add_part4_protest(B):
    _h1(B, "6. Protest Behavior and Deactivating Strategies")
    _p(B, "These two terms do more practical work than almost any "
          "other concepts in the field. If you remember nothing else "
          "from this guide, remember to spot these in real time.")

    _h2(B, "6.1 Protest behavior (anxious side)")
    _p(B, "When the anxious system perceives distance and cannot "
          "tolerate it, it tries to force re-engagement. The form "
          "varies; the function is one and the same.")
    _b(B, "Excessive attempts to contact (calls, messages, "
          "showing up).")
    _b(B, "Withdrawal as a tactic ('I will go silent and they "
          "will notice and come back').")
    _b(B, "Score-keeping; bringing up old grievances during a "
          "small disagreement.")
    _b(B, "Hostile attention - picking a fight to force a "
          "response, any response.")
    _b(B, "Threats to leave that are not meant.")
    _b(B, "Making the partner jealous deliberately.")
    _p(B, "What looks like control or manipulation is often a "
          "panicked attachment system trying to restore proximity. "
          "That is not a justification. It is a description that "
          "lets you intervene at the right level. The fix is not "
          "to suppress the urge through willpower; it is to either "
          "(a) get the actual closeness need met by a partner who "
          "responds to plain requests, or (b) recognize that the "
          "current partner is not going to provide it and stop "
          "pretending the next intensified protest will change "
          "that.")

    _h2(B, "6.2 Deactivating strategies (avoidant side)")
    _p(B, "When the avoidant system perceives engulfment, it "
          "creates psychological distance. The behaviors look like "
          "preferences or personality, but they are predictable "
          "moves of a system trying to lower closeness pressure.")
    _b(B, "Focusing on small flaws in the partner ('the way they "
          "chew', 'their laugh') as reasons to feel less.")
    _b(B, "Idealizing an ex, a fantasy partner, or 'the one that "
          "got away'.")
    _b(B, "Keeping options open even after commitment ('I'm just "
          "not sure', for years).")
    _b(B, "Mistrust framed as 'realism' or 'just being careful'.")
    _b(B, "Avoidance of 'we' or future-tense talk.")
    _b(B, "Sudden need for solo time after a closeness peak (a "
          "great weekend reliably followed by emotional pullback "
          "on Monday).")
    _b(B, "Pseudo-intimate substitutes - flirting with others, "
          "porn or fantasy as primary outlet, work as identity.")
    _p(B, "Again: not character flaws, predictable moves. The fix "
          "is not 'try harder to want closeness'. The fix is to "
          "see that the discomfort is a signal of activation, not "
          "of incompatibility - and to learn to tolerate the "
          "signal without acting on it.")

    _h2(B, "6.3 Why this pair is so addictive")
    _p(B, "The most reliable predictor of what feels like love at "
          "first sight is not compatibility; it is whether someone "
          "activates your attachment system. For anxious-avoidant "
          "pairs, that activation is constant. The cocktail of "
          "stress hormones, dopamine on reconnection, and "
          "anticipatory anxiety produces a feeling that has been "
          "labeled 'passion' for centuries. It is not unique to "
          "couples; it is the same neurochemistry that runs slot "
          "machines, social media, and abusive relationships. "
          "Knowing this changes nothing about how it feels in the "
          "moment - and everything about whether you trust the "
          "feeling as a guide to a life decision.")
    _br(B)


def add_part5_dating(B):
    _h1(B, "7. Dating: How to Read a Partner Early")
    _p(B, "Most relationship pain is preventable at the selection "
          "stage. By weeks 4-8 of dating, an attachment pattern is "
          "usually visible to anyone willing to look. The catch is "
          "that the spike-seeking part of the brain is highly "
          "motivated to look away.")

    _h2(B, "7.1 Stop confusing activation with chemistry")
    _p(B, "When meeting someone new, ask: do I feel pulled in by "
          "interest in this specific human, or by uncertainty - "
          "wondering if they like me, decoding mixed signals, "
          "waiting for replies that come at random intervals? "
          "The first is interest. The second is your attachment "
          "system being activated by ambiguity. They feel almost "
          "the same in the body. They are not the same thing.")
    _p(B, "Practical filter: if a person produces calm interest "
          "rather than nervous spikes, give them more time before "
          "you decide they are 'not it'. The boring-secure first "
          "impression is the most underrated signal in dating.")

    _h2(B, "7.2 Behavioral signals to watch")
    _p(B, "These are not labels to slap on someone after one "
          "date. They are patterns to track over weeks.")
    _h3(B, "Signs of secure functioning (green)")
    _b(B, "Replies are timely and consistent, without being "
          "performative. The pattern is steady.")
    _b(B, "Plans are concrete and actually happen.")
    _b(B, "Direct in stating preferences and limits, without "
          "hostility.")
    _b(B, "Asks about you, listens, remembers details next time.")
    _b(B, "Comfortable with both closeness and time apart - "
          "neither clings nor disappears.")
    _b(B, "Talks about exes neutrally; takes some responsibility "
          "for past relationship outcomes.")
    _b(B, "Conflict, when it shows up, is handled by talking it "
          "through, not by silent treatment or escalation.")
    _h3(B, "Signs of anxious patterning (yellow)")
    _b(B, "Intense early enthusiasm, future-talk in week one.")
    _b(B, "Strong reactions to small delays.")
    _b(B, "Frequent reassurance-seeking, often disguised as "
          "compliments-fishing.")
    _b(B, "History of dramatic relationships described as "
          "'crazy' or 'toxic' - usually the partner's fault.")
    _h3(B, "Signs of avoidant patterning (yellow)")
    _b(B, "Reluctance to label or define anything.")
    _b(B, "Pattern of pulling back after good dates.")
    _b(B, "Talks about exes as 'too much' or 'not the one'; "
          "rarely owns their part of the breakup.")
    _b(B, "Strong stated need for independence, framed as a "
          "personality trait rather than negotiable.")
    _b(B, "Future-vague: 'we'll see', 'no labels', 'I don't "
          "plan that far'.")
    _h3(B, "Hard red flags (different category)")
    _p(B, "Keep these separate from attachment style. Lying, "
          "contempt, control, financial deception, violence, and "
          "addiction are not attachment problems and are not "
          "fixed by attachment work. If you see them, attachment "
          "framing is the wrong tool. Leave.")

    _h2(B, "7.3 The 'effective communication' test - on a date")
    _p(B, "A useful low-stakes experiment: state a small, real "
          "preference directly, and watch what happens. 'I'd "
          "actually rather we move dinner to 8 - 7 is tight for "
          "me.' Or: 'I had a good time and I'd like to see you "
          "again next week, does that work for you?' Note the "
          "response.")
    _b(B, "Secure response: easy yes, easy no, or easy "
          "counter-proposal. No drama, no scoring.")
    _b(B, "Anxious response: over-accommodation, then later "
          "resentment or score-keeping.")
    _b(B, "Avoidant response: vagueness, deflection, "
          "non-committal answers, or mild irritation at being "
          "asked directly.")
    _p(B, "One test is not diagnostic. Three or four are.")
    _br(B)


def add_part6_communication(B):
    _h1(B, "8. Effective Communication: A Practical Method")
    _p(B, "The slogan 'communicate better' is useless on its own. "
          "What actually helps is a small set of moves you can "
          "perform under pressure. Here is the method, distilled.")

    _h2(B, "8.1 The four properties of a good attachment message")
    _b(B, "Direct: name the actual issue, not a proxy.")
    _b(B, "Specific: about a behavior or situation, not a "
          "personality verdict.")
    _b(B, "Non-blaming: own your feeling, do not assign motive.")
    _b(B, "Need-focused: state what you want, not just what is "
          "wrong.")
    _p(B, "Bad: 'You never make time for me. You don't care.' "
          "(Vague, blaming, attributes motive, no clear ask.)")
    _p(B, "Better: 'When we go three days without seeing each "
          "other, I start to feel disconnected. Can we put "
          "something on the calendar this week?' (Specific, owns "
          "the feeling, clear request.)")

    _h2(B, "8.2 Why this is so hard for anxious / avoidant people")
    _p(B, "Anxious: stating a need directly feels dangerous because "
          "it surfaces the possibility that the answer is no. "
          "Protest behavior is a way to test the bond without "
          "stating the need plainly. The cost is that the partner "
          "experiences attack rather than request.")
    _p(B, "Avoidant: stating a need directly feels dangerous "
          "because it concedes that one is needed at all. "
          "Deactivation is a way to keep the felt independence "
          "intact. The cost is that the partner experiences "
          "rejection where there was, in reality, ordinary "
          "closeness pressure.")
    _p(B, "The fix is the same on both sides: lower the perceived "
          "stakes of stating the need by stating it earlier, "
          "smaller, and more often. Big requests delivered at low "
          "frequency hit hard. Small requests delivered "
          "continuously become a normal soundtrack.")

    _h2(B, "8.3 The 'first response' test")
    _p(B, "When you state a clean need, what your partner does in "
          "the first 30 seconds is data. It is not the whole "
          "person, but it is a real signal.")
    _b(B, "Helpful first responses: 'Tell me more.' 'I hear "
          "you.' 'Thanks for saying it directly.' 'Let me think "
          "for a moment.'")
    _b(B, "Unhelpful first responses: defensiveness, "
          "counter-attack, dismissal, mocking the request, "
          "going silent for days.")
    _p(B, "If, over months, the unhelpful responses outnumber the "
          "helpful ones at a 3-to-1 rate, the bottleneck is not "
          "your delivery. It is fit.")

    _h2(B, "8.4 Repair, not perfection")
    _p(B, "Healthy couples are not couples that never rupture. "
          "They are couples that repair quickly. The Gottman lab "
          "research, adjacent to attachment work, suggests that "
          "the speed and quality of repair after conflict "
          "predicts long-term outcomes better than the rate of "
          "conflict itself. Implication: stop optimizing for "
          "'no fights'. Start optimizing for 'fast, honest, "
          "non-punitive repair'.")
    _br(B)


def add_part7_change(B):
    _h1(B, "9. Can You Change Your Style? What Is Realistic")
    _p(B, "Short answer: yes, but slowly, and not by reading. The "
          "research term is 'earned secure' - people who started "
          "from anxious or avoidant roots and developed reliably "
          "secure functioning over years. It happens. It is not "
          "a personality transplant.")

    _h2(B, "9.1 What actually moves the needle")
    _b(B, "A long relationship with a secure partner. The single "
          "most reliable lever. The nervous system updates when "
          "it gets repeated, lived experience that contradicts "
          "the old model.")
    _b(B, "Therapy with a competent practitioner, especially "
          "approaches that work at the experiential level (EFT, "
          "AEDP, attachment-focused work) rather than purely "
          "cognitive ones.")
    _b(B, "Honest, sustained self-observation - not analysis, "
          "but noticing in real time when the system is "
          "activating, and choosing one different small action.")
    _b(B, "Friendships and community that provide secure-base "
          "functioning outside of romance. The romantic partner "
          "is not the only attachment figure available.")
    _b(B, "Body-level practices - sleep, exercise, breath work - "
          "because the attachment system is also a nervous-system "
          "thing, and a chronically depleted body amplifies every "
          "anxious or avoidant signal.")

    _h2(B, "9.2 What does not move the needle, despite popularity")
    _b(B, "Reading more books, including this one. Insight is "
          "necessary but not sufficient. Knowing why you do "
          "something does not, by itself, change what you do.")
    _b(B, "Self-help labels worn as identity ('I'm an anxious'). "
          "Useful at first; cage later.")
    _b(B, "Trying to fix an avoidant partner from inside an "
          "anxious-avoidant loop. Statistically, you will burn "
          "five years of your life and not move them an inch.")
    _b(B, "Willpower campaigns against your own urges without "
          "addressing what produces them.")

    _h2(B, "9.3 What change actually feels like from the inside")
    _p(B, "It is not 'I no longer feel anxious / avoidant'. It "
          "is more like: the spike still arrives, but it is "
          "smaller, you notice it earlier, the gap between "
          "feeling and acting widens, and you have a couple of "
          "alternative moves you did not have before. Over years, "
          "the baseline drifts. The drift is slow. Most people "
          "underestimate it because it is not dramatic.")
    _br(B)


def add_part8_hidden_assumptions(B):
    _h1(B, "10. What the Authors Quietly Assume")
    _p(B, "Every framework smuggles in unstated assumptions. "
          "Naming them does not invalidate the work; it tells you "
          "where to be careful when applying it.")

    _h2(B, "10.1 Three styles is enough")
    _p(B, "The popular three-bucket model is a simplification of "
          "research that treats attachment as two continuous "
          "dimensions (anxiety and avoidance), which produces a "
          "2D space rather than three discrete boxes. The three "
          "buckets are catchy and clinically useful, but real "
          "people sit on a continuum and shift contextually. "
          "Treat the labels as lenses, not as IDs.")

    _h2(B, "10.2 Style is mostly a stable individual trait")
    _p(B, "The book leans toward style as a relatively stable "
          "feature of the person. The newer research is more "
          "relational: style emerges in interaction with a "
          "specific partner and a specific moment. The same "
          "person can present anxious with one partner and "
          "secure with another. This matters because it means "
          "you are not condemned to your label, and also that "
          "you cannot fully assess your own style outside of a "
          "real relationship.")

    _h2(B, "10.3 Heterosexual, monogamous, Western default")
    _p(B, "Most of the popular framing - and many of the "
          "examples - assume a particular relationship structure. "
          "The underlying biology of attachment is broader than "
          "that, but applying the framework outside the default "
          "(non-monogamy, queer relationships, cross-cultural "
          "norms about closeness) requires more care than the "
          "popular write-up admits.")

    _h2(B, "10.4 Find a secure partner is achievable advice")
    _p(B, "The book's strongest practical advice - prefer "
          "secure partners - quietly assumes (a) the reader has "
          "access to a dating pool that contains them, (b) the "
          "reader can recognize them despite their non-spike "
          "vibe, and (c) the reader can tolerate the calm long "
          "enough to bond. All three are non-trivial. For "
          "people with deep anxious or avoidant roots, secure "
          "partners can feel literally repulsive at first.")

    _h2(B, "10.5 The reader is not the problem partner")
    _p(B, "Self-help frames invite the reader to identify with "
          "the protagonist. Attachment write-ups subtly cast the "
          "anxious reader as 'the one trying' and the avoidant "
          "as 'the one to manage'. In reality, both styles cause "
          "real harm in their own way. If you are avoidant, the "
          "framework is asking you to do work you may not have "
          "noticed was yours to do.")
    _br(B)


def add_part9_critique(B):
    _h1(B, "11. Where the Authors Are Right - And Where the Logic Bends")
    _p(B, "A fair audit. The framework deserves credit and "
          "scrutiny in the same breath.")

    _h2(B, "11.1 Where they are clearly right")
    _b(B, "Naming attachment as a biological system, not a "
          "personality flaw, is the single most useful reframe "
          "in popular psychology of the last 30 years. It "
          "removes shame and replaces it with mechanism.")
    _b(B, "The advice to weight attachment compatibility over "
          "spark in long-term partner choice is, on the "
          "evidence, correct.")
    _b(B, "The dependency paradox is real and well-supported: "
          "secure connection produces more, not less, "
          "exploration and resilience.")
    _b(B, "The tools for effective communication are sound and "
          "match independent findings from couples-therapy "
          "research.")
    _b(B, "The diagnosis of the anxious-avoidant trap is "
          "accurate and probably saves a non-trivial number of "
          "people from wasted years.")

    _h2(B, "11.2 Where the logic gets thinner")
    _b(B, "Style as primary explanation. The framework is "
          "powerful, and like all powerful frameworks it tends "
          "to explain everything in its own terms. Real "
          "relationships involve trauma, mental health, life "
          "stage, money, fertility, family-of-origin politics, "
          "and plain old values mismatch. Attachment is one "
          "lens, not the lens.")
    _b(B, "Determinism on partner selection. The advice 'choose "
          "secure' is correct on average, weak as a rule for an "
          "individual. People meet who they meet, and "
          "categorical filtering excludes humans who would be "
          "good for them.")
    _b(B, "Optimism about change vs honesty about cost. "
          "Becoming earned-secure is real, but it is years of "
          "work, not a chapter. The popular framing sometimes "
          "implies that recognizing the pattern is most of the "
          "battle. It is not. Recognizing it is move one of "
          "fifty.")
    _b(B, "The clean dichotomy avoidant vs anxious. Many "
          "people are mixed - anxious with closeness, avoidant "
          "with conflict; secure in long relationships, "
          "anxious in early dating. The clean labels are "
          "easier to teach but rougher than reality.")
    _b(B, "Asymmetric sympathy. Read carefully, the popular "
          "framing is more compassionate to anxious readers "
          "than to avoidant ones. Avoidance is treated as "
          "something to work around in a partner; anxiety is "
          "treated as something to soothe. The mirror image is "
          "rarer, and it should not be.")

    _h2(B, "11.3 What is missing entirely from most popular write-ups")
    _b(B, "The role of socioeconomic stress. Attachment "
          "behavior is much louder when the nervous system is "
          "depleted - sleep debt, money fear, chronic illness. "
          "Fixing the conditions sometimes does more than "
          "fixing the relationship.")
    _b(B, "Cultural variation. Acceptable closeness norms "
          "differ widely. What looks avoidant in one culture is "
          "neutral in another.")
    _b(B, "The fact that long-term partners shape each other's "
          "styles. You are not picking a static person; you "
          "are entering a long mutual-influence loop.")
    _br(B)


def add_part10_map(B):
    _h1(B, "12. A Connection Map of All Key Ideas")
    _p(B, "How the concepts in this guide hook into each other. "
          "Read the diagram top-to-bottom; arrows mean 'feeds "
          "into' or 'explains'.")

    _h3(B, "Layer 1: Biology")
    B.append(("mono", "[Evolved attachment system]"))
    B.append(("mono", "  |"))
    B.append(("mono", "  v"))
    B.append(("mono", "[Activated by closeness signals & threats]"))

    _h3(B, "Layer 2: Strategies")
    B.append(("mono", "                |"))
    B.append(("mono", "                v"))
    B.append(("mono", "  +-------------+--------------+"))
    B.append(("mono", "  |             |              |"))
    B.append(("mono", " SECURE      ANXIOUS        AVOIDANT"))
    B.append(("mono", "(reliable   (hyperactivate  (deactivate"))
    B.append(("mono", " base)       to seek          to keep"))
    B.append(("mono", "             closeness)       distance)"))

    _h3(B, "Layer 3: Visible behavior")
    B.append(("mono", "                |"))
    B.append(("mono", "                v"))
    B.append(("mono", "  Direct       Protest       Deactivating"))
    B.append(("mono", "  requests     behavior      strategies"))
    B.append(("mono", "  Repair       Score-keeping Idealizing exes"))
    B.append(("mono", "  Calm         Reassurance   Vagueness"))
    B.append(("mono", "  conflict     seeking       Pulling back"))

    _h3(B, "Layer 4: Pairings")
    B.append(("mono", "                |"))
    B.append(("mono", "                v"))
    B.append(("mono", "  Sec+Sec    : low drama, regenerative"))
    B.append(("mono", "  Sec+Anx    : anx calms over time"))
    B.append(("mono", "  Sec+Avo    : avo can step in safely"))
    B.append(("mono", "  Anx+Anx    : intense, can shrink the world"))
    B.append(("mono", "  Avo+Avo    : drift, low felt closeness"))
    B.append(("mono", "  Anx+Avo    : the addictive, painful loop"))

    _h3(B, "Layer 5: Levers (where you can act)")
    B.append(("mono", "                |"))
    B.append(("mono", "                v"))
    B.append(("mono", "  - Selection: weight style heavily"))
    B.append(("mono", "  - Reading partners early"))
    B.append(("mono", "  - Effective communication (4 properties)"))
    B.append(("mono", "  - Repair speed > zero conflict"))
    B.append(("mono", "  - Earned-secure work over years"))
    B.append(("mono", "  - Body & life conditions"))

    _p(B, "If you keep this five-layer map in your head, almost "
          "every situation in a relationship can be located on "
          "one of the layers - which tells you where to act. Most "
          "couples fight at layer 3 (behavior) without realizing "
          "the pressure is coming from layer 1 (biology) and the "
          "pattern was set at layer 4 (pairing). Solving things "
          "at the wrong layer is why so many fights repeat.")
    _br(B)


def add_part11_practical_plan(B):
    _h1(B, "13. A Practical 6-Week Plan")
    _p(B, "Pick the track that fits your situation. Each track is "
          "designed to be done in real time, not just read. The "
          "point is repetition; the point is not insight.")

    _h2(B, "Track A: I am single and dating")
    _h3(B, "Week 1 - Inventory")
    _b(B, "Write a one-page honest history of your last 3-5 "
          "relationships. For each: what activated me, what "
          "calmed me, why it ended, what I would now name as "
          "their style and mine.")
    _b(B, "Identify your default attraction signal. Be specific: "
          "'I get pulled in when someone is hot-and-cold' is "
          "more useful than 'I have bad taste'.")
    _h3(B, "Week 2 - Filter")
    _b(B, "Define 3 secure-functioning behaviors that, going "
          "forward, are non-negotiable on a third date. "
          "Examples: replies are consistent, plans actually "
          "happen, no contempt about exes.")
    _b(B, "Define 3 deactivating or protest behaviors that are "
          "automatic disqualifiers, no matter the chemistry.")
    _h3(B, "Week 3-4 - Field test")
    _b(B, "Date with the filters. When you feel the spike, "
          "ask: is this interest in the person, or activation "
          "from ambiguity?")
    _b(B, "Try the small-direct-request test on actual dates. "
          "Note the first response.")
    _h3(B, "Week 5 - Slow down a candidate")
    _b(B, "If someone passes the filters but feels 'flat', "
          "extend the runway. Three more dates. Calm is data, "
          "not absence.")
    _h3(B, "Week 6 - Decide and document")
    _b(B, "Either keep going with awareness, or close and "
          "return to week 1. Either way, write what you "
          "learned. Make the lesson explicit.")

    _h2(B, "Track B: I am in a relationship and want to improve it")
    _h3(B, "Week 1 - Locate")
    _b(B, "Identify, in writing, your style and your partner's "
          "most common mode. Use last month's events, not theories.")
    _b(B, "List the 3 most repeating fights. For each, name the "
          "underlying need on each side, not the surface topic.")
    _h3(B, "Week 2 - One direct request")
    _b(B, "Choose one small, real need. Use the four-property "
          "format. Deliver it once, plainly. Note the response.")
    _h3(B, "Week 3 - Repair drill")
    _b(B, "Next time a small rupture happens, attempt repair "
          "within 24 hours rather than waiting for it to fade. "
          "Repair = name what happened, own your share, ask "
          "what would help.")
    _h3(B, "Week 4 - Lower the stakes")
    _b(B, "Increase the rate of small requests so big ones "
          "stop carrying all the load.")
    _h3(B, "Week 5 - Honest audit")
    _b(B, "Of the last four weeks, did the partner respond to "
          "direct requests in helpful ways more often than not? "
          "If yes, you have a workable relationship. If no, "
          "consider what that means.")
    _h3(B, "Week 6 - Decide the trajectory")
    _b(B, "Three options: keep building, escalate to couples "
          "therapy, or honestly consider that the bottleneck is "
          "fit. Avoid option four (do nothing and hope).")

    _h2(B, "Track C: I think I have an anxious-avoidant loop")
    _b(B, "Week 1: write the loop in your own words. When does "
          "it start? Who pulls first? What is the recurring "
          "high and low?")
    _b(B, "Week 2: stop one move - either the protest or the "
          "deactivation - and observe what the relationship "
          "does without it. Not forever, just for a week.")
    _b(B, "Week 3: state the underlying need plainly, once, in "
          "the four-property format.")
    _b(B, "Week 4: collect evidence on responsiveness. Keep "
          "notes; memory is not reliable in loops.")
    _b(B, "Week 5: if responsiveness is real, build on it. "
          "If responsiveness is theatrical and reverts within "
          "days, that is your answer.")
    _b(B, "Week 6: stop optimizing the loop. Either commit to "
          "long structural work (therapy, often individual + "
          "couples), or commit to leaving. The third option, "
          "wait and see, is the option that loses years.")
    _br(B)


def add_part12_pareto(B):
    _h1(B, "14. The 20% That Gives 80% of the Results")
    _p(B, "If you do nothing else from this guide, do these.")
    _b(B, "1. In long-term partner choice, weight attachment "
          "compatibility above chemistry. Calm is not boring; "
          "it is the precondition for everything else.")
    _b(B, "2. Learn to tell activation apart from interest. "
          "Spike is not signal.")
    _b(B, "3. Make small, direct, specific, non-blaming "
          "requests early and often. Watch the first response.")
    _b(B, "4. Stop waiting for an avoidant partner to "
          "spontaneously transform inside an anxious-avoidant "
          "loop. They will not. The loop is the obstacle.")
    _b(B, "5. Optimize for repair speed, not for never "
          "fighting.")
    _b(B, "6. If you want to shift your own style, change the "
          "lived environment - not just your reading list. "
          "Secure relationships, body practices, and slow "
          "deliberate exposure to the discomfort beat any "
          "amount of self-analysis.")
    _b(B, "7. Treat the framework as a flashlight, not a "
          "courtroom. It is a way to see; it is not a verdict "
          "on you or your partner.")
    _br(B)


def add_appendix(B):
    _h1(B, "15. Appendix")

    _h2(B, "A. Glossary")
    _b(B, "Attachment system - an evolved emotional/behavioral "
          "system that regulates closeness with a primary "
          "caregiver, and later with a romantic partner.")
    _b(B, "Secure base - a person whose reliable availability "
          "lets you explore the world with less fear.")
    _b(B, "Safe haven - a person you can return to for comfort "
          "when distressed.")
    _b(B, "Activation - the state of the attachment system "
          "responding to perceived threat to closeness.")
    _b(B, "Hyperactivation - the anxious strategy: turn the "
          "system up, demand contact.")
    _b(B, "Deactivation - the avoidant strategy: turn the "
          "system down, suppress the need.")
    _b(B, "Protest behavior - actions that try to force "
          "re-engagement when distance is perceived.")
    _b(B, "Earned secure - someone who developed secure "
          "functioning later in life rather than from "
          "childhood.")
    _b(B, "Internal working model - the implicit map you carry "
          "of what closeness costs and what it gives.")
    _b(B, "Disorganized / fearful-avoidant - a mixed pattern "
          "where closeness is both wanted and feared.")

    _h2(B, "B. Self-assessment prompts")
    _p(B, "Answer in writing, in your own words. The point is "
          "not to score yourself; it is to make the patterns "
          "visible.")
    _b(B, "When the person I am dating takes longer than usual "
          "to reply, my first physical reaction is _____.")
    _b(B, "When a partner asks for more closeness than I "
          "expected, my first physical reaction is _____.")
    _b(B, "The last three relationships ended because _____ - "
          "and my honest share of that was _____.")
    _b(B, "I am drawn to people who _____. The pattern across "
          "the last five attractions is _____.")
    _b(B, "When I state a small, direct need to a partner, my "
          "internal experience right after is _____.")
    _b(B, "If I imagine a perfectly available, calm, "
          "responsive partner, my first reaction is "
          "(excitement / boredom / suspicion / relief / other) "
          "_____. What that reveals is _____.")
    _b(B, "The recurring fight in my last relationship was "
          "really about (closeness, autonomy, respect, fear of "
          "loss, control, fairness) _____.")

    _h2(B, "C. Green-flag / red-flag pocket cards")
    _h3(B, "Green flags (lean in)")
    _b(B, "Steady, predictable communication.")
    _b(B, "Direct requests; can hear yours without offense.")
    _b(B, "Owns part of past relationship outcomes.")
    _b(B, "Comfortable with both closeness and time apart.")
    _b(B, "Repairs after small ruptures within hours, not days.")
    _b(B, "Curious about you across topics, not just romance.")
    _h3(B, "Yellow flags (track over weeks)")
    _b(B, "Intense early future-talk after barely knowing you.")
    _b(B, "Strong reactions to minor delays or ambiguity.")
    _b(B, "Pattern of pulling back after good closeness.")
    _b(B, "Reluctance to define or label.")
    _b(B, "Talks about exes mostly as crazy or as 'too much'.")
    _h3(B, "Red flags (different category - leave)")
    _b(B, "Lying that is patterned, not occasional.")
    _b(B, "Contempt - mockery, eye-rolling, name-calling.")
    _b(B, "Control of money, friends, time, body.")
    _b(B, "Threats - to leave, to harm self, to harm you.")
    _b(B, "Any physical violence, ever.")
    _b(B, "Untreated addiction with denial.")
    _p(B, "Red flags are not attachment work. They are exit "
          "conditions. Do not let attachment framing turn them "
          "into 'just their style'.")

    _h2(B, "D. Suggested further reading and study")
    _p(B, "If you want to go deeper than this guide, look in "
          "these directions:")
    _b(B, "Mary Ainsworth's Strange Situation studies (the "
          "empirical foundation).")
    _b(B, "Hazan and Shaver's 1987 paper extending attachment "
          "to adult romance (the leap that started the field).")
    _b(B, "Mikulincer and Shaver, Attachment in Adulthood - "
          "the academic textbook of the field; dense but "
          "definitive.")
    _b(B, "Sue Johnson's work on Emotionally Focused Therapy "
          "(EFT) - the clinical application of attachment to "
          "couples.")
    _b(B, "Gottman lab research on conflict and repair - "
          "complementary, more behavioral, very practical.")
    _b(B, "Bessel van der Kolk's writing on trauma - useful "
          "when attachment patterns are entangled with trauma "
          "history.")

    _h2(B, "E. A closing note from the analyst")
    _p(B, "The most honest thing this framework can give you is "
          "not a label, a partner, or a happy ending. It is a "
          "vocabulary. With a vocabulary, you stop being inside "
          "the storm; you can name what is happening while it "
          "is happening. That alone, repeated for years, is "
          "what changes lives. Not the labels. The seeing.")
    _p(B, "Use the framework as a tool. Drop it when it stops "
          "being useful. The point was never the theory.")
