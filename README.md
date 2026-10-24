# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--24_16:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,809 measurements** from **39** stations.
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
| 2026-10-24 16:10:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:08:45 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-24 16:08:42 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:08:30 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:29 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:06:28 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:15 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.054 |  |
| 2026-10-24 16:06:04 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-24 16:05:46 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:05:25 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:05:02 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:05:00 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:04:55 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:04:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-10-24 16:04:45 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-10-24 16:04:44 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:04:27 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | -0.077 |  |
| 2026-10-24 16:04:14 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:03:43 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:03:29 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:03:23 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:03:20 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:03:18 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.049 |  |
| 2026-10-24 16:03:03 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:02:57 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:02:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-10-24 16:02:53 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.085 |  |
| 2026-10-24 16:02:42 | Kuda Oya (Kirindi Oya) | 2.23 | 🟢 Normal | 1.007 | 🔺 Rising |
| 2026-10-24 16:02:30 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.096 |  |
| 2026-10-24 16:02:08 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:02:06 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-10-24 16:01:53 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:01:33 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 16:01:29 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:01:22 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 16:01:16 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:00:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-24 16:02:42 | Kuda Oya (Kirindi Oya) | 2.23 | 🟢 Normal | 1.007 | 🔺 Rising |
| 2026-10-24 16:06:04 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | 0.168 | 🔺 Rising |
| 2026-10-24 16:01:33 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-24 16:01:21 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-24 16:01:29 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:08:30 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:01:16 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:08:42 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:01:22 | Pitabeddara (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:51 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:10:21 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:05:02 | Panadugama (Nilwala Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:05:00 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:00:32 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:03:03 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:06:28 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:04:55 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:04:14 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-24 16:03:43 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:06:29 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:01:53 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:03:20 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:02:08 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:03:23 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:05:46 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:04:44 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.010 |  |
| 2026-10-24 16:08:45 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.018 |  |
| 2026-10-24 16:04:45 | Thanthirimale (Malwathu Oya) | 1.72 | 🟢 Normal | -0.019 |  |
| 2026-10-24 16:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.83 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:02:57 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:05:25 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-10-24 16:02:54 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-10-24 16:02:06 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-10-24 16:03:18 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.049 |  |
| 2026-10-24 16:06:15 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.054 |  |
| 2026-10-24 16:04:27 | Moragaswewa (Deduru Oya) | 1.60 | 🟢 Normal | -0.077 |  |
| 2026-10-24 16:02:53 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | -0.085 |  |
| 2026-10-24 16:04:46 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.091 |  |
| 2026-10-24 16:02:30 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)