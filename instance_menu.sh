#!/bin/bash

# # # # # # # # # # # # # # # # # # # #
# Creator: João Vítor Foltran         #
# Date...: 24/01/2020                 #
# Purpose: Menu for Oracle variables  #
# # # # # # # # # # # # # # # # # # # # 

ANSWER="none"

MENU() {
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
        echo ""
        echo "============================================"
        read -p " Choose: " ANSWER
        echo "============================================"
    
        case ${ANSWER} in
            1) source /etc/ambiente_pont.sh; break     ;;
            2) source /etc/ambiente_credflow.sh; break ;;
            3) source /etc/ambiente_homopont.sh; break ;;
            4) source /etc/ambiente_ibracred.sh; break ;;
            5) source /etc/ambiente_volph.sh; break    ;;
            *) echo "Option not found." | exit 1 ;;
        esac
    done
}

MENU
