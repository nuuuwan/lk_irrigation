# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_08:25:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,958 measurements** from **39** stations.
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
| 2026-08-15 08:25:29 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-08-15 08:20:55 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-15 08:14:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:12:32 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-15 08:11:12 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:10:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:09:01 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:08:01 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-15 08:06:46 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-15 08:05:48 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:40 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:23 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-15 08:05:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:09 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-15 08:04:41 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 08:04:28 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-08-15 08:03:39 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-15 08:03:26 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:03:23 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-15 08:03:22 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-15 08:03:21 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.098 |  |
| 2026-08-15 08:02:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:56 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 08:02:50 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.100 |  |
| 2026-08-15 08:02:44 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.032 |  |
| 2026-08-15 08:02:37 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.149 |  |
| 2026-08-15 08:02:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 08:02:04 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:01:50 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-08-15 08:01:32 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.133 |  |
| 2026-08-15 08:01:30 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-08-15 08:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:01:07 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:00:49 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:00:47 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 08:03:39 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-15 08:05:23 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-15 08:06:46 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-08-15 08:08:01 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-15 08:03:23 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-15 08:03:22 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-08-15 08:05:09 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-15 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 08:02:56 | Ellagawa (Kalu Ganga) | 6.07 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-15 08:04:41 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 08:20:55 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-15 08:02:04 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:56 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:35 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:03:26 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:01:07 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:48 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:09:01 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:35 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:40 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:02:50 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:14:50 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:05:37 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:11:12 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:00:49 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:10:20 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:00:47 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-15 08:12:32 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-08-15 08:01:50 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.010 |  |
| 2026-08-15 08:01:30 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.011 |  |
| 2026-08-15 08:04:28 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.021 |  |
| 2026-08-15 08:25:29 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.030 |  |
| 2026-08-15 08:02:44 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.032 |  |
| 2026-08-15 08:03:21 | Kithulgala (Kelani Ganga) | 2.00 | 🟢 Normal | -0.098 |  |
| 2026-08-15 08:02:47 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.100 |  |
| 2026-08-15 08:01:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.133 |  |
| 2026-08-15 08:02:37 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)