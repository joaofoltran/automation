#!/bin/bash

############################################################
# Creator: João Vítor Foltran
# Functions for ORACLE user to set environment variables.
############################################################

DEFAULT(){
  export USER_BIN=/home/${USER}/bin
  export ORACLE_BASE="/u01/app/oracle"
  export PATH=${PATH}:${ORACLE_HOME}/bin:${ORACLE_HOME}/OPatch:${USER_BIN}
}

PONT() {
  export ORACLE_HOME="/u01/app/oracle/product/11.2.0/pont_home"
  export ORACLE_SID=PONT
  DEFAULT
}

CREDFLOW() {
  export ORACLE_HOME="/u01/app/oracle/product/11.2.0/cred_home"
  export ORACLE_SID=CREDFLOW
  DEFAULT
}

HOMOPONT() {
  export ORACLE_HOME="/u01/app/oracle/product/11.2.0/dev_home"
  export ORACLE_SID=HOMOPONT
  DEFAULT
}

IBRACRED() {
  export ORACLE_HOME="/u01/app/oracle/product/11.2.0/dev_home"
  export ORACLE_SID=IBRACRED
  DEFAULT
}

VOLPH() {
  export ORACLE_HOME="/u01/app/oracle/product/11.2.0/volph_home"
  export ORACLE_SID=VOLPH
  DEFAULT
}

ASM() {
  export ORACLE_HOME="/u01/app/oracle/grid/product/11.2.0.4"
  export ORACLE_SID=+ASM
  DEFAULT
}

menu() {
    while true; do
        clear
        echo "============================================"
        echo ""
        echo " Oracle variables settings"
        echo ""
        echo " 1) PONT - Production Database"
        echo " 2) CREDFLOW - Production Database"
        echo " 3) HOMOPONTUACAO - Homolog Database"
        echo " 4) IBRACRED - Development Database"
        echo " 5) VOLPH - Standby Database (tanpr214)"
        echo " 6) +ASM - Automatic Storage Management"
        echo ""
        echo "============================================"
        read -p " Choose: " ANSWER
        echo "============================================"

        case ${ANSWER} in
            1) PONT; break                       ;;
            2) CREDFLOW; break                   ;;
            3) HOMOPONT; break                   ;;
            4) IBRACRED; break                   ;;
            5) VOLPH; break                      ;;
            6) ASM; break                        ;;
            *) echo "Option not found." | exit 1 ;;
        esac
    done
}