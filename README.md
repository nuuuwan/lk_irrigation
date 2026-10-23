# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_08:14:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,611 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 08:14:13 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.016 |  |
| 2026-10-23 08:13:23 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.027 |  |
| 2026-10-23 08:13:20 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.025 |  |
| 2026-10-23 08:13:10 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:08:48 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:08:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:08:24 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.047 |  |
| 2026-10-23 08:07:32 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.052 |  |
| 2026-10-23 08:07:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:05:14 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.094 |  |
| 2026-10-23 08:04:21 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-10-23 08:04:10 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:04:09 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:04:04 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:04:02 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.048 |  |
| 2026-10-23 08:03:58 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-10-23 08:03:44 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:03:37 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-10-23 08:03:32 | Galgamuwa (Mee Oya) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 08:03:31 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.060 |  |
| 2026-10-23 08:03:21 | Moragaswewa (Deduru Oya) | 4.87 | 🟡 Alert | -0.031 |  |
| 2026-10-23 08:03:18 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:03:10 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 08:02:54 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-23 08:02:54 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.088 |  |
| 2026-10-23 08:02:43 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:39 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.125 |  |
| 2026-10-23 08:02:34 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:02:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-23 08:02:03 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:01 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:01:37 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:01:28 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.075 |  |
| 2026-10-23 08:01:19 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.021 |  |
| 2026-10-23 08:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:00:37 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.082 |  |
| 2026-10-23 08:00:30 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-23 07:35:37 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 08:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-10-23 08:03:21 | Moragaswewa (Deduru Oya) | 4.87 | 🟡 Alert | -0.031 |  |
| 2026-10-23 08:03:10 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 08:00:30 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-23 08:03:32 | Galgamuwa (Mee Oya) | 2.64 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 08:08:26 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:01:37 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:08:48 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:31 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:04:09 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:01 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:43 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:04:04 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:07:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:02:03 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-23 08:04:10 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:03:44 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:02:34 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:03:18 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:13:10 | Thalgahagoda (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-10-23 08:14:13 | Urawa (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.016 |  |
| 2026-10-23 08:03:58 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-10-23 08:02:54 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2026-10-23 08:01:19 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | -0.021 |  |
| 2026-10-23 08:13:20 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.025 |  |
| 2026-10-23 08:13:23 | Panadugama (Nilwala Ganga) | 4.47 | 🟢 Normal | -0.027 |  |
| 2026-10-23 08:04:21 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | -0.041 |  |
| 2026-10-23 08:03:37 | Holombuwa (Kelani Ganga) | 1.24 | 🟢 Normal | -0.041 |  |
| 2026-10-23 08:08:24 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | -0.047 |  |
| 2026-10-23 08:04:02 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.048 |  |
| 2026-10-23 08:07:32 | Badalgama (Maha Oya) | 3.62 | 🟢 Normal | -0.052 |  |
| 2026-10-23 08:03:31 | Hanwella (Kelani Ganga) | 4.32 | 🟢 Normal | -0.060 |  |
| 2026-10-23 08:01:28 | Magura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.075 |  |
| 2026-10-23 07:06:12 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.075 |  |
| 2026-10-23 08:00:37 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | -0.082 |  |
| 2026-10-23 08:02:54 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | -0.088 |  |
| 2026-10-23 08:05:14 | Rathnapura (Kalu Ganga) | 4.00 | 🟢 Normal | -0.094 |  |
| 2026-10-23 08:02:39 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)