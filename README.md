# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_09:12:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,833 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 09:12:12 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:09:45 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:09:29 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-11-28 09:08:49 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:08:12 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.050 |  |
| 2026-11-28 09:07:50 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.103 |  |
| 2026-11-28 09:07:11 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:06:56 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:06:36 | Badalgama (Maha Oya) | 4.06 | 🟢 Normal | -0.065 |  |
| 2026-11-28 09:06:30 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:06:08 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.099 |  |
| 2026-11-28 09:05:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-11-28 09:05:03 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:04:40 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.215 |  |
| 2026-11-28 09:04:21 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.053 |  |
| 2026-11-28 09:04:09 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-28 09:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.084 |  |
| 2026-11-28 09:04:00 | Moraketiya (Walawe Ganga) | 3.18 | 🟡 Alert | -0.021 |  |
| 2026-11-28 09:03:45 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:03:25 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:03:20 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.024 |  |
| 2026-11-28 09:02:42 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.060 |  |
| 2026-11-28 09:02:39 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.082 |  |
| 2026-11-28 09:02:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.113 |  |
| 2026-11-28 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:02:26 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 09:02:17 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 09:02:11 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 09:02:10 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.032 |  |
| 2026-11-28 09:02:06 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 09:01:41 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.162 |  |
| 2026-11-28 09:01:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 09:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-28 09:02:11 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 09:04:00 | Moraketiya (Walawe Ganga) | 3.18 | 🟡 Alert | -0.021 |  |
| 2026-11-28 09:04:21 | Panadugama (Nilwala Ganga) | 5.48 | 🟡 Alert | -0.053 |  |
| 2026-11-28 07:00:16 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-28 09:00:25 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 09:03:45 | Wellawaya (Kirindi Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:00:34 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:06:56 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:12:12 | Pitabeddara (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:04:09 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:07:11 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-28 09:09:29 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-11-28 09:05:03 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:06:30 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:08:49 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:11 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:01:39 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-11-28 09:02:26 | Moragaswewa (Deduru Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-11-28 09:02:06 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 09:03:00 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.024 |  |
| 2026-11-28 09:02:17 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-11-28 09:03:20 | Putupaula (Kalu Ganga) | 1.73 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:00:20 | Kuda Oya (Kirindi Oya) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-11-28 09:02:10 | Giriulla (Maha Oya) | 2.93 | 🟢 Normal | -0.032 |  |
| 2026-11-28 09:08:12 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.050 |  |
| 2026-11-28 09:00:11 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.053 |  |
| 2026-11-28 09:05:49 | Urawa (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.053 |  |
| 2026-11-28 09:02:42 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.060 |  |
| 2026-11-28 09:06:36 | Badalgama (Maha Oya) | 4.06 | 🟢 Normal | -0.065 |  |
| 2026-11-28 09:02:39 | Hanwella (Kelani Ganga) | 4.00 | 🟢 Normal | -0.082 |  |
| 2026-11-28 09:04:03 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.084 |  |
| 2026-11-28 09:06:08 | Magura (Kalu Ganga) | 3.69 | 🟢 Normal | -0.099 |  |
| 2026-11-28 09:07:50 | Rathnapura (Kalu Ganga) | 2.55 | 🟢 Normal | -0.103 |  |
| 2026-11-28 09:02:30 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.113 |  |
| 2026-11-28 09:01:41 | Glencourse (Kelani Ganga) | 11.67 | 🟢 Normal | -0.162 |  |
| 2026-11-28 09:04:40 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)