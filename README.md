# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_06:11:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,750 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 06:11:13 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 06:10:26 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-11-10 06:10:14 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.055 |  |
| 2026-11-10 06:07:55 | Hanwella (Kelani Ganga) | 6.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-10 06:07:25 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:06:49 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:06:08 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-10 06:06:00 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | -0.283 |  |
| 2026-11-10 06:05:43 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-10 06:05:42 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-10 06:05:30 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-10 06:04:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-10 06:04:34 | Thanamalwila (Kirindi Oya) | 2.21 | 🟢 Normal | -0.230 |  |
| 2026-11-10 06:04:21 | Moraketiya (Walawe Ganga) | 3.25 | 🟡 Alert | -0.367 |  |
| 2026-11-10 06:04:16 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-10 06:03:51 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-11-10 06:03:41 | Glencourse (Kelani Ganga) | 14.11 | 🟢 Normal | -0.238 |  |
| 2026-11-10 06:03:19 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.379 |  |
| 2026-11-10 06:03:16 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 06:03:07 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.049 |  |
| 2026-11-10 06:02:37 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:02:26 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 06:02:18 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | -0.085 |  |
| 2026-11-10 06:02:07 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 06:02:03 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | -0.017 |  |
| 2026-11-10 06:01:44 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.144 |  |
| 2026-11-10 06:01:39 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-10 06:01:12 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.159 |  |
| 2026-11-10 06:01:10 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-11-10 06:00:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.000 |  |
| 2026-11-10 06:00:44 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-10 06:00:39 | Pitabeddara (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.309 |  |
| 2026-11-10 06:00:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:00:28 | Thawalama (Gin Ganga) | 4.74 | 🟡 Alert | -0.129 |  |
| 2026-11-10 05:47:22 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | 0.091 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 05:47:22 | Panadugama (Nilwala Ganga) | 6.07 | 🟠 Minor Flood | 0.091 | 🔺 Rising |
| 2026-11-10 06:11:13 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-10 06:03:16 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 06:10:26 | Thalgahagoda (Nilwala Ganga) | 1.62 | 🟡 Alert | 0.018 | 🔺 Rising |
| 2026-11-10 06:00:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.40 | 🟡 Alert | 0.000 |  |
| 2026-11-10 06:02:03 | Magura (Kalu Ganga) | 5.17 | 🟡 Alert | -0.017 |  |
| 2026-11-10 06:00:28 | Thawalama (Gin Ganga) | 4.74 | 🟡 Alert | -0.129 |  |
| 2026-11-10 06:04:21 | Moraketiya (Walawe Ganga) | 3.25 | 🟡 Alert | -0.367 |  |
| 2026-11-10 06:01:10 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.321 | 🔺 Rising |
| 2026-11-10 06:00:44 | Moragaswewa (Deduru Oya) | 3.96 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-10 06:05:43 | Badalgama (Maha Oya) | 4.13 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-10 06:05:42 | Urawa (Nilwala Ganga) | 1.53 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-10 06:02:07 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 06:07:55 | Hanwella (Kelani Ganga) | 6.29 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-10 06:06:08 | Weraganthota (Mahaweli Ganga) | -2.25 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-10 06:05:30 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-10 06:02:37 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 04:01:59 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:07:25 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:00:28 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:03:51 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-10 06:01:39 | Manampitiya (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-10 06:02:26 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.011 |  |
| 2026-11-10 06:04:41 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-11-10 06:04:16 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-11-10 06:03:43 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-11-10 06:03:07 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.049 |  |
| 2026-11-10 06:10:14 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.055 |  |
| 2026-11-10 06:02:18 | Rathnapura (Kalu Ganga) | 5.15 | 🟢 Normal | -0.085 |  |
| 2026-11-10 06:01:44 | Giriulla (Maha Oya) | 3.14 | 🟢 Normal | -0.144 |  |
| 2026-11-10 06:01:12 | Wellawaya (Kirindi Oya) | 1.82 | 🟢 Normal | -0.159 |  |
| 2026-11-10 06:04:34 | Thanamalwila (Kirindi Oya) | 2.21 | 🟢 Normal | -0.230 |  |
| 2026-11-10 06:03:41 | Glencourse (Kelani Ganga) | 14.11 | 🟢 Normal | -0.238 |  |
| 2026-11-10 06:06:00 | Peradeniya (Mahaweli Ganga) | 3.99 | 🟢 Normal | -0.283 |  |
| 2026-11-10 06:00:39 | Pitabeddara (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.309 |  |
| 2026-11-10 06:03:19 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.379 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)