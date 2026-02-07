# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--07_10:43:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **66,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 10:43:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:16:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:10:58 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:07:37 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-02-07 10:07:04 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:06:40 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:06:23 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:05:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.119 |  |
| 2026-02-07 10:05:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.067 |  |
| 2026-02-07 10:04:58 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-02-07 10:04:43 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:04:27 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.021 |  |
| 2026-02-07 10:04:17 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 10:03:57 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-07 10:03:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:50 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.115 |  |
| 2026-02-07 10:03:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-02-07 10:03:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:32 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-07 10:03:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-07 10:03:20 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.070 |  |
| 2026-02-07 10:03:15 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-07 10:03:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:02:54 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:02:51 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.067 |  |
| 2026-02-07 10:02:11 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.080 |  |
| 2026-02-07 10:02:08 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.069 |  |
| 2026-02-07 10:01:56 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:51 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-02-07 10:01:37 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:33 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:21 | Weraganthota (Mahaweli Ganga) | -1.68 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-07 10:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:00:54 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-02-07 10:00:54 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 10:00:10 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-07 10:03:57 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-02-07 10:01:21 | Weraganthota (Mahaweli Ganga) | -1.68 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-07 10:03:30 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-07 10:03:32 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-07 10:00:54 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 10:01:33 | Manampitiya (Mahaweli Ganga) | 2.02 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-07 10:04:17 | Ellagawa (Kalu Ganga) | 4.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-07 10:01:37 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:56 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:04:43 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:02:55 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:02:54 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:06:40 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:04 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:13 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:06:23 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:50 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:03:37 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:43:07 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:07:04 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:01:09 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:10:58 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:16:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-02-07 10:04:58 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-02-07 10:03:15 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-02-07 10:00:10 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-07 10:00:54 | Horowpothana (Yan Oya) | 2.67 | 🟢 Normal | -0.020 |  |
| 2026-02-07 10:04:27 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.021 |  |
| 2026-02-07 10:01:51 | Padiyathalawa (Maduru Oya) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-02-07 10:03:47 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.029 |  |
| 2026-02-07 10:07:37 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.049 |  |
| 2026-02-07 10:05:01 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.067 |  |
| 2026-02-07 10:02:51 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.067 |  |
| 2026-02-07 10:02:08 | Baddegama (Gin Ganga) | 1.66 | 🟢 Normal | -0.069 |  |
| 2026-02-07 10:03:20 | Rathnapura (Kalu Ganga) | 1.01 | 🟢 Normal | -0.070 |  |
| 2026-02-07 10:02:11 | Kithulgala (Kelani Ganga) | 1.12 | 🟢 Normal | -0.080 |  |
| 2026-02-07 10:03:50 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.115 |  |
| 2026-02-07 10:05:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)