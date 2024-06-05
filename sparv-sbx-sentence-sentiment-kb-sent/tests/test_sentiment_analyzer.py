from typing import Optional

import pytest
from sbx_sentence_sentiment_kb_sent.sentiment_analyzer import SentimentAnalyzer


@pytest.fixture(name="sentiment_analyzer", scope="session")
def fixture_sentiment_analyzer() -> SentimentAnalyzer:
    return SentimentAnalyzer.default()


def test_neutral_text(sentiment_analyzer: SentimentAnalyzer) -> None:
    text = "Vi hoppas och tror att detta också snabbt ska kunna komma på plats , säger Garborg .".split(
        " "
    )

    actual = sentiment_analyzer.analyze_sentence(text)

    actual = remove_scores(actual)
    expected = "|NEUTRAL|"

    assert actual == expected


def remove_scores(actual: Optional[str]) -> Optional[str]:
    """Remove scores."""
    if not actual:
        return actual
    return "|".join(x.split(":")[0] for x in actual.split("|"))


def test_issue_10(sentiment_analyzer: SentimentAnalyzer, snapshot) -> None:  # noqa: ANN001
    text = """Frisinnade landsföreningen, som på allt sätt vill verka till främjande af ett sådant resultat, anser, att den förestående valkampanjen, förutom kring den politiska rösträttsfrågan såsom den gifna hufvudfrågan, bör koncentrera sig särskildt kring följande uppgifter:

att till Andra kammaren må sändas män, hvilka - särskildt med hänsyn till statsbudgetens oerhörda stegring - vilja häfda den sunda sparsamhetens grundsatser i vår statshushållning;

att till Andra kammaren sändas män, hvilka - sedan riksdagen antagit en progressiv inkomstskatt i förening med obligatorisk själfdeklaration - vilja verka för bevillningsförordningens omarbetande i enlighet med
dessa sålunda erkända grundsatser och därvid jämväl beakta, att taxeringsförfarandet äfven för icke deklarationsskyldige måtte blifva fullt betryggande;

att till Andra kammaren sändas män, hvilka äro beslutna att verka för en effektiv begränsning af den kommunala röstskalan;

att till Andra kammaren sändas män, hvilka - såsom en nödvändig konsekvens af 1901 års beslut i försvarsfrågan - vilja verka för en grundlig omarbetning af krigslagarne i tidsenlig och human riktning;

att till Andra kammaren sändas män, hvilka äro beslutna att verka för folkskolans sunda utveckling och närmast för att äfven folkskolorna i -likhet med de allmänna läroverkan måtte erhålla sin särskilda öfverstyrelse;

att till Andra kammaren sändas män, som vilja arbeta mot öfverhandtagande af bolagens jordvälde och för vidmakthållande och stärkande af en själfägande jordbrukande befolkning samt mot bolagsmakten i den kommunala styrelsen;

att till Andra kammaren sändas män, hvilka fullt behjärta arbetarefrågans utomordentliga betydelse och särskildt såsom närmaste mål vilja verka för upprättande af ett statsdepartement för arbetarelagstiftning och därmed sammanhängande ärenden anordnande af opartisk medling i arbetstvister samt invaliditets- och ålderdomspensionering, och hvilka bestämdt motsätta sig all ensidig strafflagstiftning såsom botemedel mot sociala missförhållanden;

att till Andra kammaren sändas män, hvilka i frågor sådana som näringslifvets höjande, främjande af det mindre jordbruket, utveckling af egna hensrörelsen, ny arrendelagstiftning, humanare fattigvårdslagstiftning, äfvenson tidsenlig lönereglering för de s.k. lägre statstjänarne, vilja nedlägga ett allvarligt och ihärdigt arbete för att få till stånd goda och gagnande resultat;

samt slutligen att till Andra kammaren sändas män, hvilka på nykterhetslagstiftningens viktiga.""".split(
        " "
    )

    actual = sentiment_analyzer.analyze_sentence(text)

    assert actual == snapshot
