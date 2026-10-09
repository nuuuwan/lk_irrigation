# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--10_01:07:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,622 measurements** from **39** stations.
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
| 2026-10-10 01:07:11 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-10-10 01:07:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:05:15 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-10 01:04:59 | Hanwella (Kelani Ganga) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 01:04:42 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.011 |  |
| 2026-10-10 01:04:32 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 01:04:26 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.200 |  |
| 2026-10-10 01:03:44 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-10 01:03:35 | Giriulla (Maha Oya) | 3.94 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-10-10 01:03:27 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-10 01:03:25 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-10-10 01:03:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:02:42 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.118 |  |
| 2026-10-10 01:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.061 |  |
| 2026-10-10 01:02:17 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | -0.127 |  |
| 2026-10-10 01:02:13 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-10-10 01:02:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-10-10 01:02:09 | Ellagawa (Kalu Ganga) | 6.79 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 01:02:07 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-10 01:02:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:49 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:39 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-10-10 01:01:36 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-10-10 01:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-10-10 01:01:23 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-10 01:01:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:06 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:00:57 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.101 |  |
| 2026-10-10 01:00:11 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-10 01:03:35 | Giriulla (Maha Oya) | 3.94 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-10-10 01:03:44 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-10 01:03:27 | Dunamale (Aththanagalu Oya) | 3.02 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-10-10 01:02:09 | Ellagawa (Kalu Ganga) | 6.79 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-10-10 01:02:07 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-10 00:07:18 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-10 01:05:15 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-10-10 00:04:46 | Pitabeddara (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-10 01:01:23 | Moragaswewa (Deduru Oya) | 2.20 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 18:10:37 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-10 01:04:59 | Hanwella (Kelani Ganga) | 4.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 01:04:32 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-09 18:01:41 | Weraganthota (Mahaweli Ganga) | -3.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-10 01:07:01 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:06 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:19 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:00:11 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:03:50 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:01:49 | Manampitiya (Mahaweli Ganga) | -0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 18:01:04 | Thanthirimale (Malwathu Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:03:05 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-10 01:02:00 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-10 00:04:01 | Norwood (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-10 01:04:42 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.011 |  |
| 2026-10-10 00:00:50 | Thawalama (Gin Ganga) | 2.13 | 🟢 Normal | -0.020 |  |
| 2026-10-10 01:01:31 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-10-10 01:01:39 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.024 |  |
| 2026-10-10 01:03:25 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.029 |  |
| 2026-10-10 01:02:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-10-10 01:01:36 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.040 |  |
| 2026-10-10 00:05:45 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.041 |  |
| 2026-10-10 01:02:13 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-10-10 01:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.20 | 🟢 Normal | -0.061 |  |
| 2026-10-10 01:07:11 | Holombuwa (Kelani Ganga) | 1.60 | 🟢 Normal | -0.097 |  |
| 2026-10-10 01:00:57 | Glencourse (Kelani Ganga) | 12.15 | 🟢 Normal | -0.101 |  |
| 2026-10-10 01:02:42 | Siyambalanduwa (Heda Oya) | 0.86 | 🟢 Normal | -0.118 |  |
| 2026-10-10 01:02:17 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | -0.127 |  |
| 2026-10-10 00:07:18 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.134 |  |
| 2026-10-10 01:04:26 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)