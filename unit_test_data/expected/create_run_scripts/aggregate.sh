#!/usr/bin/env bash
l2_agg_fn=create_run_scripts_test/l2_aggregate.h5
l2_plus_more_agg_fn=create_run_scripts_test/l2_plus_more_aggregate.h5
l1b_file=/fake_path/spectrum.h5

export PYTHONPATH=/fake_python_path
export PATH=/fake_bin_path
export LD_LIBRARY_PATH=/fake_lib_path
export LUA_PATH="/fake_path/input/gosat/config/?.lua;/l2_lua_fake_path"

function find_extra_product() {
    local l1b_file=$1
    local prod_dir_name=$2
    local prod_file_prefix=$3
    local prod_desc_name=$4
    local datasets_grep=$6

    # Try and find IMAP file based on L1B filename
    prod_fn=$(ls $(dirname $(echo ${l1b_file}) | sed "s/L1bSc/${prod_dir_name}/g")/${prod_file_prefix}*_${orbit_ident}_*.h5 2>/dev/null)
    if [ ! -z "$prod_fn" ]; then
        same_l1b=$(h5dump -d /Metadata/InputPointer $prod_fn | grep $(basename $l1b_file))
        if [ -z "$same_l1b" ]; then
            echo "$prod_desc_name file does not use the same L1B file, will not use it: $prod_fn"
            unset prod_fn
        else
            echo "Found and using $prod_desc_name file:"
            echo $prod_fn
        fi
    fi
}

# Aggregate all single sounding output hdf files into a single hdf file
if [ ! -e "$l2_agg_fn" ]; then
    input_files_tmp=$(mktemp)
    find create_run_scripts_test/output -name "*.h5" > $input_files_tmp

    echo "Aggregating L2 output files"
    /l2_support_fake_path/utils/splice_acos_hdf_files.py -o $l2_agg_fn -i $input_files_tmp $*
    rm $input_files_tmp
else
    echo "L2 aggregated file exists, skipping creation"
fi

if [ ! -e "$l2_plus_more_agg_fn" ]; then
    echo "Creating L2 plus L1B aggregated file"
    # Extract sounding ids, and reformat into a format that can be used by splice tool
    snd_id_tmp1=$(mktemp)
    snd_id_tmp2=$(mktemp)
    h5dump --noindex -o $snd_id_tmp1 -d RetrievalHeader/sounding_id_reference $l2_agg_fn > /dev/null

    # This line below, turns commas into new lines, removes empty spaces and blank lines
    cat $snd_id_tmp1 | sed 's|,|\n|g' | sed -r 's|^[ ]*||' | grep -v '^$' > $snd_id_tmp2
    rm $snd_id_tmp1 

    # Extract orbit number 
    orbit_ident=$(echo $l1b_file | sed -r 's/.*_L1bScND_([^_]+)_.*/\1/')

    # Try and find IMAP file based on L1B filename
    find_extra_product "$l1b_file" "L2IDP" "oco2_L2IDP" "IMAP DOAS" "DOAS"
    imap_fn=$prod_fn

    # Try and find ABand file based on L1B filename
    find_extra_product "$l1b_file" "L2ABP" "oco2_L2ABP" "ABand" "/ABandRetrieval"
    aband_fn=$prod_fn

    # Combine L1B and L2 files into one file
    echo "Combining L2 and L1B into a single file"
    /l2_support_fake_path/utils/splice_acos_hdf_files.py --splice-all --rename_mapping --agg_names_filter -o $l2_plus_more_agg_fn $l2_agg_fn $l1b_file $imap_fn $aband_fn -s $snd_id_tmp2
    rm $snd_id_tmp2

    # Create retrieval_index dataset based on L1B file
    echo "Adding retrieval information datasets"
    /l2_support_fake_path/utils/add_spliced_retrieval_info.py $l1b_file $l2_plus_more_agg_fn
else
    echo "L2 plus L1B file exists, skipping creation"
fi