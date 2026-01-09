# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_14:08:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,953 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 14:08:46 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-01-09 14:08:30 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.043 |  |
| 2026-01-09 14:08:13 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.011 |  |
| 2026-01-09 14:07:36 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:07:28 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:06:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:06:10 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 14:06:10 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:05:41 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-09 14:05:11 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:04:57 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-09 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.092 |  |
| 2026-01-09 14:04:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:04:17 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:04:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-01-09 14:03:29 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:03:04 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:48 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:37 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-09 14:02:32 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:25 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:16 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-09 14:01:58 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:56 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.273 |  |
| 2026-01-09 14:01:49 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:43 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 14:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:41 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:32 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-09 14:01:21 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 14:01:12 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 14:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-01-09 14:01:04 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-09 14:00:52 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:00:41 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:00:14 | Weraganthota (Mahaweli Ganga) | -1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:55:08 | Weraganthota (Mahaweli Ganga) | -1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:17:55 | Moragaswewa (Deduru Oya) | 1.70 | 🟢 Normal | -0.273 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 14:02:16 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-09 14:02:37 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-09 14:04:57 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-09 14:01:12 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 14:01:43 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 14:01:21 | Horowpothana (Yan Oya) | 2.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-09 14:00:52 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:00:41 | Manampitiya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:07:36 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 14:06:10 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-09 14:00:14 | Weraganthota (Mahaweli Ganga) | -1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:39 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:42 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:00:45 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:32 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:04:17 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:05:11 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:25 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:03:29 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:41 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-09 13:05:23 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:03:04 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:23 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:01:58 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:02:48 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:06:48 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:04:46 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:07:28 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:06:10 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-01-09 14:08:46 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-01-09 14:01:04 | Pitabeddara (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-01-09 14:01:32 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-01-09 14:08:13 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.011 |  |
| 2026-01-09 14:04:03 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-01-09 14:05:41 | Baddegama (Gin Ganga) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-09 14:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-01-09 14:08:30 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.043 |  |
| 2026-01-09 14:04:48 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.092 |  |
| 2026-01-09 14:01:56 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | -0.273 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)