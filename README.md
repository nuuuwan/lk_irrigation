# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_21:03:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,623 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Urawa — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 21:03:28 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-07 21:03:22 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.068 |  |
| 2026-11-07 21:03:16 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:03:09 | Wellawaya (Kirindi Oya) | 3.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-07 21:02:48 | Dunamale (Aththanagalu Oya) | 3.68 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-07 21:02:40 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-11-07 21:02:13 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-11-07 21:01:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-11-07 21:01:53 | Thaldena (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.153 |  |
| 2026-11-07 21:01:26 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-07 21:01:07 | Moraketiya (Walawe Ganga) | 2.45 | 🟢 Normal | 0.500 | 🔺 Rising |
| 2026-11-07 21:00:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:00:29 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 20:06:36 | Urawa (Nilwala Ganga) | 3.81 | 🟡 Alert | 0.277 | 🔺 Rising |
| 2026-11-07 21:02:48 | Dunamale (Aththanagalu Oya) | 3.68 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-07 21:01:07 | Moraketiya (Walawe Ganga) | 2.45 | 🟢 Normal | 0.500 | 🔺 Rising |
| 2026-11-07 20:01:33 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-11-07 20:04:53 | Peradeniya (Mahaweli Ganga) | 3.87 | 🟢 Normal | 0.243 | 🔺 Rising |
| 2026-11-07 20:18:14 | Rathnapura (Kalu Ganga) | 3.02 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 21:03:09 | Wellawaya (Kirindi Oya) | 3.29 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-11-07 21:03:28 | Magura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-07 20:03:32 | Baddegama (Gin Ganga) | 1.95 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-11-07 20:02:10 | Hanwella (Kelani Ganga) | 3.47 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-07 20:07:19 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-11-07 20:04:53 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-07 21:00:29 | Moragaswewa (Deduru Oya) | 1.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-07 20:07:20 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-07 20:15:01 | Norwood (Kelani Ganga) | 1.04 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-07 21:01:26 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-07 20:03:52 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 20:04:11 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 20:06:00 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:00:53 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:14:13 | Giriulla (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:01:14 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:03:52 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:03:07 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-07 21:03:16 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:07:39 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 20:08:38 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.009 |  |
| 2026-11-07 20:03:32 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-07 21:02:13 | Manampitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-11-07 21:02:40 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.022 |  |
| 2026-11-07 20:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.99 | 🟢 Normal | -0.031 |  |
| 2026-11-07 21:01:57 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-11-07 20:08:49 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.061 |  |
| 2026-11-07 21:03:22 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.068 |  |
| 2026-11-07 21:01:53 | Thaldena (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)