read -p "please provide the character" char

accepted_list="YyNn"

if [[ $accepted_list =~ $char ]]; then
    if [[ $char == 'y' || char == 'Y' ]]; then echo YES
    elif [[ $char == [nN] ]]; then echo NO  # using sets
    fi
else echo "invalid input"

fi
