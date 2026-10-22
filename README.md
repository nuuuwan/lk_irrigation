# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_03:20:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,421 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 03:20:22 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.083 |  |
| 2026-10-23 03:16:51 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:13:45 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.078 |  |
| 2026-10-23 03:10:20 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-23 03:09:40 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.023 |  |
| 2026-10-23 03:08:58 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-23 03:07:55 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.139 |  |
| 2026-10-23 03:07:34 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.077 |  |
| 2026-10-23 03:07:32 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.031 |  |
| 2026-10-23 03:07:00 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-10-23 03:06:51 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:06:45 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-23 03:06:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.075 |  |
| 2026-10-23 03:06:24 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.057 |  |
| 2026-10-23 03:05:30 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:05:12 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-23 03:05:12 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-23 03:05:01 | Badalgama (Maha Oya) | 3.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-23 03:04:40 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.256 |  |
| 2026-10-23 03:04:37 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:04:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 03:04:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -1.166 |  |
| 2026-10-23 03:03:58 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-23 03:03:57 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-23 03:03:56 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-23 03:03:46 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:03:44 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-10-23 03:03:35 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-10-23 03:02:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-23 03:02:58 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:02:56 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 03:02:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-23 03:02:07 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | -0.011 |  |
| 2026-10-23 03:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-23 03:01:21 | Moragaswewa (Deduru Oya) | 5.29 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-23 03:00:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 03:00:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:56:16 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 03:01:21 | Moragaswewa (Deduru Oya) | 5.29 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-10-23 03:03:58 | Pitabeddara (Nilwala Ganga) | 2.24 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-10-23 03:05:12 | Putupaula (Kalu Ganga) | 2.06 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-23 03:05:01 | Badalgama (Maha Oya) | 3.79 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-23 03:02:59 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-23 03:05:12 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 03:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 03:10:20 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-23 03:08:58 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-23 03:04:33 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 03:00:30 | Magura (Kalu Ganga) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 03:16:51 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:02:56 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:00:24 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:05:30 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-23 03:06:45 | Norwood (Kelani Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-10-23 03:02:58 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:03:46 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:06:51 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:04:37 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-10-23 03:02:07 | Horowpothana (Yan Oya) | 3.00 | 🟢 Normal | -0.011 |  |
| 2026-10-23 03:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-23 03:07:00 | Thawalama (Gin Ganga) | 2.49 | 🟢 Normal | -0.019 |  |
| 2026-10-23 03:03:44 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.021 |  |
| 2026-10-23 03:02:25 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-10-23 03:09:40 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.023 |  |
| 2026-10-23 03:03:35 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.030 |  |
| 2026-10-23 03:07:32 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | -0.031 |  |
| 2026-10-23 03:06:24 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.057 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-23 03:06:37 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.075 |  |
| 2026-10-23 03:07:34 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.077 |  |
| 2026-10-23 03:13:45 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.078 |  |
| 2026-10-23 03:20:22 | Rathnapura (Kalu Ganga) | 4.47 | 🟢 Normal | -0.083 |  |
| 2026-10-23 03:07:55 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.139 |  |
| 2026-10-23 03:04:40 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | -0.256 |  |
| 2026-10-23 03:04:25 | Wellawaya (Kirindi Oya) | 1.47 | 🟢 Normal | -1.166 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)