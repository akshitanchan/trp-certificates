import argparse, subprocess, os.path, sys, shutil

def compress(input_file_path, output_file_path, power=0):
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    if not os.path.isfile(input_file_path):
        print("Error: Invalid path for input PDF file")
        sys.exit(1)

    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: Input file is not a PDF")
        sys.exit(1)

    gs = get_ghostscript_path()
    print("Compressing the PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call([gs, '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                    '-dPDFSETTINGS={}'.format(quality[power]),
                    '-dNOPAUSE', '-dQUIET', '-dBATCH',
                    '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done. File has been compressed.")


def get_ghostscript_path():
    gs_names = ['gs', 'gswin32', 'gswin64']
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(f'No GhostScript executable was found on path ({"/".join(gs_names)})')


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('input', help='Relative or absolute path of the input PDF file.')
    parser.add_argument('-o', '--out', help='Relative or absolute path of the output PDF file.')
    parser.add_argument('-c', '--compress', type=int, help='Compression level from 0 to 4.')
    parser.add_argument('-b', '--backup', action='store_true', help="Backup the old PDF file.")
    parser.add_argument('--open', action='store_true', default=False,
                        help='Open PDF after compression.')
    args = parser.parse_args()

    if not args.compress:
        args.compress = 2

    if not args.out:
        args.out = 'temp.pdf'

    compress(args.input, args.out, power=args.compress)

    if args.out == 'temp.pdf':
        if args.backup:
            shutil.copyfile(args.input, args.input.replace(".pdf", "_BACKUP.pdf"))
        shutil.copyfile(args.out, args.input)
        os.remove(args.out)

    if args.open:
        if args.out == 'temp.pdf' and args.backup:
            subprocess.call(['open', args.input])
        else:
            subprocess.call(['open', args.out])

if __name__ == '__main__':
    main()
