import os
import json
import facebook
from argparse import ArgumentParser

def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    token = os.environ.get('Aq7YYLQNKABAB37fbZCOcRpIcsI2PxZBCayu97VYGIZC2BciWIj5daZCsZAENqCvgSfnpF8qbRNDcpkiipudTouRIzfdkr4vyCUFkCarHMkh8h2aQfZB7ZCNqcLGOlyh9RXJ52ZAqdSc0dqYE48DJ6DSYfiGGO504vXGZBMwRHJw6xTCoQJ6q248tvCVCOmZCOrgZDi')
    fields = ['id', 'name', 'about', 'likes', 'website', 'link']
    fields = ','.join(fields)

    graph = facebook.GraphAPI(token)
    page = graph.get_object(args.page, fields=fields)

    print(json.dumps(page, indent=4))
