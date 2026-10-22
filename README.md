# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_02:07:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,375 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 02:07:56 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | -0.028 |  |
| 2026-10-23 02:07:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:07:45 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:51 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:36 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:21 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:05:38 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:05:36 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.073 |  |
| 2026-10-23 02:05:25 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:04:34 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.082 |  |
| 2026-10-23 02:04:24 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 02:04:23 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-23 02:03:37 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -0.068 |  |
| 2026-10-23 02:03:22 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-10-23 02:03:16 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 02:03:07 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-23 02:03:01 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:02:48 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.058 |  |
| 2026-10-23 02:02:45 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:02:03 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:01:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:01:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:00:59 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:00:55 | Moragaswewa (Deduru Oya) | 5.27 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-10-23 02:00:29 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 02:00:55 | Moragaswewa (Deduru Oya) | 5.27 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-10-23 00:07:50 | Putupaula (Kalu Ganga) | 1.90 | 🟢 Normal | 0.924 | 🔺 Rising |
| 2026-10-23 00:06:30 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-23 01:06:02 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-23 02:03:16 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-23 00:07:11 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-23 02:04:23 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 23:08:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-23 02:04:24 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-23 02:00:29 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 01:01:29 | Hanwella (Kelani Ganga) | 4.61 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-23 02:01:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:21 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:05:38 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:02:09 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:00:59 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:51 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-23 01:01:57 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:07:46 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:01:36 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:06:36 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-23 02:05:25 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:02:45 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:02:03 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-23 02:03:01 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:03:06 | Manampitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-23 01:03:52 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-10-23 02:03:07 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.021 |  |
| 2026-10-23 00:07:00 | Urawa (Nilwala Ganga) | 1.19 | 🟢 Normal | -0.022 |  |
| 2026-10-23 02:03:22 | Padiyathalawa (Maduru Oya) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-10-23 02:07:56 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | -0.028 |  |
| 2026-10-23 02:02:48 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.058 |  |
| 2026-10-23 02:03:37 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | -0.068 |  |
| 2026-10-23 01:17:44 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.068 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-23 02:05:36 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.073 |  |
| 2026-10-23 02:04:34 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.082 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)