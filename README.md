# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_16:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 16:16:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.008 |  |
| 2026-03-13 16:12:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:12:11 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:11:36 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:11:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:11:04 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-03-13 16:10:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-03-13 16:10:03 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:19 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-03-13 16:08:18 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:04 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-13 16:07:40 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:07:38 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:07:09 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:06:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-13 16:06:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 16:06:10 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-03-13 16:05:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:05:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-13 16:04:06 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:03:36 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:03:35 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.178 |  |
| 2026-03-13 16:03:18 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:03:18 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:03:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:57 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:46 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-03-13 16:02:33 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-13 16:02:19 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:02:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-13 16:02:13 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:36 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:21 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:01:10 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-13 16:01:02 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.073 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 16:02:33 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-03-13 16:01:10 | Manampitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-13 16:05:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-13 16:06:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-13 16:02:19 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:05:51 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:01:21 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 16:06:22 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 16:07:38 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:13 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:03:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:22 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:04:06 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:18 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:06:10 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:12:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:03:36 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:02:51 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:11:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:45 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:10:03 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:12:11 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:07:09 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:07:40 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:01:36 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:16:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | -0.008 |  |
| 2026-03-13 16:08:19 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-03-13 16:11:04 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.009 |  |
| 2026-03-13 16:02:14 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-13 16:10:06 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-03-13 16:08:04 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-03-13 16:02:46 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-03-13 16:03:18 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:03:18 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-03-13 16:05:54 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.038 |  |
| 2026-03-13 16:01:02 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | -0.073 |  |
| 2026-03-13 16:03:35 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | -0.178 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)