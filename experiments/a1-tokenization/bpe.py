"""Weekend 1 — A1: Byte-Pair Encoding from scratch.

Starter scaffold, NOT the solution (rule: implement before watching the
solution — struggle first). The test harness at the bottom already runs;
your job is to make the two TODOs pass it.

Gate:
  1. runs      — `python bpe.py` trains on SAMPLE and roundtrips cleanly
  2. broke it  — try a merge count of 0, or unicode outside the training
                 text; document what fails and why
  3. beginner  — writeup in concepts/A1-tokenization.md
  4. committed — code + writeup, one commit

Resource (after struggling): Karpathy, "Let's build the GPT Tokenizer".
"""

SAMPLE = (
    "low lower lowest newer newest wider widest "
    "the model does not read words the model reads tokens "
    "strawberry has three r letters but the model may not see them"
)


def train_bpe(text: str, num_merges: int) -> dict[tuple[int, int], int]:
    """Learn `num_merges` merge rules over the UTF-8 bytes of `text`.

    Returns {(token_a, token_b): new_token_id}, new ids starting at 256.

    TODO(weekend 1): count adjacent pairs -> merge the most frequent pair
    into a new token -> repeat.
    """
    raise NotImplementedError("weekend 1, saturday, hour 2")


def encode(text: str, merges: dict[tuple[int, int], int]) -> list[int]:
    """Bytes -> token ids, applying learned merges in training order.

    TODO(weekend 1).
    """
    raise NotImplementedError("weekend 1, saturday, hour 3")


def decode(ids: list[int], merges: dict[tuple[int, int], int]) -> str:
    """Token ids -> text. Inverse of encode; provided so the roundtrip
    test is unambiguous about the contract."""
    vocab = {i: bytes([i]) for i in range(256)}
    for (a, b), idx in merges.items():
        vocab[idx] = vocab[a] + vocab[b]
    return b"".join(vocab[i] for i in ids).decode("utf-8", errors="replace")


if __name__ == "__main__":
    try:
        merges = train_bpe(SAMPLE, num_merges=50)
        ids = encode(SAMPLE, merges)
        raw = len(SAMPLE.encode("utf-8"))
        assert decode(ids, merges) == SAMPLE, "roundtrip failed"
        print(f"bytes: {raw}  tokens: {len(ids)}  compression: {raw/len(ids):.2f}x")
        print("GATE 1 (it runs): PASS")
    except NotImplementedError as todo:
        print(f"scaffold ok — next: {todo}")
