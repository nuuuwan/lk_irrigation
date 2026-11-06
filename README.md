# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_01:23:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **308,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 01:23:08 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-07 01:18:54 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-07 01:11:30 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.009 |  |
| 2026-11-07 01:10:04 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-07 01:09:20 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 01:09:00 | Holombuwa (Kelani Ganga) | 3.32 | 🟡 Alert | -0.562 |  |
| 2026-11-07 01:07:35 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.062 |  |
| 2026-11-07 01:06:26 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.171 | 🔺 Rising |
| 2026-11-07 01:06:13 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-07 01:05:44 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 01:04:16 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 01:04:10 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-11-07 01:04:09 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-07 01:04:06 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 01:03:58 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:03:12 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-07 01:02:44 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.070 |  |
| 2026-11-07 01:02:44 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-11-07 01:02:36 | Giriulla (Maha Oya) | 3.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 01:02:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 01:02:24 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-07 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.103 |  |
| 2026-11-07 01:00:35 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:00:35 | Glencourse (Kelani Ganga) | 12.54 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-11-07 01:00:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 01:06:26 | Dunamale (Aththanagalu Oya) | 3.58 | 🟡 Alert | 0.171 | 🔺 Rising |
| 2026-11-07 01:01:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.28 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-11-07 01:09:00 | Holombuwa (Kelani Ganga) | 3.32 | 🟡 Alert | -0.562 |  |
| 2026-11-07 01:00:35 | Glencourse (Kelani Ganga) | 12.54 | 🟢 Normal | 0.458 | 🔺 Rising |
| 2026-11-07 01:06:13 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | 0.301 | 🔺 Rising |
| 2026-11-07 00:02:38 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-11-07 01:04:10 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.281 | 🔺 Rising |
| 2026-11-07 01:03:12 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-11-06 22:09:55 | Magura (Kalu Ganga) | 2.49 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-07 01:10:04 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 01:05:44 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-07 01:02:36 | Giriulla (Maha Oya) | 3.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-07 01:04:06 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 01:04:16 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-07 00:03:36 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 01:18:54 | Kuda Oya (Kirindi Oya) | 1.69 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-11-07 01:09:20 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 00:02:33 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:24 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 00:02:13 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:02:36 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:00:17 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:03:58 | Thalgahagoda (Nilwala Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-11-07 01:11:30 | Peradeniya (Mahaweli Ganga) | 4.15 | 🟢 Normal | -0.009 |  |
| 2026-11-07 01:02:23 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-07 00:03:48 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:00:35 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:07 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-11-07 01:02:31 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.013 |  |
| 2026-11-07 01:04:09 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-11-07 01:23:08 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2026-11-07 01:02:44 | Moragaswewa (Deduru Oya) | 1.85 | 🟢 Normal | -0.059 |  |
| 2026-11-07 01:07:35 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.062 |  |
| 2026-11-07 01:02:44 | Thawalama (Gin Ganga) | 2.47 | 🟢 Normal | -0.070 |  |
| 2026-11-07 01:04:52 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.077 |  |
| 2026-11-07 01:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)