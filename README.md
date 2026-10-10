# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_16:31:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,195 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 16:31:36 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.007 |  |
| 2026-10-10 16:18:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.008 |  |
| 2026-10-10 16:15:08 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.087 |  |
| 2026-10-10 16:13:28 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-10 16:12:29 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.122 |  |
| 2026-10-10 16:11:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-10-10 16:11:08 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-10 16:09:12 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-10-10 16:08:59 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 16:08:15 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-10 16:07:08 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:07:04 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:06:34 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.068 |  |
| 2026-10-10 16:06:20 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-10 16:05:37 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-10 16:05:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.137 |  |
| 2026-10-10 16:05:17 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.079 |  |
| 2026-10-10 16:05:01 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 16:04:20 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.028 |  |
| 2026-10-10 16:04:18 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:04:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 16:04:17 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.050 |  |
| 2026-10-10 16:03:47 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:03:40 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:03:37 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-10 16:03:36 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-10 16:03:24 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:03:23 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:03:01 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.050 |  |
| 2026-10-10 16:02:40 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.021 |  |
| 2026-10-10 16:02:14 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-10 16:02:11 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.070 |  |
| 2026-10-10 16:02:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:56 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:21 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-10-10 16:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:01:06 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:03 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 16:13:28 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-10-10 16:03:36 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-10 16:03:37 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-10 16:05:37 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-10 16:05:01 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-10 16:04:17 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 16:08:59 | Deraniyagala (Kelani Ganga) | 0.66 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-10 16:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:02:10 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:03 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:56 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:04:18 | Panadugama (Nilwala Ganga) | 4.21 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:03:40 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:07:08 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:03:24 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:01:06 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:07:04 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-10 16:31:36 | Magura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.007 |  |
| 2026-10-10 16:18:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.008 |  |
| 2026-10-10 16:11:08 | Urawa (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-10-10 16:09:12 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.009 |  |
| 2026-10-10 16:03:47 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:02:40 | Moragaswewa (Deduru Oya) | 2.42 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:01:15 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-10 16:01:21 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2026-10-10 16:11:37 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.018 |  |
| 2026-10-10 16:06:20 | Pitabeddara (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.019 |  |
| 2026-10-10 16:02:14 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | -0.021 |  |
| 2026-10-10 16:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.021 |  |
| 2026-10-10 16:04:20 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.028 |  |
| 2026-10-10 16:08:15 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | -0.039 |  |
| 2026-10-10 16:04:17 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.050 |  |
| 2026-10-10 16:03:01 | Hanwella (Kelani Ganga) | 3.18 | 🟢 Normal | -0.050 |  |
| 2026-10-10 16:06:34 | Badalgama (Maha Oya) | 4.15 | 🟢 Normal | -0.068 |  |
| 2026-10-10 16:02:11 | Giriulla (Maha Oya) | 3.08 | 🟢 Normal | -0.070 |  |
| 2026-10-10 16:05:17 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | -0.079 |  |
| 2026-10-10 16:15:08 | Rathnapura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.087 |  |
| 2026-10-10 16:12:29 | Dunamale (Aththanagalu Oya) | 2.96 | 🟢 Normal | -0.122 |  |
| 2026-10-10 16:05:33 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.137 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)