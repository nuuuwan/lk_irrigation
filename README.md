# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_11:36:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,913 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 11:36:24 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.007 |  |
| 2026-11-28 11:24:37 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.015 |  |
| 2026-11-28 11:11:56 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.111 |  |
| 2026-11-28 11:09:13 | Moragaswewa (Deduru Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-28 11:07:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:07:19 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |
| 2026-11-28 11:07:16 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-11-28 11:07:04 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-28 11:06:58 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-11-28 11:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-28 11:06:01 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.088 |  |
| 2026-11-28 11:05:54 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.097 |  |
| 2026-11-28 11:05:21 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.077 |  |
| 2026-11-28 11:05:07 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -14.400 |  |
| 2026-11-28 11:04:42 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -14.400 |  |
| 2026-11-28 11:04:38 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | -0.028 |  |
| 2026-11-28 11:04:28 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-11-28 11:04:27 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.070 |  |
| 2026-11-28 11:04:00 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | -0.040 |  |
| 2026-11-28 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-11-28 11:03:27 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:03:20 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:02:59 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-28 11:02:56 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.020 |  |
| 2026-11-28 11:02:49 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.227 |  |
| 2026-11-28 11:02:45 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.100 |  |
| 2026-11-28 11:02:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | -0.010 |  |
| 2026-11-28 11:02:22 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-28 11:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-28 11:02:04 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:01 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:01:51 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-28 11:01:50 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.176 |  |
| 2026-11-28 11:01:29 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 11:01:10 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-28 11:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 11:00:11 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 11:01:29 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | -0.010 |  |
| 2026-11-28 11:02:56 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.020 |  |
| 2026-11-28 11:05:21 | Panadugama (Nilwala Ganga) | 5.35 | 🟡 Alert | -0.077 |  |
| 2026-11-28 11:06:15 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-11-28 11:02:59 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-28 11:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 11:02:01 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:07:47 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:00:11 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:04 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:36:24 | Horowpothana (Yan Oya) | 2.36 | 🟢 Normal | -0.007 |  |
| 2026-11-28 11:03:20 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:03:27 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:50 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:07:16 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-11-28 11:07:04 | Norwood (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-11-28 11:24:37 | Ellagawa (Kalu Ganga) | 7.18 | 🟢 Normal | -0.015 |  |
| 2026-11-28 11:07:19 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |
| 2026-11-28 11:09:13 | Moragaswewa (Deduru Oya) | 2.26 | 🟢 Normal | -0.020 |  |
| 2026-11-28 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-11-28 11:04:38 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | -0.028 |  |
| 2026-11-28 11:04:28 | Putupaula (Kalu Ganga) | 1.67 | 🟢 Normal | -0.029 |  |
| 2026-11-28 11:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-28 11:01:10 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-28 11:06:58 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.039 |  |
| 2026-11-28 11:02:22 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-28 11:04:00 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | -0.040 |  |
| 2026-11-28 11:01:51 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-28 11:04:27 | Rathnapura (Kalu Ganga) | 2.38 | 🟢 Normal | -0.070 |  |
| 2026-11-28 11:06:01 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.088 |  |
| 2026-11-28 11:05:54 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.097 |  |
| 2026-11-28 11:02:45 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.100 |  |
| 2026-11-28 11:11:56 | Magura (Kalu Ganga) | 3.46 | 🟢 Normal | -0.111 |  |
| 2026-11-28 11:01:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.176 |  |
| 2026-11-28 11:02:49 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.227 |  |
| 2026-11-28 11:05:07 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -14.400 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)