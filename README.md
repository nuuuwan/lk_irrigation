# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_12:05:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,191 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 12:05:23 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:04:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:04:38 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 12:04:35 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:04:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-08 12:04:29 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.050 |  |
| 2026-11-08 12:04:23 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.079 |  |
| 2026-11-08 12:03:45 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.204 |  |
| 2026-11-08 12:03:38 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.156 |  |
| 2026-11-08 12:03:32 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.082 |  |
| 2026-11-08 12:03:16 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 12:03:11 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-08 12:02:59 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.069 |  |
| 2026-11-08 12:02:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:02:40 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-08 12:02:39 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-08 12:02:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 12:02:15 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-08 12:02:14 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:01:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 12:01:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.201 |  |
| 2026-11-08 12:01:36 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:25 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.201 |  |
| 2026-11-08 12:01:15 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:00:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:00:44 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:48:26 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | 0.017 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 11:08:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.44 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-08 11:04:27 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | 0.000 |  |
| 2026-11-08 11:13:25 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | -0.036 |  |
| 2026-11-08 11:11:45 | Panadugama (Nilwala Ganga) | 5.93 | 🟡 Alert | -0.051 |  |
| 2026-11-08 12:02:40 | Moragaswewa (Deduru Oya) | 3.08 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-11-08 12:04:35 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-08 12:03:16 | Putupaula (Kalu Ganga) | 1.63 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 12:02:39 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-08 11:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 11:10:05 | Baddegama (Gin Ganga) | 3.04 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-08 12:02:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 11:48:26 | Ellagawa (Kalu Ganga) | 7.39 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-08 12:04:38 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 12:01:49 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 12:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:36 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:00:58 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:01:15 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:19:08 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:02:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:04:50 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:00:44 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 12:04:35 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:02:14 | Kuda Oya (Kirindi Oya) | 1.91 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:05:23 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-08 12:02:15 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:06:58 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-11-08 12:03:11 | Hanwella (Kelani Ganga) | 3.08 | 🟢 Normal | -0.040 |  |
| 2026-11-08 11:07:17 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | -0.048 |  |
| 2026-11-08 12:04:29 | Glencourse (Kelani Ganga) | 10.74 | 🟢 Normal | -0.050 |  |
| 2026-11-08 11:04:09 | Thanamalwila (Kirindi Oya) | 1.90 | 🟢 Normal | -0.051 |  |
| 2026-11-08 12:02:59 | Giriulla (Maha Oya) | 2.70 | 🟢 Normal | -0.069 |  |
| 2026-11-08 12:04:23 | Badalgama (Maha Oya) | 3.93 | 🟢 Normal | -0.079 |  |
| 2026-11-08 12:03:32 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.082 |  |
| 2026-11-08 11:11:12 | Pitabeddara (Nilwala Ganga) | 2.90 | 🟢 Normal | -0.103 |  |
| 2026-11-08 12:03:38 | Rathnapura (Kalu Ganga) | 4.40 | 🟢 Normal | -0.156 |  |
| 2026-11-08 12:01:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | -0.201 |  |
| 2026-11-08 12:01:25 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | -0.201 |  |
| 2026-11-08 12:03:45 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)