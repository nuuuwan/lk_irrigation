# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_10:20:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **49,762 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 10:20:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:13:09 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:11:00 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-01-19 10:09:30 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:09:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-19 10:08:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:07:37 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:07:04 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:06:33 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-19 10:05:08 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:05:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-01-19 10:05:03 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-19 10:04:58 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-19 10:04:50 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.089 |  |
| 2026-01-19 10:04:45 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:04:05 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.155 |  |
| 2026-01-19 10:04:02 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-01-19 10:03:39 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:03:33 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:03:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:48 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:44 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:38 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.040 |  |
| 2026-01-19 10:02:32 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:24 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:02:24 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-01-19 10:02:09 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-19 10:01:52 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:42 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:37 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-01-19 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:28 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-19 10:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-19 10:00:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:00:16 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 10:05:03 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-19 10:06:33 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-19 10:02:09 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-19 10:00:16 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-19 10:09:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-19 10:00:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:02:24 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:05:08 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:09:30 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 10:03:33 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:42 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:28 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:04:02 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:07:04 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:40 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:08:16 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:32 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:07:37 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:48 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:01:28 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:24 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:03:12 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:30 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:04:45 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:03:39 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:02:44 | Thanthirimale (Malwathu Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:13:09 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:20:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-19 10:11:00 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-01-19 10:04:58 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.009 |  |
| 2026-01-19 10:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-01-19 10:01:18 | Dunamale (Aththanagalu Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-19 10:03:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-01-19 10:01:37 | Manampitiya (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.031 |  |
| 2026-01-19 10:02:38 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.040 |  |
| 2026-01-19 10:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.041 |  |
| 2026-01-19 10:04:50 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.089 |  |
| 2026-01-19 10:05:06 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.091 |  |
| 2026-01-19 10:04:05 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | -0.155 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)