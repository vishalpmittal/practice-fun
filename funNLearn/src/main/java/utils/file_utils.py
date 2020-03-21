import os

text2remove=['2017', 'Mp3', 'Songs', 'SongsMp3', 'Com', 'Hindi', '320Kbps', 'Songs', 'pk', 'Movie']

def remove_special_chars(str_with_sc, remove_space=True):
    if remove_space:
        return ''.join(c for c in str_with_sc if c.isalnum())

def remove_substrs(s, substr_list=text2remove):
    for text in text2remove: s = s.replace(text, '')
    return s

def rename_file(old_abs_path, new_abs_path):
    print '{} -> {}'.format(old_abs_path, new_abs_path)
    os.rename(old_abs_path, new_abs_path)

def update_dir_names(base_dir):
    for dir in os.listdir(base_dir):
        old_name = os.path.join(base_dir, dir)
        dir = remove_substrs(dir)
        dir = remove_special_chars(dir)
        new_name = os.path.join(base_dir, dir)
        rename_file(old_name, new_name)

def update_all_filenames_in_dir(base_dir, new_name_prefix):
    file_count = 1
    num_padding = len(str(len(os.listdir(base_dir)))) + 1
    for file2rename in os.listdir(base_dir):
        file_extension = file2rename.split('.')[-1].lower()
        old_file_name = os.path.join(base_dir, file2rename)
        new_file_name = os.path.join(
            base_dir, 
            '{}_{}.{}'.format(
                new_name_prefix,
                str(file_count).zfill(num_padding),
                file_extension
            )
        )
        rename_file(old_file_name, new_file_name)        
        file_count += 1

    print 'Renamed {} files at {}'.format(file_count-1, base_dir)

def update_access_n_modify_time(abs_file_path, time_str):
    touch_cmd = 'touch -a -m -t {} {}'.format(time_str, abs_file_path)
    os.system(touch_cmd)

def update_access_n_modify_time_dir(base_dir, time_str='201501211010'):
    counter = 1
    for file2update in os.listdir(base_dir):
        abs_file_path = os.path.join(base_dir, file2update)
        update_access_n_modify_time(abs_file_path, time_str)
        counter += 1
    
    print 'updated access and modified time to {} for {} files at {}'.format(
        time_str, counter-1, base_dir
    )

# update_dir_names(base_dir='/Users/vishalm/Downloads/songs_wip/2017')

# update_all_filenames_in_dir(
#     base_dir='/Users/vishalm/Downloads/WeddingPics', 
#     new_name_prefix='20150120_PoorvaVishalWedding'
# )

# update_access_n_modify_time_dir(
#     base_dir='/Users/vishalm/Downloads/WeddingPics', 
#     time_str='201501211010.30'
# )

update_all_filenames_in_dir(
    base_dir='/Users/vishalm/Downloads/SC_Wedding', 
    new_name_prefix='20141205_PoorvaVishalWedding_SantaClara'
)
update_access_n_modify_time_dir(
    base_dir='/Users/vishalm/Downloads/SC_Wedding', 
    time_str='201412051010.30'
)
