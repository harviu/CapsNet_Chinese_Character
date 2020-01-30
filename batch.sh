#
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=8:gpus=1
#PBS -N UNET
#PBS -j oe
#PBS -A PAS1488

cd $HOME/CapsNet_Chinese_Character

ml python/3.6-conda5.2
source activate tsflow_pitzer
python capsulenet.py 
