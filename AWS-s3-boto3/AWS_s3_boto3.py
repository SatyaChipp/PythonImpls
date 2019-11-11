# -*- coding: utf-8 -*-
"""
@author: Satya
Coding Excercise
"""

import pandas as pd
#S3 access credentials:
ACCESS_KEY = ********
SECRET_KEY = ***********
Bucket_name = **********

import pip
from subprocess import call
def install_pkg(package):
    pip.main(['install', package])
install_pkg('schedule')
install_pkg('boto3')
import boto3
#from boto.s3.key import Key

class dataS3:
    def __init__(self):
        self.count = 0
        pass
    def connect_s3(self):
        conn = boto3.Session(aws_access_key_id=ACCESS_KEY, 
                            aws_secret_access_key=SECRET_KEY)
        resource = conn.resource('s3')
        bucket_s3 = resource.Bucket(Bucket_name)
        return bucket_s3, resource
        
    def get_gzip_files(self, filename_=None):
        bucket_s3, resource = self.connect_s3()
        if not data:
            complete_df = pd.DataFrame()
            for item in list(bucket_s3.objects.filter(Prefix='*****************bid_logs.2018_06_01/200_files/')):
                '''s3.ObjectSummary(bucket_name=*************, key='*************bid_logs.2018_06_01/200_files/*********.gz')
                '''
                self.count +=1
                key = item.key
                gz_file = "gz_file_{}.gz".format(self.count)
                downloadfile = resource.Bucket(Bucket_name).download_file(key, gz_file)
                #downloading to local for faster processing
                with gzip.open(r"C:\\Users\\Jen\\Downloads\\SampleExercise"+gz_file, 'r') as fi: #here modify to add current directory path
                    
                    file_content = fi.read()
                    import csv
                    filename = "data_file_{}.csv".format(self.count)
                    print(filename)
                    with open(filename, 'wb') as rf:
                        rf.write(file_content)
                    data = pd.read_csv(filename, error_bad_lines=False)
                    #implement any or all functions on the data as below
                    #function calls can be hierarchical for multiple implementations
                    data1 = self.Question1(data)
                    data2 = self.Question2(data)
                    data3 = self.Question3(data, data)
                    data4 = self.Question4_1(data3)
                     #by the time loop ends we have processed and merged all log data into one dataframe
                    complete_df.append(data4, ignore_index=True)
            self.Question4_2(complete_df) #data merged and maintains logs
                    break
        else:
            try:
                if filename.endswith('.csv'):
                    #we can add the below code into a function so that DRY
                    data = pd.read_csv(filename, error_bad_lines=False)
                    #implement any or all functions on the data as below
                    data1 = self.Question1(data)
                    data2 = self.Question2(data)
                    data3 = self.Question3(data, data)
                    data4 = self.Question4_1(data3)
                     #by the time loop ends we have processed and merged all log data into one dataframe
                    complete_df.append(data4, ignore_index=True)
                    self.Question4_2(complete_df) #data merged and maints logs
                else:
                    pass #here we can convert whtever file to csv and do the same as above
                    
        
    def Question1(self, data):
        """1.	Select the ip_address, device_id pair 
        from the data set provided along with first_seen and last_seen timestamps 
        (there should only be one entry in the output feed for distinct ip_address, device_id pair). 
        **** column provides the timestamp for each record."""
        
        columns = ["ip_address", "platform_device_ifa", "bid_time_epoch_in_usecs"]
        df1 = pd.DataFrame(data, columns=columns)
        
        df_last = df1.loc[df1.groupby(['ip_address','platform_device_ifa'])['bid_time_epoch_in_usecs'].idxmax()]
        df_last_seen = df_last.rename(columns=({'bid_time_epoch_in_usecs': 'last_seen'}))
        
        df_first = df1.loc[df1.groupby(['ip_address','platform_device_ifa'])['bid_time_epoch_in_usecs'].idxmin()]      
        df_first_seen = df_first.rename(columns=({'bid_time_epoch_in_usecs': 'first_seen'}))
        
        df_merged = df_first_seen.merge(df_last_seen, on=['ip_address','platform_device_ifa'])
        
        df_remove_duplicates = df_merged.drop_duplicates(['ip_address','platform_device_ifa'],keep= 'last')
        return df_remove_duplicates, df_merged

        
        
    def Question2(self, data):
        """2.	Remove any ip address that has more than 12 device_ids associated with it in the data set provided."""
        #groupby ipaddr and deviceids to find counts
        count_df = data.groupby(['ip_address', 'platform_device_ifa']).size().to_frame('count_ids').reset_index()
        new_df = count_df[count_df.count_ids > 12]
        #remove above from our dataset
        data.drop(new_df.index, axis=0, inplace=True)
        return data

        
    def Question3(self, data, raw_df):
        """3.	Remove any ip addresses or device_ids that is associated with more than 12 mobile_apps in the data provided."""
        #groupby and count appids for each ipaddress from complete dataset
        count_mobile_df_ip = raw_df.groupby(['ip_address', 'app_id']).size().to_frame('count_ids').reset_index()
        new_df_ip = count_mobile_df_ip[count_mobile_df_ip.count_ids > 12]
        
        #groupby and count for each deviceid from our complete dataset
        count_mobile_df_id = raw_df.groupby(['platform_device_ifa', 'app_id']).size().to_frame('count_ids').reset_index()
        new_df_id = count_mobile_df_id[count_mobile_df_id.count_ids > 12]
        
        #remove both of them from processed dataset
        data.drop(new_df_ip.index, axis=0, inplace=True)
        data.drop(new_df_id.index, axis=0, inplace=True)
        return data
    
    
    def Question4_1(self, data):
        """4.	Generate a CSV (or TSV) feed named: ip_device_id_snapshot.csv (or .tsv) 
        with the following columns:-
        ipaddress, device_id, first_seen_timestamp, last_seen_timestamp """
        
        ##since its not mentioned in this part of the question that we need output feed for distinct ip_address, device_id pair
        df1, df = self.Question1(data)
        df_ = df.rename(columns=({'first_seen': 'first_seen_timestamp', 'last_seen': 'last_seen_timestamp' }))
        return df_
    
    def Question4_2(self, data):
        """4.	Generate a CSV (or TSV) feed named: ip_device_id_snapshot.csv (or .tsv) 
        with the following columns:-
        ipaddress, device_id, first_seen_timestamp, last_seen_timestamp """
        ##write data to csv
        try:
            data.to_csv("ip_device_id_snapshot.csv", sep=',', encoding='utf-8', index=False)
            job_status = 'Success'
        except:
            job_status = 'Failed'
            
        ##maintainging a log file here to keep track of job status, files and timestamp
        #can be used for backfill checks and reprocessing old data, failed jobs etc
        import os
        if os.path.exists('Log_file_track_backfill.csv'):
            append_wr = 'a' # append if already exists
        else:
            append_wr = 'w' # make a new file if not
     
        with open('Log_file_track_backfill.csv', append_wr) a csvfile:
            logwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            import time
            if append_wr == 'w':
                #dont create columns again
                logwriter.writerow(['Date', 'Snapshot_id', 'job_status'])
            else:
                logwriter.writerow([time.time(), "ip_device_id_snapshot.csv", job_status])
            
            
            
    def merge_files_keep_log(self, ip_device_id_snapshot_filename, newdata):
        """
        Write the program such that, it can start with an existing ip_device_id_snapshot 
        and merge with the new data set provided. For example, we want to be able to run the program on a 
        daily basis with new versions of the data logs. 
        Take care of backfill (processing older days logs) and reprocessing use cases as well.
        """
        try:
            if os.path.exists('ip_device_id_snapshot.csv'):
                if os.path.exists('Log_file_track_backfill.csv'):
                    ###open log_file_rtacekr and get file with latest timestamp and job status as success
                    #and merge into that file
                    self.get_gzip_files(filename=newdata)
            else:
                raise("cannot find file")
            job_status = 'Success'
        except:
            job_status = 'Failed'
            
        #write back to log tracker file with newly merged file and job status
        
    def program_run_daily(self, new_log_files):
        import schedule
        import time
        #scheduling it to run everyday at 10 30am -- modify as required here
        schedule.every().day.at("10:30").do(self.merge_results(ip_device_id_snapshot_filename, new_log_files))
        

    
if __name__ == "__main__":
    S3bucket = dataS3()
    print(S3bucket.connect_s3())
    S3bucket.get_gzip_files()
    ##to schedule jobs
    sample_log_file = 'data_file_5.csv'
    S3bucket.program_run_daily(sample_log_file)
    
        
