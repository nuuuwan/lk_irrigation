# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_14:21:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **294,051 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 14:21:03 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:14:41 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-10-21 14:11:02 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:10:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-10-21 14:08:50 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:07:35 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-21 14:07:09 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:06:58 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:06:20 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 14:06:17 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 14:05:50 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.009 |  |
| 2026-10-21 14:05:36 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 14:04:49 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-10-21 14:04:47 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:04:25 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 14:04:12 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.037 |  |
| 2026-10-21 14:03:55 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.030 |  |
| 2026-10-21 14:03:45 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:03:32 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 14:03:22 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:03:22 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.089 |  |
| 2026-10-21 14:02:59 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.079 |  |
| 2026-10-21 14:02:51 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:02:51 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-10-21 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-21 14:02:30 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 14:02:21 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-10-21 14:02:06 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:02:04 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-10-21 14:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:01:40 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:01:35 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:37 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:00:15 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 14:02:38 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-21 14:06:20 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 14:04:25 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 14:02:30 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 14:03:32 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 14:05:36 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 14:06:17 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-21 14:01:40 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:46 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:01:46 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:01:35 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:15 | Magura (Kalu Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:03:22 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:08:50 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:06:58 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:07:09 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:11:02 | Urawa (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:00:37 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:02:21 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-21 14:14:41 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.009 |  |
| 2026-10-21 14:05:50 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.009 |  |
| 2026-10-21 14:04:47 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:21:03 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:03:45 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:00:18 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:03:22 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:02:06 | Ellagawa (Kalu Ganga) | 5.57 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:02:51 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-10-21 14:10:16 | Siyambalanduwa (Heda Oya) | 0.67 | 🟢 Normal | -0.018 |  |
| 2026-10-21 14:04:49 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.019 |  |
| 2026-10-21 14:00:12 | Weraganthota (Mahaweli Ganga) | -2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-21 14:02:04 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-10-21 14:02:51 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.021 |  |
| 2026-10-21 14:03:55 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.030 |  |
| 2026-10-21 14:07:35 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.030 |  |
| 2026-10-21 14:02:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.031 |  |
| 2026-10-21 14:04:12 | Thalgahagoda (Nilwala Ganga) | 1.24 | 🟢 Normal | -0.037 |  |
| 2026-10-21 14:02:59 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | -0.079 |  |
| 2026-10-21 14:03:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.86 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)