import hashlib

#Do not change the name of this class
class MerkleTreeCalculator:
    #use this function for hashing a file
    def sha256sum(self, filename):
        h = hashlib.sha256()
        with open(filename, 'rb', buffering=0) as f:
            for b in iter(lambda: f.read(128 * 1024), b''):
                h.update(b)
        return h.hexdigest()

	#Do not change the name of this function
    def calculate_merkle_root(self):
        N = 20
        hashes0 = []
        hashes1 = []
        hashes2 = []
        hashes3 = []
        hashes4 = []
        for i in range(N):
            hashes0.append(sha256sum('resource/file'+str(i+1)+'.txt'))
        for i in range(19):
            if i%2==0:
                h = hashlib.sha256()
                h.update((hashes0[i]+hashes0[i+1]).encode())
                hashes1.append(h.hexdigest())
        for i in range(9):
            if i%2==0:
                h = hashlib.sha256()
                h.update((hashes1[i]+hashes1[i+1]).encode())
                hashes2.append(h.hexdigest())
        hashes2.append(hashes2[4])
        for i in range(5):
            if i%2==0:
                h = hashlib.sha256()
                h.update((hashes2[i]+hashes2[i+1]).encode())
                hashes3.append(h.hexdigest())
        hashes3.append(hashes3[2])
        for i in range(3):
            if i%2==0:
                h = hashlib.sha256()
                h.update((hashes3[i]+hashes3[i+1]).encode())
                hashes4.append(h.hexdigest())
        h = hashlib.sha256()
        h.update((hashes4[0]+hashes4[1]).encode())
        root = h.hexdigest()
	return root
