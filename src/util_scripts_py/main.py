import typer

app = typer.Typer()


@app.command()
def alphabetical_sort(input_filename: str):
    typer.echo(f"alphabetical sort {input_filename} start")

    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sorted_lines = sorted(line.strip() for line in lines)

    with open(input_filename, "w", encoding="utf-8") as f:
        for line in sorted_lines:
            f.write(line + "\n")


def main():
    app()


if __name__ == "__main__":
    main()
