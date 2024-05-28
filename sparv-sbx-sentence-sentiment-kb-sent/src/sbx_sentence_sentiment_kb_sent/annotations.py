"""Sparv annotator."""

from sparv import api as sparv_api  # type: ignore [import-untyped]

from sbx_sentence_sentiment_kb_sent.sentiment_analyzer import SentimentAnalyzer

logger = sparv_api.get_logger(__name__)


@sparv_api.annotator("Sentiment analysis of sentences", language=["swe"])
def annotate_sentence_sentiment(
    out_sentence_sentiment: sparv_api.Output = sparv_api.Output(
        "<sentence>:sbx_sentence_sentiment_kb_sent.sbx-sentence-sentiment--kb-sent",
        # cls="sbx_sentence_sentiment_kb_sent",
        description="Sentiment analysis of sentence with KBLab/robust-swedish-sentiment-multiclass",  # noqa: E501
    ),
    word: sparv_api.Annotation = sparv_api.Annotation("<token:word>"),
    sentence: sparv_api.Annotation = sparv_api.Annotation("<sentence>"),
) -> None:
    """Sentiment analysis of sentence with KBLab/robust-swedish-sentiment-multiclass."""
    sentences, _orphans = sentence.get_children(word)
    token_word = list(word.read())
    out_sentence_sentiment_annotation = sentence.create_empty_attribute()

    analyzer = SentimentAnalyzer.default()

    logger.progress(total=len(sentences))  # type: ignore
    for sent_i, sent in enumerate(sentences):
        sent_to_tag = [token_word[token_index] for token_index in sent]
        out_sentence_sentiment_annotation[sent_i] = analyzer.analyze_sentence(sent_to_tag)

    out_sentence_sentiment.write(out_sentence_sentiment_annotation)
