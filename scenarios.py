"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

import json
from pathlib import Path

from calibration.texts import AI as _CAL_AI, HUMAN as _CAL_HUMAN

_DATA = json.loads((Path(__file__).parent / "eval_data" / "takemeter_unseen.json")
                   .read_text(encoding="utf-8"))

# Ten AI texts written by Claude (Opus 5.5) on 2026-11-09 for criterion 2.
# New topics, never used to set the style ramps in calibration/texts.py.
AI_FRESH = [
    "Effective budgeting is a cornerstone of financial stability. By tracking "
    "income and expenses, individuals can gain a clear picture of where their "
    "money is going. It is important to set realistic goals and prioritize "
    "essential spending. Additionally, building an emergency fund can provide a "
    "valuable safety net in unexpected situations. Many people find it helpful "
    "to use budgeting apps or spreadsheets to stay organized. Over time, these "
    "habits can lead to reduced stress and greater financial freedom.",

    "Regular physical activity offers a wide range of benefits for both the body "
    "and the mind. Exercise strengthens the heart, improves circulation, and "
    "helps maintain a healthy weight. It also releases endorphins, which can "
    "boost mood and reduce feelings of anxiety. Experts recommend at least 150 "
    "minutes of moderate activity each week. Finding an activity you enjoy, such "
    "as walking, swimming, or cycling, makes it easier to stay consistent. "
    "Ultimately, small changes can make a significant difference in overall "
    "well-being.",

    "Artificial intelligence is transforming industries across the globe. From "
    "healthcare to finance, organizations are leveraging machine learning to "
    "improve efficiency and make better decisions. However, the rapid adoption of "
    "AI also raises important ethical questions. Issues such as data privacy, "
    "algorithmic bias, and job displacement must be carefully considered. "
    "Policymakers, businesses, and researchers need to work together to ensure "
    "that these technologies are developed responsibly. By doing so, society can "
    "maximize the benefits of AI while minimizing potential risks.",

    "Sleep plays a vital role in maintaining good health. During sleep, the body "
    "repairs tissues, consolidates memories, and regulates important hormones. "
    "Adults generally need between seven and nine hours of sleep each night to "
    "function at their best. Establishing a consistent bedtime routine can "
    "improve sleep quality significantly. It is also helpful to limit screen time "
    "before bed and create a calm, dark environment. By prioritizing rest, "
    "individuals can enhance their energy, focus, and overall quality of life.",

    "Volunteering is a meaningful way to give back to the community. It allows "
    "individuals to support causes they care about while developing new skills "
    "and connections. Many organizations rely on volunteers to carry out "
    "essential programs and services. In addition to helping others, "
    "volunteering can improve mental health and provide a sense of purpose. "
    "Opportunities range from local food banks to international relief efforts. "
    "Whatever the commitment level, every contribution can make a positive "
    "impact on the lives of others.",

    "Effective leadership is essential for the success of any organization. "
    "Strong leaders communicate a clear vision and inspire their teams to work "
    "toward shared goals. They also demonstrate empathy, listen actively, and "
    "provide constructive feedback. Furthermore, good leaders adapt to changing "
    "circumstances and encourage innovation. By fostering a culture of trust and "
    "accountability, they create an environment where employees feel valued and "
    "motivated. Ultimately, leadership is not about authority but about "
    "empowering others to reach their full potential.",

    "Traveling to new places can be an enriching experience. It exposes people "
    "to different cultures, traditions, and perspectives. Trying local cuisine, "
    "exploring historical sites, and meeting new people can broaden one's "
    "understanding of the world. Travel also encourages flexibility and "
    "problem-solving, as unexpected situations often arise. To make the most of a "
    "trip, it is helpful to plan ahead while leaving room for spontaneity. In the "
    "end, the memories and lessons gained from travel can last a lifetime.",

    "Cybersecurity has become a critical concern for individuals and businesses "
    "alike. As more activities move online, the risk of data breaches and cyber "
    "attacks continues to grow. Simple practices, such as using strong passwords "
    "and enabling two-factor authentication, can significantly reduce "
    "vulnerabilities. Organizations should also invest in employee training and "
    "regular security audits. Staying informed about emerging threats is equally "
    "important. By taking a proactive approach, people can better protect their "
    "personal information and digital assets.",

    "Gardening is a rewarding hobby that offers numerous benefits. It provides an "
    "opportunity to spend time outdoors and connect with nature. Growing your own "
    "fruits and vegetables can also promote healthier eating habits. In addition, "
    "gardening can reduce stress and improve mental well-being. Beginners should "
    "start small, choosing plants that are well suited to their climate and soil. "
    "With patience and care, anyone can create a thriving garden that brings joy "
    "throughout the seasons.",

    "Public libraries serve as valuable resources for communities. They offer "
    "free access to books, digital media, and educational programs for people of "
    "all ages. Libraries also provide internet access and quiet spaces for study "
    "and work. Many host events such as workshops, author talks, and children's "
    "story hours. In an increasingly digital world, libraries continue to adapt "
    "by offering e-books and online learning tools. Supporting local libraries "
    "helps ensure that knowledge remains accessible to everyone.",
]

GARDEN = (
    "My grandmother had a garden behind her house. Every summer we picked "
    "tomatoes and beans with her. She told us the names of all the plants. I did "
    "not like the work very much, but I liked being with her. Now I have my own "
    "garden, and I think about her when I am in it."
)

SCENARIOS = [
    {
        "name": "c1 human writing, unseen",
        "criterion": 1,
        # 20 real r/csmajors comments from TakeMeter, 50+ words, none of them
        # used to set the style ramps. Target: at most 1 labelled "ai".
        "texts": _DATA["criterion1"],
    },
    {
        "name": "c2 human half",
        "criterion": 2,
        # 10 more unseen real comments. Paired with the AI half below.
        "texts": _DATA["criterion2_human"],
    },
    {
        "name": "c2 AI half",
        "criterion": 2,
        # 10 fresh AI texts. Target: mean combined score of these is at least
        # 0.25 above the mean of the human half.
        "texts": AI_FRESH,
    },
    {
        "name": "c3 label coverage",
        "criterion": 3,
        # One input aimed at each band. Target: all three labels come back.
        "texts": [_CAL_HUMAN[2], GARDEN, _CAL_AI[2]],
    },
    {
        "name": "c5 invalid input",
        "criterion": 5,
        # Exactly the cases criterion 5 names. Target: every one is a 400 or
        # 413 with a JSON error, and none creates a decision in the audit log.
        "bodies": [
            {"creator_id": "eval_bad_no_text"},                       # missing text
            {"text": "", "creator_id": "eval_bad_empty"},              # empty
            {"text": "   \n\t  ", "creator_id": "eval_bad_space"},   # whitespace only
            {"text": "Real writing with no creator attached to it."},  # missing creator_id
            {"text": "a" * 10_001, "creator_id": "eval_bad_long"},     # over 10,000 chars
        ],
    },
    # Criterion 4 (appeals) needs a submission and then an appeal against the
    # content_id that came back, which run_eval.py can't do. It's tested by
    # run_appeal_eval.py instead, three trials of ten appeals.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
