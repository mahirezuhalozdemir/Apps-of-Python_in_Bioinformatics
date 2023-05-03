#ilk kısım

from Bio.Blast import NCBIWWW
from Bio import SeqIO

record=SeqIO.read("dosyaadi.fasta",format="fasta")
result_handle = NCBIWWW.qblast("blastn","nt",record.format("fasta"))

with open("myblast.xml","w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()




