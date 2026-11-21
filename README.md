# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_09:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **321,678 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 09:03:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:03:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-11-21 09:03:12 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 09:02:41 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 09:02:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:02:39 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:02:32 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-21 09:02:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.701 |  |
| 2026-11-21 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-21 09:01:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.172 |  |
| 2026-11-21 09:01:54 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-21 09:01:47 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:01:34 | Giriulla (Maha Oya) | 3.86 | 🟢 Normal | 1.163 | 🔺 Rising |
| 2026-11-21 09:01:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 09:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:01:16 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-21 09:00:58 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 09:00:58 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:00:45 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-11-21 08:32:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.120 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 08:02:54 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-11-21 09:01:34 | Giriulla (Maha Oya) | 3.86 | 🟢 Normal | 1.163 | 🔺 Rising |
| 2026-11-21 08:05:52 | Magura (Kalu Ganga) | 1.89 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-11-21 08:03:19 | Ellagawa (Kalu Ganga) | 5.48 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-21 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-21 09:03:12 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-21 09:01:33 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-21 08:09:47 | Dunamale (Aththanagalu Oya) | 1.69 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:05:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-21 08:03:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-21 09:02:41 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 07:08:34 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 08:09:14 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-21 09:00:58 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 08:05:21 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-21 09:01:47 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 09:02:39 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 08:05:33 | Moraketiya (Walawe Ganga) | 2.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-21 08:05:37 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:00:58 | Moragaswewa (Deduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:01:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:05:30 | Horowpothana (Yan Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:03:33 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:02:40 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-21 09:03:37 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-21 08:04:43 | Rathnapura (Kalu Ganga) | 3.21 | 🟢 Normal | -0.009 |  |
| 2026-11-21 09:01:54 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-21 09:00:45 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-11-21 09:02:03 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-11-21 09:01:16 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.021 |  |
| 2026-11-21 08:04:16 | Glencourse (Kelani Ganga) | 9.94 | 🟢 Normal | -0.030 |  |
| 2026-11-21 09:03:29 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.030 |  |
| 2026-11-21 08:05:14 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.032 |  |
| 2026-11-21 08:05:41 | Thawalama (Gin Ganga) | 2.60 | 🟢 Normal | -0.048 |  |
| 2026-11-21 09:02:32 | Thanamalwila (Kirindi Oya) | 2.00 | 🟢 Normal | -0.080 |  |
| 2026-11-21 08:32:16 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.120 |  |
| 2026-11-21 09:01:55 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.172 |  |
| 2026-11-21 09:02:15 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.701 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)