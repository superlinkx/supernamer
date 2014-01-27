supernamer
==========

Command-line utitlity for renaming files by rulesets

SuperNamer has now hit release 0.1, download here: [http://superlinkx.github.io/supernamer/downloads/v0.1/sn.py](http://superlinkx.github.io/supernamer/downloads/v0.1/sn.py) Currently, it can detect whether you are giving it directories or files and automatically expand directories into their composite files. See known issues and in progress for more information.

    usage: sn.py [-h] [--discard INTEGER] [--keep INTEGER]
                 [--replace STRING,STRING] [--slice START,STOP] [--version]
                 [--dryrun] [--nonverbose]
                 files [files ...]
                 
    Rename files according to ruleset
        
    positional arguments:
      files                 Files to rename. If only two filenames and no rules
                            are given (not counting flags like -N and -D), the
                            first file will get the second file's name. Can be a
                            single file, list of files (with spaces between), or a
                            directory/directories (including .), but not mixed
                            
    optional arguments:
      -h, --help            show this help message and exit
      --discard INTEGER, -d INTEGER
                            Discards X characters from either the beginning or end
                            of the filename. Negative numbers indicate discarding
                            X characters from the end of the filename. First
                            character is index 0. (Equivalent of "[:INTEGER]" in
                            python)
      --keep INTEGER, -k INTEGER
                            Keeps X characters from either the beginning or end of
                            the filename. Negative numbers indicate keeping X
                            characters starting at the end of the filename. First
                            character is index 0. (Equivalent of "[INTEGER:]" in
                            python)
      --replace STRING,STRING, -r STRING,STRING
                            Replaces instances of first string with second string
                            in a filename
      --slice START,STOP, -s START,STOP
                            Slices between two integers, representing start and
                            stop values for a python slice. First character is
                            index 0.
      --version, -v         show program's version number and exit
      --dryrun, -D          Outputs filename changes, but doesn't touch the
                            filesystem
      --nonverbose, -N      Don't display verbose output


Known Issues:
-------------
- Subdirectories will automatically be renamed along with files
- If both files and directories are given as input, an error will be displayed. Proper error detection in progress.
- Cannot use the special number rule yet. Still working on an implementation for that

In Progress:
------------
- Special number rule implementation for replacing substrings and passing original numbers along (crucial for renaming tv shows for example)
- Error detection system and proper exceptions
- Code clean up
- Optional recursive renames
