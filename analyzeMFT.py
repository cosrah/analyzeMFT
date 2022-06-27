#!/usr/bin/python

try:
    from analyzemft import mftsession
except Exception as e:
    from .analyzemft import mftsession

if __name__ == "__main__":
    session = mftsession.MftSession()
    session.mft_options()
    session.open_files()
    session.process_mft_file()
    print('Done')
