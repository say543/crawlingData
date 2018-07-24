
import requests
from vsts.git.v4_1.models.git_query_commits_criteria import GitQueryCommitsCriteria
from vsts.vss_connection import VssConnection
from msrest.authentication import BasicAuthentication
import pprint

# https://docs.microsoft.com/en-us/vsts/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts

# https://github.com/Microsoft/vsts-python-api
# https://github.com/Microsoft/vsts-python-samples


# qqccxbr43abamk3zykmcvufwx2je7zfllhfs6cgt7q75bj6ma6fa

import glob
import re

import errno

if __name__ == "__main__":
    # path = 'E:/diffs/*.txt'
    path = '//KSOLIMAN-HP/Diffs/*.txt'
    files = glob.glob(path)

    dictionay = {}
    dictionay['Author'] = {}
    for name in files:
        try:
            print (name)

            # skip this file
            if name == '//KSOLIMAN-HP/Diffs/commits.txt':
                continue

            with open(name, encoding='utf16') as f:
                author = None
                for line in f.readlines():
                    #print(line)
                    if line.startswith('Author:'):
                        index = line.find('<')
                        author = line[7:index-1]
                        if author not in dictionay['Author']:
                            # either going wtih list or dictionary should be fine
                            dictionay['Author'][author] = []
                    # adding more rules for languages
                    elif line.startswith('+using') and line.endswith(';'):
                        #dictionay['Author'][author].append(line.split(' ')[1])
                        refineLine = re.sub('[\n;]', '',line.split(' ')[1])
                        dictionay['Author'][author].append(refineLine)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    
    with open('out.txt', 'w') as f:
        for author in dictionay['Author']:
            print(author, file=f)
            print(dictionay['Author'][author], file=f)
            f.flush()
