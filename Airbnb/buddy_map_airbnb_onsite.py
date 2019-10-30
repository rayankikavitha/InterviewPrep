https://gist.github.com/nwadams/f4bfe01699c3e87f629c416978c4dd48


wishlists = [
  "U1,Amsterdam,Barcelona,London,Prague",
  "U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne",
  "U3,London,Boston,Amsterdam,Madrid",
  "U4,Barcelona,Prague,London,Sydney,Moscow",
  "U5,Amsterdam,Barcelona,London,Prague"
]



def scanwishlist(wishlists):
	d ={}
	for each in wishlists:
		items = each.split(',')
		d[items[0]] = [item for item in items[1:]]
	return d




def buddymap(wishlists, guest):
	bucket = scanwishlist(wishlists)
	if guest not in bucket:
		return -1
	guestitems = set(bucket[guest])
	countlist = len(bucket[guest])
	halflist = countlist//2
	preference =[]
	for k,v in bucket.items():
		if k != guest:
			matches = len(set(v).intersection(guestitems))
			preference.append((k,matches))
	#print (preference)
	final =[]
	for each in preference:
		if each[1] >= halflist:
			final.append(each)
	#print (final)
	final.sort(key =lambda x: -x[1])
	return final, bucket

def find_recommendation(  wishlists, guest):
	buddylist, bucket = buddymap(wishlists,guest)
	result = {}
	recomm = set()
	#print (bucket[guest])
	currentpref = set(bucket[guest])
	#print (currentpref)
	for each in buddylist:
		for item in bucket[each[0]]:
			recomm.add(item)
	return recomm - currentpref


print (find_recommendation(wishlists,'U5'))




print (buddymap(wishlists, 'U5'))









	