from domain.model.Pairs import Pairs
from infrastructure.crawler.PairsCrawler import PairsCrawler


class PairsUsecase:

    def invoke(self):
        pairs = Pairs()
        crawler = PairsCrawler(pairs.min_sleep_second, pairs.max_sleep_second)

        crawler.auth(pairs.facebook_login_id, pairs.facebook_login_password)
        crawler.profile_list()
        crawler.crawle(pairs.max_view_profile_count)
