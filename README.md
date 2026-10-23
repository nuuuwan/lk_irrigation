# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_07:14:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,572 measurements** from **39** stations.
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
| 2026-10-23 07:14:11 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:12:38 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:10:25 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-23 07:10:21 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.036 |  |
| 2026-10-23 07:09:23 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-10-23 07:09:10 | Galgamuwa (Mee Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:07:27 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.086 |  |
| 2026-10-23 07:07:19 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-10-23 07:06:12 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.075 |  |
| 2026-10-23 07:05:39 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-10-23 07:05:12 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:05:11 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-10-23 07:04:50 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:04:48 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 07:04:45 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-23 07:04:36 | Moragaswewa (Deduru Oya) | 4.90 | 🟡 Alert | -0.030 |  |
| 2026-10-23 07:04:21 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:59 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:45 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:30 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.077 |  |
| 2026-10-23 07:03:26 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:02:59 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-23 07:02:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:02:46 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 07:02:42 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-10-23 07:02:34 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:02:22 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 07:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:02:17 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:01:47 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.158 |  |
| 2026-10-23 07:01:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:01:32 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-10-23 07:01:28 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.113 |  |
| 2026-10-23 07:01:19 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:01:17 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.085 |  |
| 2026-10-23 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.134 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 07:02:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.07 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-10-23 07:04:36 | Moragaswewa (Deduru Oya) | 4.90 | 🟡 Alert | -0.030 |  |
| 2026-10-23 07:10:25 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-10-23 07:04:45 | Horowpothana (Yan Oya) | 3.03 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-10-23 07:02:22 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-23 07:04:48 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 07:02:46 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 07:04:21 | Giriulla (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:09:10 | Galgamuwa (Mee Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:59 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:45 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:03:45 | Putupaula (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:04:50 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-23 06:09:40 | Urawa (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:14:11 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:01:19 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-23 07:02:17 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:02:05 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:02:55 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-10-23 07:07:19 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.019 |  |
| 2026-10-23 07:05:12 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:02:34 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:03:26 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.020 |  |
| 2026-10-23 07:02:42 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.021 |  |
| 2026-10-23 07:09:23 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.027 |  |
| 2026-10-23 07:02:18 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:02:59 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:01:42 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-10-23 07:10:21 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.036 |  |
| 2026-10-23 07:01:32 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | -0.038 |  |
| 2026-10-23 07:05:39 | Dunamale (Aththanagalu Oya) | 2.86 | 🟢 Normal | -0.040 |  |
| 2026-10-23 07:05:11 | Magura (Kalu Ganga) | 2.35 | 🟢 Normal | -0.067 |  |
| 2026-10-23 07:06:12 | Thawalama (Gin Ganga) | 2.22 | 🟢 Normal | -0.075 |  |
| 2026-10-23 07:03:30 | Hanwella (Kelani Ganga) | 4.38 | 🟢 Normal | -0.077 |  |
| 2026-10-23 07:01:17 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.085 |  |
| 2026-10-23 07:07:27 | Panadugama (Nilwala Ganga) | 4.50 | 🟢 Normal | -0.086 |  |
| 2026-10-23 07:01:28 | Rathnapura (Kalu Ganga) | 4.10 | 🟢 Normal | -0.113 |  |
| 2026-10-23 07:00:16 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.134 |  |
| 2026-10-23 07:01:47 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)