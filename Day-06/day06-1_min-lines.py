print(sum([len(i) for i in [''.join(set(i)) for i in [i.replace('\n', '') for i in open('input.txt').read().split('\n\n')]]]))