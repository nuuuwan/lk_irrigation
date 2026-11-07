# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_01:29:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,784 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 01:29:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:18:52 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 01:16:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:11:31 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-08 01:10:01 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-08 01:09:13 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:09:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2026-11-08 01:07:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-08 01:06:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2026-11-08 01:06:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | -0.009 |  |
| 2026-11-08 01:05:34 | Thawalama (Gin Ganga) | 3.58 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-08 01:05:08 | Thaldena (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.061 |  |
| 2026-11-08 01:04:54 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | -0.099 |  |
| 2026-11-08 01:04:52 | Rathnapura (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:03:50 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 01:02:52 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:02:45 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-08 01:02:36 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:02:28 | Rathnapura (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:19 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:13 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.070 |  |
| 2026-11-08 01:02:10 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:08 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.169 |  |
| 2026-11-08 01:01:45 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.045 |  |
| 2026-11-08 01:01:36 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-08 01:01:31 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-08 01:01:29 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-08 01:01:23 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.039 |  |
| 2026-11-08 01:00:28 | Panadugama (Nilwala Ganga) | 4.99 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-08 01:00:19 | Nakkala (Kumbukkan Oya) | 2.00 | 🟢 Normal | -0.157 |  |
| 2026-11-08 01:00:13 | Moraketiya (Walawe Ganga) | 4.45 | 🟡 Alert | 0.101 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 01:00:13 | Moraketiya (Walawe Ganga) | 4.45 | 🟡 Alert | 0.101 | 🔺 Rising |
| 2026-11-08 01:01:29 | Dunamale (Aththanagalu Oya) | 3.77 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-08 00:03:32 | Urawa (Nilwala Ganga) | 3.70 | 🟡 Alert | -0.101 |  |
| 2026-11-08 00:04:17 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-08 01:11:31 | Giriulla (Maha Oya) | 3.30 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-11-08 01:10:01 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-08 01:01:31 | Ellagawa (Kalu Ganga) | 6.61 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-11-08 01:00:28 | Panadugama (Nilwala Ganga) | 4.99 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-08 01:01:36 | Moragaswewa (Deduru Oya) | 1.67 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-08 00:04:10 | Baddegama (Gin Ganga) | 2.35 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 01:05:34 | Thawalama (Gin Ganga) | 3.58 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-08 01:03:50 | Badalgama (Maha Oya) | 3.80 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-11-08 01:07:35 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-08 01:18:52 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 00:03:19 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:16:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:10 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:08 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:29:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:09:13 | Holombuwa (Kelani Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:04:52 | Rathnapura (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:02:19 | Kuda Oya (Kirindi Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:06:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.96 | 🟢 Normal | -0.009 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 01:02:45 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:02:36 | Manampitiya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:02:52 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:09:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2026-11-08 01:01:23 | Glencourse (Kelani Ganga) | 10.75 | 🟢 Normal | -0.039 |  |
| 2026-11-08 01:01:45 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.045 |  |
| 2026-11-08 01:05:08 | Thaldena (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.061 |  |
| 2026-11-08 01:06:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.067 |  |
| 2026-11-08 01:02:13 | Hanwella (Kelani Ganga) | 3.36 | 🟢 Normal | -0.070 |  |
| 2026-11-08 01:04:54 | Thanamalwila (Kirindi Oya) | 2.89 | 🟢 Normal | -0.099 |  |
| 2026-11-08 00:08:20 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.139 |  |
| 2026-11-08 01:00:19 | Nakkala (Kumbukkan Oya) | 2.00 | 🟢 Normal | -0.157 |  |
| 2026-11-08 01:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.169 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)