@echo off
set EXP_DIR=./results_isic
set N_STEPS=1000
set RUN_NAME=run_1
set PRIOR_TYPE=f_phi_prior
set CAT_F_PHI=_cat_f_phi
set F_PHI_TYPE=f_phi_supervised
set MODEL_VERSION_DIR=diffmic_conditional_results/%N_STEPS%steps/nn/%RUN_NAME%/%PRIOR_TYPE%%CAT_F_PHI%/%F_PHI_TYPE%
set LOSS=diffmic_conditional
set TASK=isic
set N_SPLITS=1
set DEVICE_ID=0
set N_THREADS=8

python main.py --device %DEVICE_ID% --thread %N_THREADS% --loss %LOSS% --config %EXP_DIR%/%MODEL_VERSION_DIR%/logs/ --exp %EXP_DIR%/%MODEL_VERSION_DIR% --doc %TASK% --n_splits %N_SPLITS% --test --eval_best