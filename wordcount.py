import click


def count_words(text: str) -> int:
    return len(text.split())


@click.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
def main(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        click.echo(count_words(file.read()))


if __name__ == "__main__":
    main()
