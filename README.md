# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_14:12:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 14:12:25 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:11:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-01 14:10:58 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 14:08:29 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-01 14:07:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-01 14:06:49 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.009 |  |
| 2026-02-01 14:06:24 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:13 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:00 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:05:57 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:05:22 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.070 |  |
| 2026-02-01 14:04:56 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:04:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-01 14:04:08 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-01 14:04:05 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:57 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:39 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 14:03:17 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:15 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-01 14:03:06 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-01 14:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:44 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.070 |  |
| 2026-02-01 14:01:59 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:58 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-02-01 14:01:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:37 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.050 |  |
| 2026-02-01 14:01:33 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | -0.012 |  |
| 2026-02-01 14:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:23 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-01 14:01:10 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:00:32 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 13:41:22 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-01 13:22:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 14:11:48 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-02-01 14:01:23 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-01 14:03:39 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-01 14:08:29 | Yaka Wewa (Ma Oya) | 1.20 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-02-01 14:10:58 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-01 13:00:55 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 14:00:32 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 14:01:55 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:44 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:10 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:13 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:59 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:17 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:01:59 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:04:56 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:12:25 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:57 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:04:05 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:05:57 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:00 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:03:15 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:02:50 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:24 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 14:06:49 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.009 |  |
| 2026-02-01 14:07:10 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.009 |  |
| 2026-02-01 14:04:08 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-01 14:03:08 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-02-01 14:01:33 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | -0.012 |  |
| 2026-02-01 14:03:06 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | -0.020 |  |
| 2026-02-01 14:04:22 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-02-01 13:02:48 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-02-01 13:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | -0.024 |  |
| 2026-02-01 14:01:58 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | -0.032 |  |
| 2026-02-01 13:22:16 | Pitabeddara (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.034 |  |
| 2026-02-01 14:01:37 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.050 |  |
| 2026-02-01 14:02:02 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.070 |  |
| 2026-02-01 14:05:22 | Rathnapura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)