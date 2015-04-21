import discogs_client
import yaml
import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + '../../../apis_helpers'))
import apis_helpers


def authenticate():
  credentials = apis_helpers.get_credentials('discogs')
  user_agent = credentials['app-name'] + '/' + credentials['app-version']
  filepath = 'config/APIs/discogs/access_token.yml'
  if not os.path.isfile(filepath):
    user_agent = credentials['app-name'] + '/' + credentials['app-version']
    client = discogs_client.Client(user_agent.decode('utf8'),
      consumer_key=credentials['consumer-key'].decode('utf8'),
      consumer_secret=credentials['consumer-secret'].decode('utf8')
    )
    
    token, secret, url = client.get_authorize_url()
    oauth_verifier = raw_input(('Browse {0} and paste the code here ' +
      '(this will only be necessary once): ').format(url)).decode('utf8')

    access_token, access_secret = client.get_access_token(oauth_verifier)
    data = {
      'access_token': access_token,
      'access_secret': access_secret
    }
    with open(filepath, 'w') as outfile:
      outfile.write(yaml.dump(data, default_flow_style=True))
  else:
    tokens = yaml.load(open(filepath, 'r'))
    client = discogs_client.Client(user_agent.decode('utf8'),
      consumer_key=credentials['consumer-key'].decode('utf8'),
      consumer_secret=credentials['consumer-secret'].decode('utf8'),
      token=tokens['access_token'].decode('utf8'),
      secret=tokens['access_secret'].decode('utf8')
    )
    
  return client


def save_fig(plt, name):
  apis_helpers.save_fig(plt, 'discogs', name)
