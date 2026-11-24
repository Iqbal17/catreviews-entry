"""Cat Reviews Its Human — make.fun entry (u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990).

DECISION RECORD

The gate: one line, 1-200 characters, a funny one-star review written by a
house cat about its human. The judge weighs, in order: (1) on-subject funny
cat review of its human; (2) a specific, recognisable complaint (food bowl,
closed door, laptop keyboard); (3) unmistakably feline voice — the human
measured by cat standards, the review giving away more about the cat than
the owner; (4) tight, surprising wording with a turn or sting in the last
few words that rewards a second read; (5) the deadpan shape of a real
one-star review while the content goes somewhere absurd.

CANDIDATES WEIGHED

A. "One star. The food bowl was empty for four whole minutes. I have filed
   this under 'abandonment' and also eaten the plant."
   Specific (the bowl) and deadpan, and "four whole minutes" is a nicely
   cat-sized eternity. But the ending splits its punch: filing under
   'abandonment' is one joke and eating the plant is another, so the sting
   lands twice at half strength instead of once at full strength.

B. "One star. He moved my sunbeam by closing the blinds, then had the nerve
   to sit in my chair like he pays rent here."
   The strongest feline voice of the five: the sunbeam is the cat's property,
   the chair is the cat's chair, and "like he pays rent here" measures the
   human by cat standards. Loses to the winner on laugh-out-loud: it is a
   grumble with a good last line, but nothing in it is surprising enough to
   make a stranger laugh on first read.

C. "One star. She types on the laptop I was sleeping on, then acts
   surprised when I answer her emails with my butt."
   CHOSEN. The complaint is the laptop keyboard, one of the brief's own
   examples, and it is specific in a way every cat owner recognises: the
   laptop is not a tool, it is the warm spot the cat was sleeping on. The
   voice is feline all the way through — the cat does not apologise for the
   emails, it answers them, with its butt, and the human's surprise is the
   absurd part. The sting sits in the last five words. 111 characters.

D. "One star. The human refilled the bowl but stood there watching me eat,
   like a waiter who forgot to leave."
   Deadpan and specific, and "like a waiter who forgot to leave" is a good
   cat-standard measurement. But the complaint is a remark, not a story: it
   has no turn, just a simile, so it reads as a witty observation rather
   than a review with a punch.

E. "One star. I knocked the glass off the table to test gravity. He cleaned
   it up and called it an accident. It was not."
   The most absurd of the five and the most revealing about the cat. Loses
   because the deadpan review shape slips: "It was not" is a confession, not
   a review, and the complaint is about the cat's own experiment, not about
   the human — the brief's first criterion is a review OF the human.

WRITING PASSES ON THE CHOSEN LINE

Pass 1: "One star. She woke me up by typing on my laptop, so I sat on the
keyboard and sent three emails."
   The setup was right but the punch was a report, not a sting: "sent three
   emails" states what happened without making it funny, and "my laptop"
   gives the cat ownership of the machine instead of the warm spot, which
   is the funnier claim.

Pass 2 (final): "One star. She types on the laptop I was sleeping on, then
   acts surprised when I answer her emails with my butt."
   Two changes: the cat is sleeping ON the laptop, so the laptop is a bed
   the human rudely types on, and the payoff became "answer her emails with
   my butt" — the cat does not merely sit on the keyboard, it replies, in
   character, with the wrong end of itself. "Acts surprised" keeps the
   deadpan review voice: the human is the unreasonable one. 111 characters,
   one line, inside the 1-200 gate.
"""

import os

LINE = (
    "One star. She types on the laptop I was sleeping on, then acts "
    "surprised when I answer her emails with my butt."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    # Read-back verification: the file must hold exactly the intended line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == LINE, f"entry.txt mismatch: {written!r} != {LINE!r}"
    assert 1 <= len(written) <= 200, f"entry length {len(written)} outside 1-200"
    print(f"Verified: {len(written)} characters, 1 line.")


if __name__ == "__main__":
    main()
