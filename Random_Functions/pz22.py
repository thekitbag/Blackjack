
# solve Mark's 22 puzzle                                   D Billings 2016-12-10

def gen_sets ():
    """Generate all sets of integers 1-13 summing to 22"""
    good, bad, s22 = 0, 0, []
    for i in range(1, 14):
        for j in range(i+1, 14):
            for k in range(j+1, 14):
                if 22 == (i + j + k):
                    good += 1
                    s22.append([i, j, k])
                else: bad += 1
    print "found %d sets of integers summing to 22, and %d fails" % (good, bad)
    return s22

def gen_cands1 ():
    """Generate all 6-tuples of s22 sets, filter out most that fail constraints"""
    s22 = gen_sets()
    n = len(s22)
    cands, count = [], [0, 0, 0]
    for i1 in range(n):
      s1 = s22[i1]
      for i2 in range(n):
        if 5 == len(set(s1 + s22[i2])):
          s2 = s22[i2]
          for i3 in range(n):
            if 5 == len(set(s2 + s22[i3])):
              s3 = s22[i3]
              for i4 in range(n):
                if 5 == len(set(s3 + s22[i4])):
                  s4 = s22[i4]
                  for i5 in range(n):
                    if 5 == len(set(s4 + s22[i5])):
                      s5 = s22[i5]
                      for i6 in range(n):
                        if 5 == len(set(s5 + s22[i6])):
                          s6 = s22[i6]
                          if 5 == len(set(s6 + s1)):
                            count[0] += 1
                            if 6 == len(set([i1, i2, i3, i4, i5, i6])):
                              count[1] += 1
                              if 12 == len(set(s1 + s2 + s3 + s4 + s5 + s6)):
                                count[2] += 1
                                cand = [s1, s2, s3, s4, s5, s6]
                                print "found candidate %d %d %d %d %d %d" % (i1, i2, i3, i4, i5, i6)
                                print cand
                                cands.append(cand)
    print 'counts =', count[0], count[1], count[2]
    print "found %d candidates in all" % (len(cands))
    return cands

def gen_cands ():
    """Generate all 6-tuples of s22 sets, filter out most that fail constraints"""
    s22 = gen_sets()
    n = len(s22)
    cands, count = [], [0, 0, 0]
    for i1 in range(n):
      s1 = s22[i1]
      for i2 in range(n):
        if 5 == len(set(s1 + s22[i2])):
          s2 = s22[i2]
          all = s1 + s2
          for i3 in range(n):
            if 5 == len(set(s2 + s22[i3])) and 7 == len(set(all + s22[i3])):
              s3 = s22[i3]
              all += s3
              for i4 in range(n):
                if 5 == len(set(s3 + s22[i4])) and 9 == len(set(all + s22[i4])):
                  s4 = s22[i4]
                  all += s4
                  for i5 in range(n):
                    if 5 == len(set(s4 + s22[i5])) and 11 == len(set(all + s22[i5])):
                      s5 = s22[i5]
                      all += s5
                      for i6 in range(n):
                        if 5 == len(set(s5 + s22[i6])) and 12 == len(set(all + s22[i6])):
                          s6 = s22[i6]
                          all += s6
                          if 5 == len(set(s6 + s1)):
                            count[0] += 1
                            if 6 == len(set([i1, i2, i3, i4, i5, i6])):
                              count[1] += 1
                              freq = [0 for x in range(20)]
                              for i in range(1, 14):
                                fcount = all.count(i)
                                freq[fcount] += 1
                              # if [1, 6, 6, 0, 0, 0, 0] == freq:
                              if (1 == freq[0]) and (6 == freq[1]) and (6 == freq[2]):
                                count[2] += 1
                                cand = [s1, s2, s3, s4, s5, s6]
                                # print "found candidate %d %d %d %d %d %d" % (i1, i2, i3, i4, i5, i6)
                                # print cand
                                cands.append(cand)
    print 'counts =', count[0], count[1], count[2]
    print "found %d candidates in all" % (len(cands))
    return cands

def gen_solns ():
    """Construct all solutions to Mark's 22 puzzle"""
    # does not filter out redundant solutions (i.e. rotational or counter-clockwise symettries)
    # only seven (7) distinct solutions, with unused center peg of 3, 3, 4, 4, 6, 6, or 8
    cands = gen_cands()
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
        for m in range(1, 14):
            if m not in all:
                excl.append(m)
        soln.append([excl, inner, outer])
    print "constructed %d solutions" % (len(soln))
    soln.sort()
    return soln


"""
>>> soln = gen_solns()
found 18 sets of integers summing to 22, and 268 fails
counts = 535 447 10
found 10 candidates in all
constructed 10 solutions
>>> pprint(soln)
[[[3], [1, 9, 7, 13, 4, 10], [12, 6, 2, 5, 8, 11]],
 [[3], [13, 5, 11, 1, 12, 2], [4, 6, 10, 9, 8, 7]],
 [[4], [7, 6, 11, 1, 8, 12], [9, 5, 10, 13, 2, 3]],
 [[4], [13, 2, 12, 1, 11, 6], [7, 8, 9, 10, 5, 3]],
 [[4], [13, 6, 11, 1, 12, 2], [3, 5, 10, 9, 8, 7]],
 [[6], [1, 12, 7, 13, 4, 10], [9, 3, 2, 5, 8, 11]],
 [[6], [13, 4, 10, 1, 12, 7], [5, 8, 11, 9, 3, 2]],
 [[6], [13, 7, 12, 1, 10, 4], [2, 3, 9, 11, 8, 5]],
 [[6], [13, 8, 2, 9, 10, 5], [1, 12, 11, 3, 7, 4]],
 [[8], [13, 6, 12, 1, 10, 7], [3, 4, 9, 11, 5, 2]]]
>>> 
"""

