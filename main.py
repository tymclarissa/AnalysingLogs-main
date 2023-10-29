import os

# Get a list of all log files in the Logs directory
log_files = os.listdir('./Logs') 

for log_file in log_files:
    error_count = 0
    warning_count = 0
    info_count = 0

    # Open the log file
    with open(f'./Logs/{log_file}', 'r') as file:
        #  Read eack line in the log file
        for line in file:
            # Count the number of each type of event
            if 'ERROR' in line:
                error_count += 1
            elif 'WARNING' in line:
                warning_count += 1
            elif 'INFO' in line:
                info_count += 1

        # Write the counts to the report file
        with open (f'./Reports/Report_for_{log_file}', 'w') as report_file:
            report_file.write(f'ERROR: {error_count}\n') 
            report_file.write(f'WARNING: {warning_count}\n') 
            report_file.write(f'INFO: {info_count}\n') 
             


        
