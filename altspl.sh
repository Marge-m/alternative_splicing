#!/usr/bin/env bash
samtools view -bS $1 | samtools sort - 1-sorted	#  first sam
samtools view -bS $2 | samtools sort - 2-sorted	#  second sam
cuffdiff $3 1-sorted.bam 2-sorted.bam -p 4		#  gtf
python cuff.py
python cuff2.py
python cuff3.py
sed 's/ /\t/g' file2writeminus.txt > minus.txt
sed 's/ /\t/g' filetowriteplus.txt > plus.txt
bedtools intersect -a minus.txt -b plus.txt -wo -v > minus.bed
bedtools intersect -a plus.txt -b minus.txt -wo -v > plus.bed
bedtools intersect -a minus.bed -b $4 -wo -f 1 > minusinpeaks.bed		#  peaks-introns
bedtools intersect -a plus.bed -b $4 -wo -f 1 > plusinpeaks.bed		#  peaks-introns
sort minusinpeaks.bed | uniq > minus_peaks.txt
sort plusinpeaks.bed | uniq > plus_peaks.txt
/usr/bin/python add_changes.py
