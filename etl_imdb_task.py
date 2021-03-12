import csv


class ETL:

    def __init__(self):
        self.csvfile = ''
        self.newcsvfile = ''
        self.header = [['TitleType', 'Title', 'StartYear', 'RunTimeMins', 'Genres']]
        self.readcsv = []
        self.movies_shows = []
        self.movie_genres = []

    def extract(self):
        with open(self.csvfile) as file:
            readcsv = csv.reader(file, delimiter=',')
            next(readcsv)
            self.readcsv = list(readcsv)
            return self.readcsv

    def transform_movies_shows(self):
        for i in self.readcsv:
            if i[0] == 'movie' or i[0] == 'tvseries':
                self.movies_shows.append(i)
        return self.movies_shows

    def transform_secondary_genres(self):
        for i in self.movies_shows:
            i[7] = i[7].split(',', 1)[0]
        return self.movies_shows

    def transform_remove(self):
        for i in self.movies_shows:
            i.pop(5)
            i.pop(3)
            i.pop(2)
        return self.movies_shows

    def loading_csv(self):
        self.header.extend(self.movies_shows)

        with open(self.newcsvfile, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.header)

    def main(self, old_file_name, new_file_name):
        self.csvfile = old_file_name
        self.newcsvfile = new_file_name
        self.extract()
        self.transform_movies_shows()
        self.transform_secondary_genres()
        self.transform_remove()
        self.loading_csv()


Example = ETL()
Example.main('imdbtitles.csv', 'newimdb.csv')
