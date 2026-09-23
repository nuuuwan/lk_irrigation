# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_22:19:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,129 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 22:19:29 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:12:49 | Baddegama (Gin Ganga) | 3.66 | 🟡 Alert | -0.009 |  |
| 2026-09-23 22:12:21 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-23 22:10:52 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-23 22:09:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:07:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 22:07:45 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-23 22:07:19 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-23 22:06:29 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-09-23 22:06:10 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-09-23 22:06:01 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-09-23 22:05:48 | Nawalapitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.094 |  |
| 2026-09-23 22:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-23 22:04:43 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 22:04:36 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:04:14 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-09-23 22:04:07 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-09-23 22:03:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:03:39 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-23 22:03:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 22:03:17 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 22:03:01 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-09-23 22:02:46 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-23 22:02:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:02:25 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -0.020 |  |
| 2026-09-23 22:02:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-09-23 22:02:11 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:01:40 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-23 22:01:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-23 22:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:01:11 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-23 22:00:27 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 21:58:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 22:05:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | -0.009 |  |
| 2026-09-23 22:12:49 | Baddegama (Gin Ganga) | 3.66 | 🟡 Alert | -0.009 |  |
| 2026-09-23 22:06:29 | Thawalama (Gin Ganga) | 3.38 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-09-23 22:06:10 | Urawa (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-09-23 22:07:19 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-23 22:01:40 | Peradeniya (Mahaweli Ganga) | 3.88 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-23 22:07:45 | Pitabeddara (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-23 22:03:39 | Glencourse (Kelani Ganga) | 12.63 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-23 22:10:52 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-09-23 22:12:21 | Rathnapura (Kalu Ganga) | 4.27 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-23 22:04:43 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 22:07:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-23 22:01:21 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-09-23 22:01:11 | Magura (Kalu Ganga) | 3.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-23 22:03:17 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 22:03:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-23 22:00:27 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 21:58:56 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 21:02:38 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:19:29 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:03:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:02:27 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:09:48 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:04:36 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:02:11 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 22:02:36 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 22:03:01 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | -0.010 |  |
| 2026-09-23 22:06:01 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-09-23 22:02:23 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-23 22:02:46 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-23 22:02:25 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | -0.020 |  |
| 2026-09-23 22:04:07 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | -0.021 |  |
| 2026-09-23 21:05:48 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.030 |  |
| 2026-09-23 22:04:14 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | -0.050 |  |
| 2026-09-23 22:05:48 | Nawalapitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.094 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)