"""CLI entrypoint for open_app."""

from open_app import get_status


def main() -> None:
    """Run the CLI command."""
    print(get_status())


if __name__ == "__main__":
    main()
