
"""
"""

def function(*args, **wargs):
  """wargs[project, key]; issues implementeds are labeled confirmed"""
  from core import map_wargs
  map_wargs(**wargs)
  from pathlib import Path
  project = Path(project).resolve()
  from core import tag
  tag = tag(project)
  if tag.find('fatal') == 0:
    tag = 1
  else:
    tag = tag.strip()
  a = int(a.split('.')[0]) + 1
  from core import count_files_recursive as count
  b = count(project)
  from core import count_keys_in_files_recursive as count
  c = count(path=project, key='class')
  d = count(path=project, key='def')
  from core import count_issues_implemented as count
  e = count(path=project, mode=count.COMMIT_EQUALS_ISSUES, issues='confirmed')
  return f'{a}.{b}.{c}.{d}.{e}'
