# coding:utf-8

import json
import requests


SPLASH_SCRIPT = """
function scroll_to(splash, x, y)
  local js = string.format(
    "window.scrollTo(%s, %s);", 
    tonumber(x), 
    tonumber(y)
  )
  return splash:runjs(js)
end


function get_doc_height(splash)
  return splash:runjs([[
    Math.max(
        Math.max(document.body.scrollHeight, document.documentElement.scrollHeight),
        Math.max(document.body.offsetHeight, document.documentElement.offsetHeight),
        Math.max(document.body.clientHeight, document.documentElement.clientHeight)
    )
  ]])
end


function scroll_to_bottom(splash)
  local y = get_doc_height(splash)
  return scroll_to(splash, 0, y)
end


function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  return {
    html = splash:html(),
  }
end
"""

ENDPOINT = 'http://localhost:8050' + '/execute'


def crawl(url):
    resp = requests.get(ENDPOINT, params={'url': url, 'lua_source': SPLASH_SCRIPT})
    text = json.loads(resp.text).get('html', '').encode('utf-8').decode('utf-8')
    print(text)


if __name__ == '__main__':
    url = 'https://www.baidu.com/'
    crawl(url)