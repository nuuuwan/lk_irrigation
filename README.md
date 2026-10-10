# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_14:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,113 measurements** from **39** stations.
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
| 2026-10-10 14:11:25 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-10 14:10:08 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.082 |  |
| 2026-10-10 14:10:06 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-10 14:09:44 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-10-10 14:08:51 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.028 |  |
| 2026-10-10 14:08:30 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:08:05 | Dunamale (Aththanagalu Oya) | 3.19 | 🟢 Normal | -0.099 |  |
| 2026-10-10 14:08:01 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.098 |  |
| 2026-10-10 14:07:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -1.003 |  |
| 2026-10-10 14:07:05 | Badalgama (Maha Oya) | 4.30 | 🟢 Normal | -0.126 |  |
| 2026-10-10 14:06:02 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:05:34 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.043 |  |
| 2026-10-10 14:04:55 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 14:04:44 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-10 14:04:32 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.005 |  |
| 2026-10-10 14:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.030 |  |
| 2026-10-10 14:03:31 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-10 14:03:30 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.042 |  |
| 2026-10-10 14:03:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:03:22 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.060 |  |
| 2026-10-10 14:03:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:03:16 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:03:08 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.030 |  |
| 2026-10-10 14:02:34 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-10-10 14:02:10 | Ellagawa (Kalu Ganga) | 6.92 | 🟢 Normal | -0.061 |  |
| 2026-10-10 14:02:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:01:27 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 14:01:23 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -1.084 |  |
| 2026-10-10 14:01:18 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-10 14:01:17 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-10 14:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:00:51 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:00:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-10-10 14:00:40 | Moragaswewa (Deduru Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:00:34 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:00:30 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-10 13:36:02 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -1.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 14:10:06 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-10-10 14:01:18 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-10 14:04:44 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-10 14:03:31 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-10 14:11:25 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-10 14:01:27 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 14:00:34 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:06:02 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:01:56 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:00:51 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:03:17 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:03:16 | Moraketiya (Walawe Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:08:30 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:02:04 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:02:34 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-10 14:09:44 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.005 |  |
| 2026-10-10 14:04:32 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | -0.005 |  |
| 2026-10-10 13:15:27 | Urawa (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.008 |  |
| 2026-10-10 14:03:28 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:00:30 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:00:59 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:00:40 | Moragaswewa (Deduru Oya) | 2.44 | 🟢 Normal | -0.010 |  |
| 2026-10-10 14:01:17 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.011 |  |
| 2026-10-10 14:00:46 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-10-10 14:08:51 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.028 |  |
| 2026-10-10 14:03:08 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.030 |  |
| 2026-10-10 14:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.60 | 🟢 Normal | -0.030 |  |
| 2026-10-10 14:02:19 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.031 |  |
| 2026-10-10 14:03:30 | Panadugama (Nilwala Ganga) | 4.25 | 🟢 Normal | -0.042 |  |
| 2026-10-10 14:05:34 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.043 |  |
| 2026-10-10 14:04:55 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.049 |  |
| 2026-10-10 14:03:22 | Hanwella (Kelani Ganga) | 3.27 | 🟢 Normal | -0.060 |  |
| 2026-10-10 14:02:10 | Ellagawa (Kalu Ganga) | 6.92 | 🟢 Normal | -0.061 |  |
| 2026-10-10 14:10:08 | Rathnapura (Kalu Ganga) | 2.45 | 🟢 Normal | -0.082 |  |
| 2026-10-10 14:08:01 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.098 |  |
| 2026-10-10 14:08:05 | Dunamale (Aththanagalu Oya) | 3.19 | 🟢 Normal | -0.099 |  |
| 2026-10-10 14:07:05 | Badalgama (Maha Oya) | 4.30 | 🟢 Normal | -0.126 |  |
| 2026-10-10 14:07:09 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -1.003 |  |
| 2026-10-10 14:01:23 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | -1.084 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)