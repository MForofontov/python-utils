#!/bin/bash

# Default directories
DEFAULT_TEST_DIR="pytest/unit"
DEFAULT_ALLURE_RESULTS_DIR="pytest_run_tests/allure-results"
DEFAULT_ALLURE_REPORT_DIR="pytest_run_tests/allure-report"

# Allow overriding default directories via command-line arguments
TEST_DIR=${1:-$DEFAULT_TEST_DIR}
ALLURE_RESULTS_DIR=${2:-$DEFAULT_ALLURE_RESULTS_DIR}
ALLURE_REPORT_DIR=${3:-$DEFAULT_ALLURE_REPORT_DIR}

# Function to print messages with timestamps
log_with_time() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log_with_time "[Info] Running tests in: $TEST_DIR"
log_with_time "[Info] Storing Allure results in: $ALLURE_RESULTS_DIR"
log_with_time "[Info] Generating Allure report in: $ALLURE_REPORT_DIR"

# Run pytest in the specified directory and generate Allure results
pytest $TEST_DIR --alluredir=$ALLURE_RESULTS_DIR

log_with_time "[Info] Allure results generated successfully in $ALLURE_RESULTS_DIR!"

log_with_time "[Info] Generating Allure report..."
# Generate the Allure report in the specified directory
allure generate $ALLURE_RESULTS_DIR -o $ALLURE_REPORT_DIR
log_with_time "[Info] Allure report generated successfully in $ALLURE_REPORT_DIR!"

# Open the Allure report
allure open $ALLURE_REPORT_DIR
