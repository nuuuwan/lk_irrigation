# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_05:31:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,659 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Baddegama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 05:31:31 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -7.059 |  |
| 2026-09-21 05:30:40 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -7.059 |  |
| 2026-09-21 05:23:46 | Rathnapura (Kalu Ganga) | 6.12 | 🟡 Alert | -0.054 |  |
| 2026-09-21 05:21:17 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.128 |  |
| 2026-09-21 05:19:21 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:12:19 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.026 |  |
| 2026-09-21 05:11:50 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:09:48 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-21 05:09:18 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-21 05:08:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:08:03 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.063 |  |
| 2026-09-21 05:07:46 | Glencourse (Kelani Ganga) | 14.85 | 🟢 Normal | -0.201 |  |
| 2026-09-21 05:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2026-09-21 05:05:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:05:15 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.143 |  |
| 2026-09-21 05:04:49 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.061 |  |
| 2026-09-21 05:04:33 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 05:04:32 | Magura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.019 |  |
| 2026-09-21 05:04:19 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 05:04:15 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-09-21 05:04:11 | Hanwella (Kelani Ganga) | 6.84 | 🟢 Normal | -0.010 |  |
| 2026-09-21 05:03:35 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.680 | 🔺 Rising |
| 2026-09-21 05:03:18 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:51 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 05:02:42 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:26 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.010 |  |
| 2026-09-21 05:02:08 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:02 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-09-21 05:02:01 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.779 | 🔺 Rising |
| 2026-09-21 05:01:57 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:01:52 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-21 05:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-09-21 05:01:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 05:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 05:12:19 | Panadugama (Nilwala Ganga) | 6.02 | 🟠 Minor Flood | -0.026 |  |
| 2026-09-21 05:07:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.147 | 🔺 Rising |
| 2026-09-21 05:02:02 | Thalgahagoda (Nilwala Ganga) | 1.49 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-09-21 05:09:48 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-21 05:02:26 | Dunamale (Aththanagalu Oya) | 3.42 | 🟡 Alert | -0.010 |  |
| 2026-09-21 05:04:32 | Magura (Kalu Ganga) | 5.68 | 🟡 Alert | -0.019 |  |
| 2026-09-21 05:23:46 | Rathnapura (Kalu Ganga) | 6.12 | 🟡 Alert | -0.054 |  |
| 2026-09-21 05:01:19 | Thawalama (Gin Ganga) | 4.86 | 🟡 Alert | -0.233 |  |
| 2026-09-21 05:02:01 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.779 | 🔺 Rising |
| 2026-09-21 05:03:35 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.680 | 🔺 Rising |
| 2026-09-21 05:09:18 | Ellagawa (Kalu Ganga) | 8.78 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 05:04:33 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 05:02:47 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 05:01:52 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 05:04:19 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 05:02:51 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:03:18 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:42 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:11:50 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:08:34 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:19:21 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:05:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:01:57 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-09-21 05:02:08 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 05:04:11 | Hanwella (Kelani Ganga) | 6.84 | 🟢 Normal | -0.010 |  |
| 2026-09-21 05:01:51 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-09-21 05:01:51 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-09-21 05:04:49 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.061 |  |
| 2026-09-21 05:08:03 | Holombuwa (Kelani Ganga) | 1.50 | 🟢 Normal | -0.063 |  |
| 2026-09-21 05:04:15 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.070 |  |
| 2026-09-21 05:21:17 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.128 |  |
| 2026-09-21 05:05:15 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.143 |  |
| 2026-09-21 05:07:46 | Glencourse (Kelani Ganga) | 14.85 | 🟢 Normal | -0.201 |  |
| 2026-09-21 05:01:23 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.426 |  |
| 2026-09-21 05:31:31 | Norwood (Kelani Ganga) | 1.27 | 🟢 Normal | -7.059 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)