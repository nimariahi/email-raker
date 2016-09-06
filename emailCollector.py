#!/usr/bin/python

"""@package emailCollector

Collect e-mail addresses from any type of (potentially unstructured) text files
and output them as a single-column on stdout. Text files containing e-mails to
be excluded can also be provided.

An encoding of UTF-8 is assumed.

@author Nima Riahi <nimariahizrh@gmail.com>

"""


import sys
import re
import argparse
import os
import string


def extractEmails(str):
    """Extract all E-Mails found in a string.
    
    @param string The string containing e-mails in an unstructured way.
    
    @return set E-mails as strings.
    """

    
    # Remove non-printable characters
    # str = filter(lambda x: x in set(string.printable), str)
    
    str = str.decode('ascii', errors='ignore')
    
    
    match = re.findall(r'([a-z|A-Z|0-9|\.|\-|_]+@[a-z|A-Z|0-9|\.|\-|_]+\.[a-z]+)',str)
    
    # Select only unique elements (sets doen't allow duplicates)
    uemails = set()
    for w in match:
        uemails.add(w)
    
    return(uemails)
    

    
def collectEmails(filein, fileex=None):
    """Collect e-mails from unstructured text files
    
    @param filein Vector of strings containing the file names of the text files to scan for inclusion.
    @param fileex Vector of strings containing the file names of the text files to scan for exclusion.
    
    
    @return set A set of strings containing the collected e-mails.
    """

    
    def getEmails(filelist):
    
        emails = set()
        for fname in filelist:
            # Load file (Universal flag to handle end-of-line)
            strEmails = open(fname,'rU').read()
            em = extractEmails(strEmails)
            emails = emails.union(em)
        
        return(emails)
    

    emailsIn = getEmails(filein)
    
    if fileex==None:
        emailsEx = set()
    else:
        emailsEx = getEmails(fileex)
    

    # Remove exclude-emails from include-emails
    emails = [k for k in emailsIn if not(k in emailsEx)]
    
    return(emails)
    


def output(emails, outfname=None):
    """Write strings in the set to stdout.
    
    @param set The set of strings.
    
    @return Writes directly to stdout
    """
        
    for el in emails:
        sys.stdout.write('%s\n' % (el,))
    # f = open(outfname,'w')



def main():
    
    parser = argparse.ArgumentParser(description='Collect emails from unstructured files.')
    # parser.add_argument('--include-addr', '-i', nargs='+',
    #                     help='File name containing e-mail addresses to be collected.')
    parser.add_argument('--exclude-addr', '-e', nargs=1,
                        help='Name of file containing e-mail addresses to be excluded.',
                        default='')
    parser.add_argument('inputfiles', nargs='+')

    # Get arguments with the parser
    args = parser.parse_args()


    # Save them to variables
    filein = args.inputfiles
    fileex = args.exclude_addr
    
    # Change directory to the location where the executed function is stored
    os.chdir(os.path.dirname(sys.argv[0]))
        
    # Collect e-mails
    emails = collectEmails(filein, fileex)
    
    # Write elements of list to stdout
    output(emails)

    sys.exit(0)



if __name__ == '__main__':
    main()
    
    
    