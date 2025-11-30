from lk_irrigation import ReadMe, RiverWaterLevelData

if __name__ == "__main__":
    RiverWaterLevelData.load_all_from_remote(
        days_offset=112, total_pages=1_000, page_size=100
    )
    RiverWaterLevelData.write_all()
    ReadMe().build()
