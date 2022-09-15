import github
import os

from GHRepo import Repository

import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger(__name__)

class GHOrganization:

    def __init__(self, org=None, token=None, username=None, email=None, name=None):
        """
        _summary_

        Args:
            org (_type_, optional): _description_. Defaults to None.
        """
        self.token = token or os.getenv('GITHUB_PAT')
        self.org = org or os.getenv('GITHUB_ORG')
        self.username = username or os.getenv('GITHUB_USERNAME')
        self.email = email or os.getenv('GITHUB_EMAIL')
        self.commit_name = name or os.getenv('GITHUB_COMMIT_NAME')
        #print(vars(self), os.getenv('GITHUB_PAT'))
        if self.token and self.org:
            self.g = github.Github(self.token)
            self.org = self.g.get_organization(self.org)
        self.repositories = []

    def get_repos(self, destination = "./", search=""):
        """
        _summary_
        """
        for repo in self.org.get_repos():
            if search.lower() in repo.name.lower():
                log.info(f"cloning {repo.name}...")
                self.repositories.append(Repository(repo, destination))
                log.info(f"...completed")
        return self.repositories
