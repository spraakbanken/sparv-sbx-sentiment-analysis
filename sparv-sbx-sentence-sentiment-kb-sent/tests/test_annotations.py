from sbx_sentence_sentiment_kb_sent.annotations import annotate_sentence_sentiment

from tests.testing import MemoryOutput, MockAnnotation


def test_annotate_sentence_sentiment(snapshot) -> None:  # noqa: ANN001
    output: MemoryOutput = MemoryOutput()
    word = MockAnnotation(
        name="<token>", values=["Han", "var", "glad", ".", "Rihanna", "uppges", "gravid", "."]
    )
    sentence = MockAnnotation(
        name="<sentence>", children={"<token>": [[0, 1, 2, 3], [4, 5, 6, 7]]}
    )

    annotate_sentence_sentiment(output, word, sentence)

    assert output.values == snapshot
