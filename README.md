# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_05:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:53 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:36 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:32 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 05:02:22 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 05:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:00:57 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.203 |  |
| 2026-09-20 05:00:52 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-20 04:56:57 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 04:34:23 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-20 04:19:39 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-20 04:19:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:17:49 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 05:00:52 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-09-20 04:04:39 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.539 | 🔺 Rising |
| 2026-09-20 04:05:03 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-20 04:05:06 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-20 04:07:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-20 04:02:46 | Hanwella (Kelani Ganga) | 1.76 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-20 04:34:23 | Thawalama (Gin Ganga) | 2.18 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-09-20 04:05:45 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-20 04:04:44 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-20 04:04:26 | Dunamale (Aththanagalu Oya) | 1.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 04:03:32 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 04:10:32 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-20 04:19:39 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-20 04:02:16 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 04:56:57 | Putupaula (Kalu Ganga) | 0.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-20 05:02:22 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 04:17:49 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-20 04:01:58 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-20 04:00:52 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 04:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 05:02:32 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 04:08:13 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 05:02:36 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:01:46 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:02:08 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:55 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:04:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:03:49 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:02:04 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:19:00 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-19 18:01:39 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:11:40 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:01:18 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 04:03:07 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-09-19 18:01:44 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 04:06:38 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.020 |  |
| 2026-09-20 04:13:36 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.027 |  |
| 2026-09-20 05:00:57 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)