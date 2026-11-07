# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_02:24:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 02:24:08 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-11-08 02:22:46 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-08 02:07:48 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | -0.105 |  |
| 2026-11-08 02:06:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 02:06:50 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 02:06:29 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:06:24 | Wellawaya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.076 |  |
| 2026-11-08 02:05:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-11-08 02:05:27 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 02:05:23 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.221 |  |
| 2026-11-08 02:04:48 | Urawa (Nilwala Ganga) | 3.42 | 🟡 Alert | -0.139 |  |
| 2026-11-08 02:03:46 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 02:03:39 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-11-08 02:03:35 | Thaldena (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.051 |  |
| 2026-11-08 02:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | -0.011 |  |
| 2026-11-08 02:03:01 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.152 |  |
| 2026-11-08 02:02:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:44 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-08 02:02:44 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-08 02:02:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:17 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-08 02:02:13 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.050 |  |
| 2026-11-08 02:02:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:05 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:01:40 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 02:01:35 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-08 02:01:30 | Thawalama (Gin Ganga) | 3.54 | 🟢 Normal | -0.043 |  |
| 2026-11-08 02:01:25 | Ellagawa (Kalu Ganga) | 6.77 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-08 02:00:45 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.052 |  |
| 2026-11-08 02:00:23 | Moraketiya (Walawe Ganga) | 4.50 | 🟡 Alert | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 02:24:08 | Panadugama (Nilwala Ganga) | 5.08 | 🟡 Alert | 0.065 | 🔺 Rising |
| 2026-11-08 02:00:23 | Moraketiya (Walawe Ganga) | 4.50 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-08 02:05:27 | Dunamale (Aththanagalu Oya) | 3.78 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 02:04:48 | Urawa (Nilwala Ganga) | 3.42 | 🟡 Alert | -0.139 |  |
| 2026-11-08 02:22:46 | Rathnapura (Kalu Ganga) | 4.49 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-08 00:04:17 | Pitabeddara (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.226 | 🔺 Rising |
| 2026-11-08 01:10:01 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-08 02:02:44 | Giriulla (Maha Oya) | 3.45 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-11-08 02:01:25 | Ellagawa (Kalu Ganga) | 6.77 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-11-08 02:02:44 | Kuda Oya (Kirindi Oya) | 1.82 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-08 02:01:35 | Moragaswewa (Deduru Oya) | 1.79 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-11-08 02:02:17 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-08 02:01:40 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-08 02:06:55 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 02:03:46 | Badalgama (Maha Oya) | 3.86 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-08 01:18:52 | Thalgahagoda (Nilwala Ganga) | 1.01 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-08 02:06:50 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-08 02:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:16:07 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:39 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:02:07 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-11-08 02:06:29 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 01:29:19 | Putupaula (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 02:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.95 | 🟢 Normal | -0.011 |  |
| 2026-11-08 02:05:45 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | -0.019 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 01:09:06 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.028 |  |
| 2026-11-08 02:03:39 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.039 |  |
| 2026-11-08 02:01:30 | Thawalama (Gin Ganga) | 3.54 | 🟢 Normal | -0.043 |  |
| 2026-11-08 02:02:13 | Hanwella (Kelani Ganga) | 3.31 | 🟢 Normal | -0.050 |  |
| 2026-11-08 02:03:35 | Thaldena (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.051 |  |
| 2026-11-08 02:00:45 | Peradeniya (Mahaweli Ganga) | 3.90 | 🟢 Normal | -0.052 |  |
| 2026-11-08 02:06:24 | Wellawaya (Kirindi Oya) | 2.50 | 🟢 Normal | -0.076 |  |
| 2026-11-08 02:07:48 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | -0.105 |  |
| 2026-11-08 02:03:01 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.152 |  |
| 2026-11-08 02:05:23 | Nakkala (Kumbukkan Oya) | 1.76 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)