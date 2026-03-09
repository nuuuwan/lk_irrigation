# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_14:10:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 14:10:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:09:40 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:08:45 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:07:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:07:17 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.024 |  |
| 2026-03-09 14:05:30 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:04:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-03-09 14:04:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:04:14 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:03:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:50 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 14:03:44 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.800 | 🔺 Rising |
| 2026-03-09 14:03:29 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:03:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:20 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.043 |  |
| 2026-03-09 14:03:17 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-03-09 14:02:56 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.113 |  |
| 2026-03-09 14:02:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:45 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.122 |  |
| 2026-03-09 14:02:36 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.072 |  |
| 2026-03-09 14:02:27 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:14 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-09 14:02:12 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:01:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:29 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.070 |  |
| 2026-03-09 14:01:29 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 14:01:29 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:24 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:23 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-09 14:01:09 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 14:03:44 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.800 | 🔺 Rising |
| 2026-03-09 14:04:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.178 | 🔺 Rising |
| 2026-03-09 14:02:14 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-03-09 14:01:23 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-03-09 14:03:50 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 14:01:29 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 14:01:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:27 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:00:16 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:09 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:28 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:50 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:07:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:12:05 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 12:02:01 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:05:11 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:05:30 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 13:04:52 | Moraketiya (Walawe Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:27 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:09:40 | Dunamale (Aththanagalu Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:29 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:52 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:03:24 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:01:24 | Thanthirimale (Malwathu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:10:37 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:08:45 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-03-09 14:04:16 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:02:12 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:03:29 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:04:14 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-03-09 14:03:17 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-03-09 14:07:17 | Thalgahagoda (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.024 |  |
| 2026-03-09 14:03:20 | Glencourse (Kelani Ganga) | 8.44 | 🟢 Normal | -0.043 |  |
| 2026-03-09 14:01:29 | Weraganthota (Mahaweli Ganga) | -2.61 | 🟢 Normal | -0.070 |  |
| 2026-03-09 14:02:36 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.072 |  |
| 2026-03-09 14:02:56 | Peradeniya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.113 |  |
| 2026-03-09 14:02:45 | Baddegama (Gin Ganga) | 0.84 | 🟢 Normal | -0.122 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)