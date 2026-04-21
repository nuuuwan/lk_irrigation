# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_03:41:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 03:41:39 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 2.764 | 🔺 Rising |
| 2026-04-22 03:32:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 2.764 | 🔺 Rising |
| 2026-04-22 03:18:50 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -360.000 |  |
| 2026-04-22 03:18:48 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -360.000 |  |
| 2026-04-22 03:12:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:08:13 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.056 |  |
| 2026-04-22 03:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.032 |  |
| 2026-04-22 03:06:47 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.006 |  |
| 2026-04-22 03:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-22 03:05:11 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:04:58 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-22 03:04:58 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.017 |  |
| 2026-04-22 03:04:48 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 03:04:46 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-22 03:04:44 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-04-22 03:04:32 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:04:19 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | -0.417 |  |
| 2026-04-22 03:04:14 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:04:13 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:04:11 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.107 |  |
| 2026-04-22 03:03:53 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-22 03:03:47 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:03:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-04-22 03:03:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:03:26 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:03:12 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-04-22 03:03:12 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.116 |  |
| 2026-04-22 03:02:55 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-04-22 03:02:41 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-22 03:02:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:25 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:02:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:13 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:12 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:01:45 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.038 |  |
| 2026-04-22 03:01:26 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:01:24 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.202 |  |
| 2026-04-22 03:01:14 | Kuda Oya (Kirindi Oya) | 2.68 | 🟢 Normal | -0.150 |  |
| 2026-04-22 03:01:07 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.044 |  |
| 2026-04-22 03:00:54 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-04-22 03:00:51 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-04-22 02:52:43 | Nawalapitiya (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.107 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 03:41:39 | Dunamale (Aththanagalu Oya) | 0.90 | 🟢 Normal | 2.764 | 🔺 Rising |
| 2026-04-22 03:06:16 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 03:02:41 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-22 03:03:53 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 03:04:58 | Pitabeddara (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-22 03:04:48 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:02:25 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:04:32 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 03:02:13 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:03:37 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:05:11 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:02:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:01:26 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:12:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 03:06:47 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.006 |  |
| 2026-04-22 03:04:46 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-22 03:03:12 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-04-22 03:00:54 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-04-22 03:00:51 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.015 |  |
| 2026-04-22 03:04:58 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | -0.017 |  |
| 2026-04-22 03:07:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | -0.032 |  |
| 2026-04-22 03:02:55 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.033 |  |
| 2026-04-22 03:01:45 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.038 |  |
| 2026-04-22 03:01:07 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.044 |  |
| 2026-04-22 03:08:13 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.056 |  |
| 2026-04-22 03:03:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-04-22 03:04:44 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.060 |  |
| 2026-04-22 03:03:56 | Nawalapitiya (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.107 |  |
| 2026-04-22 03:03:12 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.116 |  |
| 2026-04-22 03:01:14 | Kuda Oya (Kirindi Oya) | 2.68 | 🟢 Normal | -0.150 |  |
| 2026-04-22 03:01:24 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.202 |  |
| 2026-04-22 03:04:19 | Thanamalwila (Kirindi Oya) | 2.60 | 🟢 Normal | -0.417 |  |
| 2026-04-22 03:04:14 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | -108.000 |  |
| 2026-04-22 03:18:50 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -360.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)