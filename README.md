# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_13:03:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,943 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 13:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-13 13:03:50 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-02-13 13:03:48 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-02-13 13:03:38 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:03:35 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-13 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 13:03:06 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-13 13:03:04 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 13:02:48 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 13:02:40 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:02:34 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:02:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.091 |  |
| 2026-02-13 13:02:01 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:01:58 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-13 13:01:34 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 13:01:31 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 13:01:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:01:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 13:01:10 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.139 |  |
| 2026-02-13 13:01:09 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:00:56 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 13:00:48 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:00:48 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-02-13 13:00:45 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:08:46 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:08:08 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 12:04:05 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-13 13:01:13 | Manampitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-02-13 13:03:35 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-02-13 13:02:48 | Ellagawa (Kalu Ganga) | 4.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-13 13:03:30 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-13 13:03:04 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 13:00:56 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-13 13:01:34 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-13 13:01:31 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-13 13:02:40 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:00:48 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:03:38 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 13:01:09 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:01:14 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:02:34 | Giriulla (Maha Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:21 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:08:46 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:00:45 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:02:03 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:02:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-13 12:04:11 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:02:01 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:01:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 11:02:04 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 13:03:53 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-13 11:08:30 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.011 |  |
| 2026-02-13 13:01:58 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-13 13:03:06 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.020 |  |
| 2026-02-13 12:07:31 | Urawa (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.023 |  |
| 2026-02-13 12:03:24 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-02-13 13:00:48 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.030 |  |
| 2026-02-13 13:03:50 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-02-13 12:02:33 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.042 |  |
| 2026-02-13 13:03:48 | Padiyathalawa (Maduru Oya) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-02-13 12:02:00 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.069 |  |
| 2026-02-13 12:04:38 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.071 |  |
| 2026-02-13 13:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.71 | 🟢 Normal | -0.091 |  |
| 2026-02-13 13:01:10 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | -0.139 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)