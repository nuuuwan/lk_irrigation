# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_17:05:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,297 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 17:05:19 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-15 17:05:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:04:46 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-15 17:04:24 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.039 |  |
| 2026-08-15 17:04:18 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:04:07 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:03:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:32 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.081 |  |
| 2026-08-15 17:03:30 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-08-15 17:03:19 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:08 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.012 |  |
| 2026-08-15 17:02:49 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.070 |  |
| 2026-08-15 17:02:49 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.030 |  |
| 2026-08-15 17:02:46 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:41 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:20 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-15 17:02:18 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-08-15 17:02:10 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:02:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-15 17:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:02 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-08-15 17:01:11 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:00:47 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:29:13 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-15 16:27:23 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 17:03:30 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-08-15 17:02:20 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-15 17:02:10 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-15 17:04:46 | Siyambalanduwa (Heda Oya) | 0.23 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-15 17:05:19 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-15 16:27:23 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-15 16:01:11 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-15 16:12:08 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-15 17:02:46 | Wellawaya (Kirindi Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:41 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:02:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:18 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:01:11 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:32 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:05:49 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:02 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:02:57 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:06:44 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:19 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:03:46 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:08 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:04:07 | Rathnapura (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:00:47 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-15 16:06:41 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:05:09 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:02:41 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 17:03:50 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:02:10 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:04:18 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-08-15 17:03:08 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.012 |  |
| 2026-08-15 16:10:54 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-08-15 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.16 | 🟢 Normal | -0.020 |  |
| 2026-08-15 17:02:49 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | -0.030 |  |
| 2026-08-15 17:02:01 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-08-15 17:04:24 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.039 |  |
| 2026-08-15 16:09:16 | Peradeniya (Mahaweli Ganga) | 2.83 | 🟢 Normal | -0.063 |  |
| 2026-08-15 17:02:49 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.070 |  |
| 2026-08-15 17:03:32 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.081 |  |
| 2026-08-15 16:06:03 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.134 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)