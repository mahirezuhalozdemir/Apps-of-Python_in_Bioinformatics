from Bio.Align import PairwiseAligner
aligner = PairwiseAligner()
from Bio.Seq import Seq
seq1 = Seq('ACCGT') #seq bu şekilde tanımlar
seq2 = Seq('ACG')

#Biopython 1.81'de aligner modu seq tanımlarken seçilmez
#aligner.mode = 'global'
#Bipython 1.81 versiyonunda Pairwise aligner kullanılır
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)
#format aligment kaldırılmıştır.


#2.kısım global aligment
aligner.mode = 'global'
seq1 = 'ACCGT'
seq2 = 'ACG'
alignment = aligner.align(seq1, seq2)
for aln in alignment:
    print('Alignment score:', aln.score)
    print(aln)


#3.kısım local aligment
#local alignment yapmak için aligner.mode değeri local olarak değiştirilir
aligner.mode = 'local'
seq1 = 'ACCGT'
seq2 = 'ACG'
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)

#4.kısım
aligner.mode = 'global'
aligner.match_score = 2 #her match için 2 puan eklenir
aligner.mismatch_score = -1 #her mismatch için 1 puan eksiltilir
seq1 = 'ACCGT'
seq2 = 'ACG'
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)


#5.kısım
aligner.mode = 'global'
aligner.match_score = 2 #match için 2 puan
aligner.mismatch_score = -1 #mismatch için -1 puan
aligner.open_gap_score = -0.5 #açık boşluk cezası -0.5 yeni bir boşluğun oluşturulması için cezadır
aligner.extend_gap_score = -0.1 #uzatma boşluğu cezası -0.1 ise mevcut bir boşluğu uzatmak için cezadır.
seq1 = 'ACCGT'
seq2 = 'ACG'
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)


#6.kısım
aligner.mode = 'global'
aligner.match_score = 5 #her match için 2 puan
aligner.mismatch_score = -4 #her mismatch için 1 puan eksiltilir
aligner.open_gap_score = -1 #açık boşluk cezası, yeni bir boşluğun oluşturulması için cezadır
aligner.extend_gap_score = -0.1 #uzatma boşluğu cezası ise mevcut bir boşluğu uzatmak için cezadır.
seq1 = 'A'
seq2 = 'T'
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)


#7.ksıım
aligner.mode = 'global'
aligner.match_score = 5 #her match için 5 puan
aligner.mismatch_score = -4 #her mismatch için -4 puan
aligner.open_gap_score = -3 #açık boşluk cezası için -3
aligner.extend_gap_score = -0.1 #uzatma boşluğu cezası için -0.1
seq1 = 'A'
seq2 = 'T'
alignments = aligner.align(seq1, seq2)
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)


#8.ksım
#Biopyhton Substitution matrix
from Bio.Align import substitution_matrices
matrix = substitution_matrices.load("BLOSUM62")
aligner.mode = 'global'
aligner.substitution_matrix=matrix
seq1 = 'KEVLA'
seq2 = 'EVL'

alignments = aligner.align(seq1, seq2)
alignment = alignments[0]
for aln in alignments:
    print('Alignment score:', aln.score)
    print(aln)




from math import log
def gap_function(x, y):  # x is gap position in seq, y is gap length
    if y == 0:  # No gap
        return 0
    elif y == 1:  # Gap open penalty
        return -2
    return - (2 + y/4.0 + log(y)/2.0)
aligner.match_score = 5
aligner.mismatch_score = -4
aligner.open_gap_score = gap_function()
aligner.extend_gap_score = gap_function()
#globalmc fonksiyonu Align modülü içinde bulunmmyr
alignment = aligner.align("ACCCCCGT", "ACG")

for aln in alignment:
    print('Alignment score:', aln.score)
