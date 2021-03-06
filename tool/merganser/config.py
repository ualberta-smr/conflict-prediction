
# Keys
GITHUB_KEY = ''

# Paths
REPOSITORY_PATH = '../working_dir/repository/'
TEMP_CSV_PATH = '../working_dir/csv_files/'
REPOSITORY_LIST_PATH = '../working_dir/repository_lists/'
LOG_PATH = '../working_dir/logs/'
QUERY_PATH = '../queries/'
PREDICTION_RESULT_PATH = '../working_dir/prediction_result/'
PREDICTION_CSV_PATH = '../working_dir/prediction_data/'
REAPER_DATASET_PATH = '../tools/reaper/dataset.csv'
PREDICTION_CSV_DATA_NAME = 'data_<NAME>.csv'
PREDICTION_CSV_LABEL_NAME = 'label_<NAME>.csv'

# Constants
MAX_MERGE_SCENARIOS = 1000
MAX_ANALYZING_DAY = 14
MAX_REPO_SIZE_TO_ANALYZE = 1 * 1024 * 1024

# DB information
DB_HOST = 'localhost'
DB_NAME = 'Merge_Data'
DB_USER_NAME = 'root'
DB_PASSWORD = '12345678'

# Visualization
VIS_S = 100
VIS_ALPHA = 0.4

# Prediction
MIN_SAMPLE_LEAVES = [2, 5, 10, 20]
MIN_SAMPLE_SPLIT = [2, 3, 5]
ESTIMATOR_NUM = [1, 2, 3, 5, 10]
LEARNING_RATE = [0.9, 1.0, 1.1]
FOLD_NUM = 10
SCORING_FUNCTION = 'f1'
TREE_MAX_DEPTH = [1, 3, 5, 7, 11]
TEST_SIZE = 0.25
RANDOM_SEED = 17
TREE_FILE_NAME = 'tree.dot'

# REAPER repository search
STARS_MIN = 100
TOP_REPOS_NUM = 150
LANGUAGES = ['Java', 'Python', 'Ruby', 'C++', 'PHP', 'C', 'C#']
