# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_01:15:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,098 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 01:15:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:13:51 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-01 01:13:27 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-02-01 01:13:21 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-01 01:10:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 12.594 | 🔺 Rising |
| 2026-02-01 01:08:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-02-01 01:07:11 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 01:06:50 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:06:36 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:05:19 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-01 01:05:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 01:04:48 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-02-01 01:04:07 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-01 01:03:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:03:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:02:57 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-01 01:02:56 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 01:02:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:02:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-01 01:02:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-01 01:02:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:27 | Panadugama (Nilwala Ganga) | 0.12 | 🟢 Normal | 12.594 | 🔺 Rising |
| 2026-02-01 01:01:26 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:20 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.163 |  |
| 2026-02-01 01:01:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:09 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:51:24 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 12.594 | 🔺 Rising |
| 2026-02-01 00:48:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:48:02 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 01:10:53 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 12.594 | 🔺 Rising |
| 2026-02-01 01:13:51 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 3.600 | 🔺 Rising |
| 2026-02-01 01:02:42 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-02-01 01:02:17 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-02-01 01:04:07 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-02-01 00:05:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-02-01 01:07:11 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-01 01:05:12 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 01:02:56 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 00:10:51 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:26 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:18:19 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:02:55 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:19:55 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:07:51 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:06:50 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:06:36 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:03:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:12:22 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:15:08 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 00:16:30 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:02:11 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:09 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:03:12 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:01:09 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-01 01:13:27 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-02-01 00:08:43 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-02-01 00:05:00 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-02-01 00:09:49 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-31 22:00:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-01 01:08:41 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.019 |  |
| 2026-02-01 01:05:19 | Rathnapura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.020 |  |
| 2026-02-01 01:04:48 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.029 |  |
| 2026-02-01 01:02:57 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-02-01 01:01:20 | Manampitiya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.163 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)