import webbrowser
import os
from TestFunction.Login.login import LoginTest
from TestFunction.AssetList.assetList import AssetList
from TestFunction.AddAsset.assetCreate import AssetCreate
from Template.ReportTestCase import Report
from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner

def open_html_reports(report_dir):
    # List all HTML files in the specified directory
    html_files = [f"{report_dir}/{filename}" for filename in os.listdir(report_dir) if filename.endswith('.html')]

    if not html_files:
        print("No HTML reports found in the specified directory.")
        return

    # Open each HTML report in the default web browser
    for html_file in html_files:
        webbrowser.open(f'file://{html_file}', new=2)


if __name__ == '__main__':
  
    report_directory = 'C:/Code/FIndXTest/TestAsset/Report'

    LoginTest = TestLoader().loadTestsFromTestCase(LoginTest)
    AssetList = TestLoader().loadTestsFromTestCase(AssetList)
    AssetCreate = TestLoader().loadTestsFromTestCase(AssetCreate)

    suite = TestSuite([AssetCreate])

    runner = HTMLTestRunner(output=report_directory)

    runner.run(suite)
    open_html_reports(report_directory)

