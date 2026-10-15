#!/usr/bin/env python3
"""Validate the skill's static vector SVG subset. Does not assess appearance."""
import argparse
import math
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
ALLOWED = set('svg g defs title desc path rect circle ellipse line polyline polygon linearGradient radialGradient stop clipPath mask filter feGaussianBlur feDropShadow feOffset feFlood feComposite feMerge feMergeNode feBlend feColorMatrix feComponentTransfer feFuncR feFuncG feFuncB feFuncA use symbol'.split())
URL = re.compile(r'url\(\s*[\'"]?([^\s)\'\"]+)[\'"]?\s*\)', re.I)

def validate(path):
    errors = []
    try:
        source = path.read_text(encoding='utf-8')
        if re.search(r'<!DOCTYPE|<!ENTITY|<\?xml-stylesheet', source, re.I):
            return ['DTD, entities, and stylesheet processing instructions are unsupported']
        root = ET.fromstring(source)
    except (OSError, UnicodeError, ET.ParseError) as exc:
        return [str(exc)]
    if root.tag != f'{{{SVG}}}svg':
        errors.append('root must be svg in the SVG namespace')
    try:
        box = [float(v) for v in re.split(r'[\s,]+', root.get('viewBox', '').strip())]
        if len(box) != 4 or not all(math.isfinite(v) for v in box) or min(box[2:]) <= 0:
            raise ValueError()
    except ValueError:
        errors.append('viewBox requires four finite numbers and positive width/height')
    ids = set()
    refs = []
    drawable = False
    for element in root.iter():
        tag = element.tag.removeprefix(f'{{{SVG}}}')
        if tag not in ALLOWED:
            errors.append(f'unsupported element: {tag}')
        if tag in {'path', 'rect', 'circle', 'ellipse', 'line', 'polyline', 'polygon', 'use'}:
            drawable = True
        ident = element.get('id')
        if ident is not None:
            if not ident or re.search(r'\s', ident) or ident in ids:
                errors.append(f'empty, invalid, or duplicate ID: {ident!r}')
            ids.add(ident)
        for key, value in element.attrib.items():
            name = key.rsplit('}', 1)[-1]
            if name.lower().startswith('on') or name in {'style', 'src', 'base'}:
                errors.append(f'active or unsupported attribute: {name}')
            if name == 'href':
                if not value.startswith('#') or len(value) == 1:
                    errors.append('href must be a nonempty local fragment')
                else:
                    refs.append(value[1:])
            if name in {'aria-labelledby', 'aria-describedby'}:
                refs.extend(value.split())
            for target in URL.findall(value):
                if target.startswith('#') and len(target) > 1:
                    refs.append(target[1:])
                else:
                    errors.append(f'external or empty resource: {target}')
    if not drawable:
        errors.append('no vector geometry found')
    for ref in sorted(set(refs) - ids):
        errors.append(f'unresolved local reference: {ref}')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.files:
        errors = validate(path)
        failed |= bool(errors)
        print(f'{"FAIL" if errors else "PASS"} {path}')
        for error in errors:
            print(f'  {error}')
    return int(failed)

if __name__ == '__main__':
    sys.exit(main())
