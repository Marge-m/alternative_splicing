#!/usr/bin/env bash
samtools view -bS $1 | samtools sort - 1-sorted	#  first sam
samtools view -bS $2 | samtools sort - 2-sorted	#  second sam
cuffdiff $3 1-sorted.bam 2-sorted.bam -p 4		#  gtf
python filter_isoforms.py
python create_coords.py
python sort_changes.py
sed 's/ /\t/g' minus_changes.txt | cut -f2,3,4,5 | sed '1d' > minus.txt
sed 's/ /\t/g' plus_changes.txt | cut -f2,3,4,5 | sed '1d' > plus.txt
bedtools intersect -a minus.txt -b plus.txt -wo -v > minus.bed
bedtools intersect -a plus.txt -b minus.txt -wo -v > plus.bed
bedtools intersect -a minus.bed -b $4 -wo -f 1 > minusinpeaks.bed		#  peaks-introns
bedtools intersect -a plus.bed -b $4 -wo -f 1 > plusinpeaks.bed		#  peaks-introns
sort minusinpeaks.bed | uniq > minus_peaks.txt
sort plusinpeaks.bed | uniq > plus_peaks.txt
python add_changes.py
