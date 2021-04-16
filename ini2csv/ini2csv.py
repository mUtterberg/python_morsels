import argparse


def main():
    """Controlling function"""

    parser = argparse.ArgumentParser()
    parser.add_argument('ini_path')
    parser.add_argument('csv_path')
    parser.add_argument('--collapsed', action='store_true')


if __name__ == '__main__':
    main()
