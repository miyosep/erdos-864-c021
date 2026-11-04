"""Validate the distributed repository, not the mathematical proof."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from limits import configure, deadline_check

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output')
args = parser.parse_args()
configure(args.output, 'repository')
root = Path(__file__).resolve().parents[1]
states = 0

def check(condition, label):
    global states
    deadline_check()
    states += 1
    if states > int(os.environ['MATH_MAX_STATES']):
        raise RuntimeError('state cap')
    if not condition:
        raise AssertionError(label)

digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
checksum_paths = []
for line in (root/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
    sha, name = line.split('  ', 1)
    path = (root/name).resolve()
    check(path.is_relative_to(root), 'checksum path outside repository')
    check(path.is_file() and digest(path) == sha, 'checksum '+name)
    checksum_paths.append(name)
check(len(checksum_paths) == len(set(checksum_paths)), 'duplicate checksum paths')
distributed=set()
for path in root.rglob('*'):
    rel=path.relative_to(root)
    if not path.is_file() or any(part in {'.git','__pycache__'} for part in rel.parts) or rel.parts[0]=='results':
        continue
    if rel.as_posix()=='SHA256SUMS.txt' or (rel.parts[0]=='paper' and path.suffix in {'.aux','.log','.out'}):
        continue
    distributed.add(rel.as_posix())
check(distributed == set(checksum_paths), 'checksum inventory covers distributed files')
finite = json.loads((root/'evidence/FINITE_CHECKS.json').read_text(encoding='utf-8'))
for record in finite['fresh_finite_runs']:
    path = root/record['public_output']
    check(path.is_file() and digest(path) == record['sha256'], 'recorded '+record['mode'])
    data = json.loads(path.read_text(encoding='utf-8'))
    check(data['status']=='PASS' and not data['truncated'], 'completed '+record['mode'])
check(not (root/'HISTORY.md').exists(), 'current-only navigation')
documents = [root/'README.md', root/'REPRODUCING.md', root/'evidence/README.md']
for directory in ['paper','review','code']:
    documents.extend((root/directory).glob('*.md'))
links = 0
for document in documents:
    content = document.read_text(encoding='utf-8')
    check('HISTORY.md' not in content and 'historical drafts' not in content.lower()
          and 'REPOSITORY_REVIEW.md' not in content, 'current-only reader guide '+document.name)
    for link in re.findall(r'\]\(([^)]+)\)', content):
        if re.match(r'https?://|#', link):
            continue
        path = (document.parent/link.split('#')[0]).resolve()
        check(path.is_relative_to(root) and path.exists(), f'link {document.name}: {link}')
        links += 1
paper = (root/'paper/main.md').read_text(encoding='utf-8')
tex = (root/'paper/main.tex').read_text(encoding='utf-8')
baseline = json.loads((root/'evidence/EQUATION_BASELINE.json').read_text(encoding='utf-8'))
blocks = lambda value: re.findall(r'^[ ]*\$\$[ \t]*\n(.*?)^[ ]*\$\$[ \t]*$', value, re.M|re.S)
compact = lambda values: [re.sub(r'\s+', '', value) for value in values]
displays = blocks(paper)
check(len(displays) == 51, '51 display expressions')
check([hashlib.sha256(value.encode('utf-8')).hexdigest() for value in compact(displays)]
      == baseline['displays_sha256'], 'unchanged display mathematics against frozen baseline')
check(compact(displays) == compact(re.findall(r'\\\[\s*\n?(.*?)\\\]', tex, re.S)), 'TeX matches Markdown mathematics')
check(re.findall(r'\\tag\{(\d+)\}', paper) == [str(i) for i in range(1,29)], '28 sequential labels')
check(r'\author{Sage Kim\\Peking University}' in tex and 'pdfauthor={Sage Kim}' in tex, 'author and affiliation')
check('AI assistance' not in paper and 'AI assistance' not in tex, 'requested manuscript presentation')
check('/blob/main/review/COMPUTATIONAL_SUPPLEMENT.md' in tex, 'PDF supplement destination')
check('/blob/main/manuscript/' not in tex, 'obsolete PDF destination absent')
check((root/'paper/main.pdf').read_bytes().startswith(b'%PDF-'), 'PDF exists')
result = dict(status='PASS', states=states, periods=0, workers=1, truncated=False,
    current_local_links=links, checksum_files=len(checksum_paths), recorded_finite_outputs=len(finite['fresh_finite_runs']),
    displayed_expressions=51, equation_tags=28, mathematical_correctness_verified=False)
(Path(os.environ['MATH_RUN_DIR'])/'outputs/repository_checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
