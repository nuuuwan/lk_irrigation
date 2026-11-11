# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_01:22:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,369 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Peradeniya — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 01:22:09 | Moraketiya (Walawe Ganga) | 4.12 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-11-12 01:12:41 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.199 |  |
| 2026-11-12 01:12:26 | Katharagama (Menik Ganga) | 1.06 | 🟢 Normal | -0.035 |  |
| 2026-11-12 01:11:24 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2026-11-12 01:08:09 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-11-12 01:07:13 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 01:07:10 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.019 |  |
| 2026-11-12 01:06:58 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-11-12 01:06:27 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-12 01:05:35 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:05:27 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:05:20 | Urawa (Nilwala Ganga) | 3.15 | 🟡 Alert | -0.042 |  |
| 2026-11-12 01:05:03 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-12 01:04:26 | Holombuwa (Kelani Ganga) | 3.28 | 🟡 Alert | -0.118 |  |
| 2026-11-12 01:04:16 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.127 |  |
| 2026-11-12 01:04:11 | Padiyathalawa (Maduru Oya) | 3.30 | 🟢 Normal | -0.290 |  |
| 2026-11-12 01:04:00 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 01:03:40 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:03:31 | Giriulla (Maha Oya) | 3.37 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-11-12 01:03:24 | Magura (Kalu Ganga) | 5.29 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-12 01:03:20 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 01:03:14 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | 0.462 | 🔺 Rising |
| 2026-11-12 01:02:54 | Siyambalanduwa (Heda Oya) | 2.53 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-11-12 01:02:52 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 01:02:44 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 01:02:37 | Glencourse (Kelani Ganga) | 13.67 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-12 01:02:24 | Thaldena (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.133 |  |
| 2026-11-12 01:02:16 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:02:12 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 01:02:04 | Nakkala (Kumbukkan Oya) | 3.10 | 🟢 Normal | -0.379 |  |
| 2026-11-12 01:02:03 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-12 01:01:24 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:00:57 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 01:06:58 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | 0.012 | 🔺 Rising |
| 2026-11-12 01:03:20 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 01:03:14 | Peradeniya (Mahaweli Ganga) | 5.50 | 🟡 Alert | 0.462 | 🔺 Rising |
| 2026-11-12 01:11:24 | Panadugama (Nilwala Ganga) | 5.62 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2026-11-12 01:02:52 | Dunamale (Aththanagalu Oya) | 4.06 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-12 01:03:24 | Magura (Kalu Ganga) | 5.29 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-11-12 01:05:03 | Thawalama (Gin Ganga) | 5.20 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-12 01:22:09 | Moraketiya (Walawe Ganga) | 4.12 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-11-12 00:12:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | 0.000 |  |
| 2026-11-12 01:07:10 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.019 |  |
| 2026-11-12 01:05:20 | Urawa (Nilwala Ganga) | 3.15 | 🟡 Alert | -0.042 |  |
| 2026-11-12 01:04:26 | Holombuwa (Kelani Ganga) | 3.28 | 🟡 Alert | -0.118 |  |
| 2026-11-12 01:03:31 | Giriulla (Maha Oya) | 3.37 | 🟢 Normal | 0.446 | 🔺 Rising |
| 2026-11-12 01:02:54 | Siyambalanduwa (Heda Oya) | 2.53 | 🟢 Normal | 0.323 | 🔺 Rising |
| 2026-11-12 01:02:44 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-11-12 01:08:09 | Pitabeddara (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.308 | 🔺 Rising |
| 2026-11-12 01:02:37 | Glencourse (Kelani Ganga) | 13.67 | 🟢 Normal | 0.268 | 🔺 Rising |
| 2026-11-12 01:02:12 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.221 | 🔺 Rising |
| 2026-11-12 01:06:27 | Badalgama (Maha Oya) | 3.65 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-12 00:11:27 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-12 01:07:13 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-12 00:05:42 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-12 01:02:03 | Moragaswewa (Deduru Oya) | 3.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-12 01:04:00 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:05:27 | Wellawaya (Kirindi Oya) | 3.45 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:01:24 | Ellagawa (Kalu Ganga) | 8.37 | 🟢 Normal | 0.000 |  |
| 2026-11-12 01:05:35 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-12 00:06:25 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-11-12 00:06:10 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-12 01:00:57 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.015 |  |
| 2026-11-12 01:12:26 | Katharagama (Menik Ganga) | 1.06 | 🟢 Normal | -0.035 |  |
| 2026-11-12 01:04:16 | Deraniyagala (Kelani Ganga) | 1.75 | 🟢 Normal | -0.127 |  |
| 2026-11-12 01:02:24 | Thaldena (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.133 |  |
| 2026-11-12 01:12:41 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.199 |  |
| 2026-11-12 01:04:11 | Padiyathalawa (Maduru Oya) | 3.30 | 🟢 Normal | -0.290 |  |
| 2026-11-12 01:02:04 | Nakkala (Kumbukkan Oya) | 3.10 | 🟢 Normal | -0.379 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)