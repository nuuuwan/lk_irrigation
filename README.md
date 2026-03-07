# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--07_10:27:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **91,549 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **45** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 10:27:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:20:09 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:18:30 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:16:07 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-07 10:11:32 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:10:56 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:10:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:07:59 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:07:08 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-03-07 10:06:46 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:06:41 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.018 |  |
| 2026-03-07 10:06:38 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-03-07 10:06:00 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:05:47 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:05:18 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:05:07 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:04:56 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 10:04:51 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:04:17 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:03:56 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-07 10:03:51 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-07 10:03:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-07 10:03:23 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:03:17 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:03:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-03-07 10:02:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:32 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 10:02:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:24 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.050 |  |
| 2026-03-07 10:02:23 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.071 |  |
| 2026-03-07 10:02:22 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:17 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:00 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 10:02:00 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:58 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:54 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:50 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-03-07 10:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:09 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:00:38 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:00:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-07 10:07:08 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-03-07 10:03:25 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-07 10:03:51 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-07 10:02:32 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-07 10:04:56 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-07 10:05:07 | Weraganthota (Mahaweli Ganga) | -1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:50 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:25 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:22 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:17 | Horowpothana (Yan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:54 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:05:47 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:50 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:06:46 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:05:18 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:18:30 | Panadugama (Nilwala Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:20:09 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:00:06 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:03:10 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:02:10 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:04:17 | Badalgama (Maha Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:07:59 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:10:30 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:27:01 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:01:09 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-07 10:16:07 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-03-07 10:06:38 | Thanthirimale (Malwathu Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-03-07 10:03:23 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:04:51 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:00:38 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-03-07 10:06:41 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.018 |  |
| 2026-03-07 10:03:56 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-03-07 10:01:41 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.032 |  |
| 2026-03-07 10:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-03-07 10:02:24 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | -0.050 |  |
| 2026-03-07 10:02:00 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.065 |  |
| 2026-03-07 10:02:23 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)