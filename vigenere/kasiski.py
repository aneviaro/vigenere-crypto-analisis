import math


def repeated_seq_pos(text, seq_len):
    seq_pos = {}
    for i, char in enumerate(text):
        next_seq = text[i:i + seq_len]
        if next_seq in seq_pos.keys():
            seq_pos[next_seq].append(i)
        else:
            seq_pos[next_seq] = [i]
    repeated = list(filter(lambda x: len(seq_pos[x]) >= 2, seq_pos))
    rep_seq_pos = [(seq, seq_pos[seq]) for seq in repeated]
    return rep_seq_pos


def get_spacings(positions):
    return [positions[i + 1] - positions[i] for i in range(len(positions) - 1)]


def fing_gcds(spacings):
    gcds = []
    for i in range(len(spacings)):
        for j in range(i + 1, len(spacings)):
            gcd = math.gcd(spacings[i], spacings[j])
            gcds.append(gcd)
    return gcds


def find_key_length(cyphertext):
    gcds = {}
    for i in range(3, 8):
        rsp = repeated_seq_pos(cyphertext, i)
        if rsp:
            seq_spc = []
            for _, positions in rsp:
                spacing = get_spacings(positions)
                for x in spacing:
                    if x not in seq_spc:
                        seq_spc.append(x)
            for gcd in fing_gcds(seq_spc):
                gcds[gcd] = gcds[gcd] + 1 if gcd in gcds.keys() else 1
        else:
            break
    gcds = sorted(gcds.items(), key=lambda kv: kv[1], reverse=True)
    return gcds[0][0] if gcds else 1
