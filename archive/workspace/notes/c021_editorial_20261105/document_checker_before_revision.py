"""Document integrity checks, not mathematical verification. Use bounded runner."""
import json
import os
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
source = root/'proofs/quadratic_bose_chowla_integer_counts.md'
text = source.read_text(encoding='utf-8')
state_cap = int(os.environ['MATH_MAX_STATES'])
period_cap = int(os.environ['MATH_MAX_PERIOD_ENUMERATION'])
assert int(os.environ['MATH_MAX_PARALLEL_WORKERS']) >= 1
states = periods = 0


def check(test, label):
    global states
    if states >= state_cap:
        raise RuntimeError('state cap before document check')
    states += 1
    if not test:
        raise AssertionError(label)


blocks, inline, block = [], [], None
for lineno, line in enumerate(text.splitlines(), 1):
    check(not any(ord(c) < 32 for c in line), f'control character line {lineno}')
    if line.strip() == '$$':
        if block is None:
            block = []
        else:
            blocks.append('\n'.join(block))
            block = None
        continue
    if block is not None:
        block.append(line)
    else:
        check(line.count('$') % 2 == 0, f'inline delimiter line {lineno}')
        inline.extend(re.findall(r'\$([^$\n]+)\$', line))
check(block is None, 'unclosed display')
check(len(blocks) == 51, 'display count')
tags = re.findall(r'\\tag\{(\d+)\}', '\n'.join(blocks))
check(tags == [str(i) for i in range(1, 29)], 'numbered equations 1..28')
allowed = set('mathbb qquad quad beta operatorname bigl log theta bigr in mathcal tag ldots le cup cap ell max min text times sup varepsilon left frac right longrightarrow subset subseteq setminus substack varnothing Xi sum deg ge sqrt mapsto equiv pmod gamma Delta bar ne lambda begin not end delta mu alpha chi exp pi sim simeq longmapsto Longrightarrow eta epsilon lfloor rfloor tfrac widehat infty liminf to mathrm'.split())
commands = set()
for expression in blocks+inline:
    check(True, 'expression visit')
    commands.update(re.findall(r'\\([A-Za-z]+)', expression))
    depth = 0
    for match in re.finditer(r'(?<!\\)[{}]', expression):
        depth += 1 if match.group() == '{' else -1
        check(depth >= 0, 'unexpected closing TeX brace')
    check(depth == 0, 'unclosed TeX brace')
    check(not re.search(r'(?<!\\)\b(?:min|max|mu|gamma|theta|mathbb|mathcal)(?=[(_\s]|$)', expression),
          'bare TeX command word')
check(commands <= allowed, 'unreviewed TeX commands: '+repr(sorted(commands-allowed)))
sections = ['## 1. Definitions and main theorem', '## 2. Supporting lemmas',
            '## 3. Proof of the main theorem', '## 4. Corollaries and finite limitations',
            '## 5. Relation to prior results', '## 6. Verification and scope', '## References']
positions = [text.index(s) for s in sections]
check(positions == sorted(positions), 'requested section order')
for n in range(1, 7):
    check(text.count('### Lemma 2.'+str(n)+' (') == 1, 'unique lemma')
for n in range(1, 4):
    check(text.count('**Corollary 4.'+str(n)+' (') == 1, 'unique corollary')
check(not re.search(r'E864-C\d+|<!--|FOUNDATION_APPENDIX|LOCAL_LIMIT_APPENDIX', text),
      'standalone proof has workspace-only placeholder or claim label')
check('SELF_CHECKED' in text and 'no claim of literature novelty' in text,
      'verification/priority boundary')
references = re.findall(r'\]\((https://[^)]+)\)', text)
check(len(references) == 14, 'reference link count')
out = Path(os.environ['MATH_RUN_DIR'])/'outputs'
out.mkdir(exist_ok=True)
result = dict(status='PASS', document=str(source.relative_to(root)),
              display_expressions=len(blocks), inline_expressions=len(inline),
              numbered_equations=tags, tex_commands=sorted(commands),
              reference_links=len(references), requested_order=True,
              standalone_no_workspace_premises=True,
              mathematical_correctness_verified=False,
              checks='Delimiter, brace, control-character, command-spelling, numbering, section and link checks only.',
              states=states, periods=periods, workers=1, truncated=False,
              limits=dict(states=state_cap, periods=period_cap, workers=1))
(out/'document_checks.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result))
