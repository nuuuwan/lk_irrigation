# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_11:05:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,202 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 11:05:11 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-18 11:04:28 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:04:27 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 11:03:52 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 11:03:51 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:03:48 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-18 11:03:40 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-18 11:03:29 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.067 |  |
| 2026-10-18 11:02:54 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:02:49 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.081 |  |
| 2026-10-18 11:02:47 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:02:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.140 |  |
| 2026-10-18 11:02:26 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.051 |  |
| 2026-10-18 11:02:24 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:02:09 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.079 |  |
| 2026-10-18 11:02:08 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.023 |  |
| 2026-10-18 11:02:04 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-10-18 11:01:56 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 11:01:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-18 11:01:41 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 11:01:39 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.130 |  |
| 2026-10-18 11:01:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:01:33 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-18 11:01:24 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 11:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-10-18 11:00:42 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-18 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-18 10:38:41 | Moragaswewa (Deduru Oya) | 1.13 | 🟢 Normal | 0.082 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 11:03:52 | Thalgahagoda (Nilwala Ganga) | 2.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 11:02:08 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.023 |  |
| 2026-10-18 10:14:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.19 | 🟡 Alert | -0.025 |  |
| 2026-10-18 11:03:48 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-18 11:00:42 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-18 11:04:27 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-18 11:01:43 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-18 10:02:12 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 11:01:56 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-18 11:01:24 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 11:01:33 | Horowpothana (Yan Oya) | 3.10 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-18 10:05:49 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 11:02:47 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:01:34 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:04:28 | Ellagawa (Kalu Ganga) | 7.74 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:02:54 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:03:51 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 11:02:24 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-18 10:18:11 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.008 |  |
| 2026-10-18 10:07:36 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-10-18 10:03:56 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-10-18 11:01:41 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-18 11:05:11 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-18 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.011 |  |
| 2026-10-18 10:00:47 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.018 |  |
| 2026-10-18 11:03:40 | Putupaula (Kalu Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-18 10:06:05 | Holombuwa (Kelani Ganga) | 1.23 | 🟢 Normal | -0.021 |  |
| 2026-10-18 11:02:04 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-10-18 10:06:18 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.046 |  |
| 2026-10-18 11:02:26 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.051 |  |
| 2026-10-18 11:00:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.061 |  |
| 2026-10-18 11:03:29 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.067 |  |
| 2026-10-18 11:02:09 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.079 |  |
| 2026-10-18 11:02:49 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.081 |  |
| 2026-10-18 10:06:06 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | -0.092 |  |
| 2026-10-18 10:02:27 | Thawalama (Gin Ganga) | 2.99 | 🟢 Normal | -0.119 |  |
| 2026-10-18 11:01:39 | Rathnapura (Kalu Ganga) | 3.58 | 🟢 Normal | -0.130 |  |
| 2026-10-18 11:02:35 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.140 |  |
| 2026-10-18 10:02:22 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)