from importlib.machinery import SourceFileLoader
goinglobal_scrapper = SourceFileLoader('going_global_scrapper', 'code/Scraper/going_global_scraper.py').load_module()

def test_get_job_goin_global(mocker):
    final_result = goinglobal_scrapper.get_jobs("Programmer", "", 5, ["Programmer", "Analytic", "Experience"])
    assert final_result is not None