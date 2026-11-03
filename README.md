# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_02:03:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,196 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 02:03:44 | Giriulla (Maha Oya) | 3.72 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-04 02:03:39 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-04 02:03:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-11-04 02:03:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:02:53 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:02:21 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-04 02:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:02:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:02:17 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-04 02:01:58 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-04 02:01:49 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:01:44 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:01:37 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-11-04 02:01:13 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-11-04 02:01:10 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:01:09 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:00:30 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.080 |  |
| 2026-11-04 01:37:46 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-04 01:25:44 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 01:06:42 | Moraketiya (Walawe Ganga) | 3.25 | 🟡 Alert | -0.010 |  |
| 2026-11-04 01:10:29 | Urawa (Nilwala Ganga) | 2.52 | 🟡 Alert | -0.553 |  |
| 2026-11-04 00:03:29 | Pitabeddara (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.394 | 🔺 Rising |
| 2026-11-04 02:02:17 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | 0.373 | 🔺 Rising |
| 2026-11-04 01:05:19 | Dunamale (Aththanagalu Oya) | 2.45 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-11-04 01:14:49 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-04 01:06:59 | Magura (Kalu Ganga) | 3.45 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-11-04 01:13:45 | Thawalama (Gin Ganga) | 3.44 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-04 02:01:58 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-11-04 02:03:44 | Giriulla (Maha Oya) | 3.72 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-04 02:03:39 | Hanwella (Kelani Ganga) | 3.01 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-11-04 01:03:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-04 01:37:46 | Horowpothana (Yan Oya) | 3.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-04 01:20:29 | Panadugama (Nilwala Ganga) | 4.26 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-04 02:03:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:08:32 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-04 01:25:44 | Glencourse (Kelani Ganga) | 11.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-04 00:16:27 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:01:49 | Thalgahagoda (Nilwala Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-04 02:01:09 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:01:10 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:03:06 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:01:44 | Moragaswewa (Deduru Oya) | 4.17 | 🟢 Normal | -0.010 |  |
| 2026-11-04 02:01:13 | Nakkala (Kumbukkan Oya) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-11-04 02:01:37 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.021 |  |
| 2026-11-04 01:21:55 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.025 |  |
| 2026-11-04 02:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.029 |  |
| 2026-11-04 01:04:28 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.051 |  |
| 2026-11-04 02:02:21 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.066 |  |
| 2026-11-04 01:02:46 | Manampitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.070 |  |
| 2026-11-04 02:00:30 | Peradeniya (Mahaweli Ganga) | 3.48 | 🟢 Normal | -0.080 |  |
| 2026-11-04 01:14:02 | Holombuwa (Kelani Ganga) | 1.57 | 🟢 Normal | -0.112 |  |
| 2026-11-04 00:02:14 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.141 |  |
| 2026-11-04 01:02:29 | Siyambalanduwa (Heda Oya) | 0.64 | 🟢 Normal | -28.000 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)