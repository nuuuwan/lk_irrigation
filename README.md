# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_11:19:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,163 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 11:19:13 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:19:08 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:13:50 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:13:25 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.036 |  |
| 2026-11-08 11:11:45 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.051 |  |
| 2026-11-08 11:11:12 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.103 |  |
| 2026-11-08 11:10:48 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.095 |  |
| 2026-11-08 11:10:05 | Baddegama (Gin Ganga) | 3.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-08 11:08:50 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 11:08:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 11:07:17 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.048 |  |
| 2026-11-08 11:06:58 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:06:26 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.028 |  |
| 2026-11-08 11:06:05 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-08 11:05:23 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:05:13 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | -0.085 |  |
| 2026-11-08 11:04:28 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.048 |  |
| 2026-11-08 11:04:27 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | 0.000 |  |
| 2026-11-08 11:04:09 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-11-08 11:03:38 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.029 |  |
| 2026-11-08 11:03:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.061 |  |
| 2026-11-08 11:02:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:02:31 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:02:15 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.092 |  |
| 2026-11-08 11:02:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:02:08 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | -0.181 |  |
| 2026-11-08 11:02:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-08 11:01:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.107 |  |
| 2026-11-08 11:01:54 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-08 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-08 11:01:46 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:24 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 1.140 | 🔺 Rising |
| 2026-11-08 11:01:19 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:01:15 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-08 11:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 11:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-08 11:00:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 11:08:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 11:04:27 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | 0.000 |  |
| 2026-11-08 11:13:25 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.036 |  |
| 2026-11-08 11:11:45 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.051 |  |
| 2026-11-08 11:01:24 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 1.140 | 🔺 Rising |
| 2026-11-08 11:01:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-08 11:01:54 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-08 10:05:03 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 11:06:05 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-11-08 11:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 11:10:05 | Baddegama (Gin Ganga) | 3.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-08 11:08:50 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 11:19:13 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:13:50 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:19:08 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:02:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:01:19 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-08 11:01:15 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-08 11:05:23 | Putupaula (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:06:58 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:02:31 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:00:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:06:26 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.028 |  |
| 2026-11-08 11:03:38 | Hanwella (Kelani Ganga) | 3.12 | 🟢 Normal | -0.029 |  |
| 2026-11-08 11:02:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:46 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:02:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:04:28 | Glencourse (Kelani Ganga) | 10.79 | 🟢 Normal | -0.048 |  |
| 2026-11-08 11:07:17 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.048 |  |
| 2026-11-08 11:04:09 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-11-08 11:03:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.061 |  |
| 2026-11-08 11:05:13 | Thawalama (Gin Ganga) | 2.62 | 🟢 Normal | -0.085 |  |
| 2026-11-08 11:02:15 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.092 |  |
| 2026-11-08 11:10:48 | Magura (Kalu Ganga) | 3.88 | 🟢 Normal | -0.095 |  |
| 2026-11-08 11:11:12 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.103 |  |
| 2026-11-08 11:01:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.107 |  |
| 2026-11-08 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-08 11:02:08 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)