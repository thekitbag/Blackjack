
# solve Mark's 22 puzzle                                   D Billings 2016-12-17

from pprint import pprint

def gen_sets (pznum, span):
    """Generate all sets of integers 1 - n summing to the target"""
    good, bad, sset = 0, 0, []
    for i in range(1, span+1):
        for j in range(i+1, span+1):
            for k in range(j+1, span+1):
                if pznum == (i + j + k):
                    good += 1
                    sset.append([i, j, k])
                else: bad += 1
    print "found %d sets of integers summing to %d, and %d fails" % (good, pznum, bad)
    return sset

def gen_cands (pznum, span):
    """Generate all 6-tuples of sset sets, filter out most that fail constraints"""
    sset = gen_sets(pznum, span)
    n = len(sset)
    cands, count = [], [0, 0, 0]
    for i1 in range(n):
      for i2 in range(n):
        for i3 in range(n):
          for i4 in range(n):
            for i5 in range(n):
              for i6 in range(n):
                  s1, s2, s3, s4, s5, s6 = sset[i1], sset[i2], sset[i3], sset[i4], sset[i5], sset[i6]
                  if ((5 == len(set(s1 + s2))) and (5 == len(set(s2 + s3))) and (5 == len(set(s3 + s4))) and
                      (5 == len(set(s4 + s5))) and (5 == len(set(s5 + s6))) and (5 == len(set(s6 + s1)))):
                      count[0] += 1
                      # if 0 == count[0] % 10000: print "count[0] =", count[0]
                      all = s1 + s2 + s3 + s4 + s5 + s6
                      if 12 == len(set(all)):
                          count[1] += 1
                          # if 0 == count[1] % 100: print "  count[1] =", count[1]
                          freq = [0 for x in range(20)]
                          for i in range(1, span+1):
                                fcount = all.count(i)
                                freq[fcount] += 1
                                # if [1, 6, 6, 0, 0, 0, 0] == freq:
                                if ((span - 12) == freq[0]) and (6 == freq[1]) and (6 == freq[2]):
                                    count[2] += 1
                                    # if 0 == count[2] % 10: print "    count[2] =", count[2]
                                    cand = [s1, s2, s3, s4, s5, s6]
                                    cands.append(cand)
    print 'counts =', count[0], count[1], count[2]
    print "found %d candidates in all" % (len(cands))
    return cands

def gen_solns (pznum, span):
    """Construct all solutions to Mark's 22 puzzle"""
    cands = gen_cands(pznum, span)
    soln = []
    for i in range(len(cands)):
        cand = [cands[i][-1]] + cands[i] + [cands[i][0]]
        outer, inner, excl, all = [], [], [], []
        for j in range(1, 7):
            for k in range(3):
                all.append(cand[j][k])
                if (cand[j][k] not in cand[j-1]) and (cand[j][k] not in cand[j+1]):
                    outer.append(cand[j][k])
                if (cand[j][k] in cand[j-1]) and (cand[j][k] not in cand[j+1]):
                    inner.append(cand[j][k])
        all = set(all)
        for m in range(1, span+1):
            if m not in all:
                excl.append(m)
        soln.append([excl, inner, outer])
    print "constructed %d solutions" % (len(soln))
    soln.sort()
    return soln

pznum, span = 23, 13
soln = gen_solns (pznum, span)
print "All %d solutions to the 1-%d %d-puzzle (excluded, inner ring, outer ring):" % (len(soln), span, pznum)
pprint(soln)

