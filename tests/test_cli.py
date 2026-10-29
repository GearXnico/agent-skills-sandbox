from click.testing import CliRunner

from wordcount.cli import count_words, main


def test_count_words():
    assert count_words("one two  three\n") == 3


def test_cli_prints_the_count(tmp_path):
    path = tmp_path / "note.txt"
    path.write_text("hello world", encoding="utf-8")
    result = CliRunner().invoke(main, [str(path)])
    assert result.output.strip() == "2"
