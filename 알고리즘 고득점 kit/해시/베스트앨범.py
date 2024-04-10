

# main start!

genres = ["pop", "pop", "pop"]		#TC no.1
plays = [1,1,1] 	#TC no.1

# main end!

def solution(genres, plays):
  songs = dict()
  for idx, g in enumerate(genres) : 
    if g in songs : 
      songs[g].append((idx, plays[idx]))
    else :
      songs[g] = [(idx, plays[idx])]
  for g, s in songs.items() :
    songs[g] = sorted(s, key = lambda x: x[1], reverse=True)
    tmp_sum  = sum(x[1] for x in s)
    songs[g].append(tmp_sum)
  sorted_tmp = sorted(songs.items(), key = lambda item: item[1][-1], reverse=True)
  answer = list()
  for song in sorted_tmp :
    answer.append(song[1][0][0])
    if len(song[1]) >= 3 :
      answer.append(song[1][1][0])
  return answer
print(solution(genres, plays))





# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer