import json


def remove_conditions(file_path: str) -> None:
    
    with open(file_path, 'r+') as f:
        templates = json.load(f)
        if 'mappings' not in templates:
            raise KeyError('The specified file does not contain mappings.')
        for i in range(len(templates['mappings'])):
            if 'conditions' in templates['mappings'][i]:
                templates['mappings'][i].pop('conditions')
    
    with open(file_path, "w") as nf:
        nf.write(json.dumps(templates, 
                            sort_keys=False, 
                            indent=2, 
                            separators=(',', ': ')))


def main(argv=None) -> int:
    remove_conditions('route_templates.json')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
