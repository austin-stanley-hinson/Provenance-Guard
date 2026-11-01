"""
Calibration inputs for Milestone 4: the four kinds the stylometry docstring
names, plus extra human samples so one odd text can't set a threshold.

Where each one came from matters, so it's written beside it:

    ai             written by Claude (Opus 5.5) on 2026-11-01 for this file,
                   in an ordinary assistant voice. Genuinely AI-generated.
    edited_ai      one of the `ai` texts with light human-style edits by
                   Claude: contractions, one short sentence, one typo, one
                   aside. Simulates someone touching up AI output.
    human          real r/csmajors comments, collected and labelled for
                   TakeMeter (project 3), 90+ words. Written by people.
    plain_human    real r/csmajors comments written plainly: short sentences,
                   common words, or non-native English. The writers the
                   model signal is most likely to accuse.

The human texts are loaded from `_takemeter_human.json`, copied out of
`../ai201-project3-takemeter-starter-v2026/labels.csv`.
"""

import json
from pathlib import Path

_HERE = Path(__file__).parent
_TM = json.loads((_HERE / "_takemeter_human.json").read_text())

AI = [
    "Remote work has fundamentally transformed the modern workplace. It offers "
    "employees greater flexibility and allows companies to access a wider talent "
    "pool. However, it also presents several challenges that organizations must "
    "address. Communication can become more difficult when teams are distributed "
    "across different time zones. Additionally, maintaining a strong company "
    "culture requires intentional effort and thoughtful planning. To succeed, "
    "organizations should invest in reliable collaboration tools, establish "
    "clear expectations, and prioritize regular check-ins. By taking these "
    "steps, companies can create a productive and engaging remote environment "
    "that benefits both employees and the business as a whole.",

    "Learning a new programming language can be a rewarding experience. It "
    "helps developers expand their skill set and approach problems from new "
    "perspectives. The first step is to understand the basic syntax and core "
    "concepts of the language. Next, it is important to practice by building "
    "small projects that apply what you have learned. Reading documentation and "
    "exploring open-source code can also provide valuable insights. Over time, "
    "consistent practice will help you become more confident and proficient. "
    "Ultimately, the key to success is patience, persistence, and a genuine "
    "curiosity about how things work.",

    "Climate change is one of the most pressing issues facing our world today. "
    "Rising global temperatures are leading to more frequent and severe weather "
    "events, including droughts, floods, and wildfires. These changes have "
    "significant impacts on ecosystems, agriculture, and human health. "
    "Addressing climate change requires a coordinated effort from governments, "
    "businesses, and individuals. Transitioning to renewable energy sources, "
    "improving energy efficiency, and protecting natural habitats are all "
    "important strategies. While the challenge is significant, there is still "
    "time to take meaningful action and build a more sustainable future for "
    "generations to come.",

    "Preparing for a technical interview requires a combination of knowledge, "
    "practice, and strategy. Candidates should start by reviewing fundamental "
    "data structures and algorithms, such as arrays, linked lists, trees, and "
    "graphs. It is also helpful to practice solving problems on platforms that "
    "simulate real interview conditions. In addition to technical skills, "
    "communication plays a crucial role. Interviewers want to understand how "
    "you think, so it is important to explain your reasoning clearly as you "
    "work through each problem. Finally, getting enough rest before the "
    "interview can help you stay focused and perform at your best.",

    "Reading regularly offers numerous benefits for both personal and "
    "professional growth. It improves vocabulary, enhances concentration, and "
    "strengthens critical thinking skills. Fiction allows readers to explore "
    "different perspectives and develop empathy for others. Nonfiction, on the "
    "other hand, provides practical knowledge and insights into a wide range of "
    "topics. Establishing a reading habit can be as simple as setting aside a "
    "few minutes each day. Over time, these small efforts can lead to "
    "significant improvements in knowledge and well-being. In conclusion, "
    "reading is a valuable activity that everyone should consider making a "
    "part of their daily routine.",

    "Time management is an essential skill for students who want to succeed "
    "academically. Balancing coursework, extracurricular activities, and "
    "personal responsibilities can be challenging without a clear plan. One "
    "effective strategy is to create a weekly schedule that outlines important "
    "deadlines and study sessions. Breaking large assignments into smaller, "
    "manageable tasks can also reduce stress and improve productivity. "
    "Additionally, it is important to minimize distractions, such as social "
    "media, during focused work periods. By developing strong time management "
    "habits, students can achieve their goals while maintaining a healthy "
    "balance in their lives.",
]

EDITED_AI = [
    # AI[0], touched up
    "Remote work has changed the workplace a lot. It gives people more "
    "flexibility and lets companies hire from a much wider pool. But it's not "
    "all upside. Communication gets harder when your team is spread across "
    "time zones — I've seen standups at 7am for half the team. Keeping a real "
    "company culture takes actual effort and planing. If you want it to work, "
    "invest in decent collaboration tools, set clear expectations, and do "
    "regular check-ins. Do that and remote can be productive for employees and "
    "the business both.",

    # AI[3], touched up
    "Prepping for a technical interview takes knowledge, practice and some "
    "strategy. Start by reviewing the basics: arrays, linked lists, trees, "
    "graphs. Practice on sites that feel like the real thing. Honestly though, "
    "communication matters just as much as getting the answer. Interviewers "
    "want to know how you think, so talk through your reasoning as you go "
    "(even when you're stuck). And get some sleep the night before. It helps "
    "more than one more leetcode problem will.",
]

_PLAIN_LONG = next(t for t in _TM["long"] if t.startswith("CIA does regular studies"))
HUMAN = [t for t in _TM["long"] if t is not _PLAIN_LONG]

PLAIN_HUMAN = [
    # Non-native English, short lines, no full stops on most of them.
    _PLAIN_LONG,
] + [t for t in _TM["mid"] if t.count(",") <= 2][:9]

SETS = {
    "ai": AI,
    "edited_ai": EDITED_AI,
    "human": HUMAN,
    "plain_human": PLAIN_HUMAN,
}
