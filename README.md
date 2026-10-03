# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--03_13:20:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **277,778 measurements** from **39** stations.
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
| 2026-10-03 13:20:58 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:17:49 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.032 |  |
| 2026-10-03 13:16:27 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.036 |  |
| 2026-10-03 13:16:14 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-03 13:13:50 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:12:50 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-03 13:10:11 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:08:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:07:40 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.070 |  |
| 2026-10-03 13:07:03 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-03 13:07:02 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-10-03 13:06:18 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:05:54 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-03 13:04:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:04:57 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:04:53 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.051 |  |
| 2026-10-03 13:04:53 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-03 13:04:50 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 13:04:24 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.068 |  |
| 2026-10-03 13:03:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:03:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:03:30 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-03 13:03:30 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2026-10-03 13:03:10 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.040 |  |
| 2026-10-03 13:02:29 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:02:18 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:02:12 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 13:02:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:01:42 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-10-03 13:01:30 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:01:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-03 13:00:56 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:00:44 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-03 13:00:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:00:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-03 13:04:39 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-10-03 13:03:30 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-03 13:04:53 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-03 13:01:09 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-03 13:02:12 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-03 13:16:14 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-10-03 13:01:30 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:00:22 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:01:53 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:01:57 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:00:32 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:08:43 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:10:11 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:13:50 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:20:58 | Panadugama (Nilwala Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:03:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:06:18 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:04:50 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:03:59 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:00:56 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:02:29 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-03 13:12:50 | Rathnapura (Kalu Ganga) | 1.97 | 🟢 Normal | -0.009 |  |
| 2026-10-03 13:07:02 | Dunamale (Aththanagalu Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-10-03 13:04:57 | Holombuwa (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:04:59 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:02:05 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:05:54 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:02:18 | Giriulla (Maha Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-10-03 13:00:44 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.011 |  |
| 2026-10-03 13:07:03 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-10-03 13:01:42 | Weraganthota (Mahaweli Ganga) | -3.50 | 🟢 Normal | -0.020 |  |
| 2026-10-03 13:17:49 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.032 |  |
| 2026-10-03 13:16:27 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | -0.036 |  |
| 2026-10-03 13:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-03 13:03:10 | Hanwella (Kelani Ganga) | 2.29 | 🟢 Normal | -0.040 |  |
| 2026-10-03 13:04:53 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.051 |  |
| 2026-10-03 13:03:30 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.052 |  |
| 2026-10-03 13:04:24 | Ellagawa (Kalu Ganga) | 6.31 | 🟢 Normal | -0.068 |  |
| 2026-10-03 13:07:40 | Glencourse (Kelani Ganga) | 10.42 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)