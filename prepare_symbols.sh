if [ "" == "$1" ]; then
	echo "USAGE: ./prepare_symbols PATH_TO_DEBUG_EXEC NAME_OF_RELEASE_EXEC"
	exit 1
fi

if [ "" == "$2" ]; then
	echo "USAGE: ./prepare_symbols PATH_TO_DEBUG_EXEC NAME_OF_RELEASE_EXEC"
	exit 1
fi

SYM_FILE="$2.sym"

dump_syms "$1" > "$SYM_FILE"

SYM_DIR="./symbols/$2/"$(head -n1 "$SYM_FILE" | awk -F ' ' '{print $4}') #####

mkdir -p "$SYM_DIR"

mv "$SYM_FILE" "$SYM_DIR/"
