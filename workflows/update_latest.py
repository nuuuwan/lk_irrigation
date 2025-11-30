from lk_irrigation import ReadMe, RiverWaterLevelData

if __name__ == "__main__":
    RiverWaterLevelData.load_all_from_remote(
        days_offset=7, total_pages=100, page_size=100
    )
    RiverWaterLevelData.write_all()
    ReadMe().build()
