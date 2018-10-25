""" LaunchWatch bots. """

from html.parser import HTMLParser

from launchwatch.exceptions import (
    BotError,
    ParseError
)

import requests as r
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_binary


class RLESSiteBot:
    """ Bot that handles all RLES website scraping. """
    base = 'https://www.rocketleagueesports.com'

    def get_matches(self):
        """ Get listed matches.

        Uses requests to check connection, then uses selenium
        Chrome webdriver to render the whole page because of all the
        JavaScript present, soups it, parses and extracts match data.

        Returns:
            list:matches -- a list of match dicts

        """
        path = self.base + '/schedule'
        
        # check connection
        response = r.get(path)
        if response.status_code != 200:
            raise BotError(response)

        # get page source, handle
        driver = webdriver.Chrome()
        driver.get(path)
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        except:
            raise ParseError(response)

        # begin extraction
        matches = []
        raw_matches = soup.find_all('div', {'class': 'match'})
        for raw_match in raw_matches:
            match = {}
            match['time'] = raw_match.find('h3', {'class': 'time'}).string
            match['teams'] = [
                name.string
                for name in raw_match.find_all(
                    'span', {'class': 'team-name'}
                )
            ]
            match['score'] = ' - '.join([
                score.string
                for score in raw_match.find_all(
                    'span', {'class': 'win'}
                )
            ])

            matches.append(match)

        driver.quit()
        return matches

    def get_teams(self):
        """ Get listed teams.

        Checks connection, sets up a driver on the /stats page,
        extracts team data and packages into a list.

        Returns:
            list:teams -- a list of model-friendly team dicts
        
        """
        path = self.base + '/stats'
        
        # check connection
        response = r.get(path)
        if response.status_code != 200:
            raise BotError(response)

        # get page source, handle
        driver = webdriver.Chrome()
        driver.get(path)
        try:
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        except:
            raise ParseError(response)

        # begin extraction
        teams = []
        table = soup.find('table', {'id': 'team-stats'})
        rows = table.find('tbody')
        for row in rows:
            team = {}
            fields = row.find_all('td')
            
            team['rank'] = fields[0].string
            team['name'] = fields[1].string
            team['matches_played'] = fields[2].string
            team['wins'] = fields[3].string
            team['losses'] = fields[4].string
            team['games_played'] = fields[5].string
            team['win_percentage'] = fields[6].string
            team['goals'] = fields[7].string
            team['goals_per_game'] = fields[8].string
            team['saves'] = fields[9].string
            team['saves_per_game'] = fields[10].string
            team['assists'] = fields[11].string
            team['assists_per_game'] = fields[12].string

            teams.append(team)

        driver.quit()
        return teams

