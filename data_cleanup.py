
import csv


def filter_invalid_teams(data_file):
    cleaned_scrape = open("cleaned_scrape.csv", 'w')

    with open(data_file,'r') as scraped_data:
        for row in scraped_data:
            row = row.split(',')
            team_name, team_link_url, team_btags = row[0], row[1], row[2:]
            if len(team_btags) < 6:
                print ("Dropped {} for having too few members ({}).".format(team_name, len(team_btags)))
            else:
                team_btags = ','.join(team_btags)
                cleaned_scrape.write("{},{},{}\n".format(team_name, team_link_url, team_btags))

    def too_few_members():
        


filter_too_few_members('raw_scrape.csv')