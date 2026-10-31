# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--01_01:29:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **303,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 01:29:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-01 01:18:57 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:14:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | -72.000 |  |
| 2026-11-01 01:14:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.02 | 🟢 Normal | -72.000 |  |
| 2026-11-01 01:09:38 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:09:05 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-01 01:07:54 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:06:44 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:06:11 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-11-01 01:05:56 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:05:36 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-01 01:05:33 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-01 01:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:05:17 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:04:50 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-01 01:04:13 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-01 01:04:12 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.064 |  |
| 2026-11-01 01:04:01 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 01:03:45 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:03:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:03:32 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:03:02 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:03:00 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-01 01:02:58 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:48 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:02:37 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:01:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-11-01 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-01 01:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:00:23 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-01 01:01:15 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.034 | 🔺 Rising |
| 2026-11-01 01:05:36 | Pitabeddara (Nilwala Ganga) | 1.65 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-01 01:04:13 | Ellagawa (Kalu Ganga) | 6.05 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-01 01:04:50 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-01 01:09:05 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-11-01 01:29:03 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-01 01:04:01 | Rathnapura (Kalu Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-01 01:00:23 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:37 | Moragaswewa (Deduru Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:02 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:48 | Horowpothana (Yan Oya) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:03:45 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:03:45 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:09:38 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:18:57 | Glencourse (Kelani Ganga) | 10.15 | 🟢 Normal | 0.000 |  |
| 2026-11-01 00:10:44 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:00:50 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:03:44 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:07:54 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:02:58 | Thawalama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-01 01:05:17 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:05:21 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.009 |  |
| 2026-11-01 01:05:56 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:06:44 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:03:32 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:11 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-11-01 01:02:27 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-31 18:00:38 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-01 00:02:39 | Magura (Kalu Ganga) | 1.95 | 🟢 Normal | -0.011 |  |
| 2026-10-31 18:01:51 | Galgamuwa (Mee Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-11-01 01:05:33 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-10-31 18:04:44 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-01 01:01:44 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.021 |  |
| 2026-11-01 01:06:11 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.039 |  |
| 2026-11-01 01:03:00 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.041 |  |
| 2026-11-01 01:02:39 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:03:02 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | -0.061 |  |
| 2026-11-01 01:04:12 | Thanamalwila (Kirindi Oya) | 1.62 | 🟢 Normal | -0.064 |  |
| 2026-11-01 01:14:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)