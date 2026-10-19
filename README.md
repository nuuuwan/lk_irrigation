# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_02:08:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,667 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 02:08:11 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-20 02:08:07 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:07:23 | Panadugama (Nilwala Ganga) | 4.96 | 🟢 Normal | -0.027 |  |
| 2026-10-20 02:07:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:06:17 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:05:27 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:04:42 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.024 |  |
| 2026-10-20 02:04:39 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-10-20 02:04:29 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:04:08 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:03:28 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.116 |  |
| 2026-10-20 02:03:21 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-20 02:03:21 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.106 |  |
| 2026-10-20 02:02:50 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.269 |  |
| 2026-10-20 02:02:28 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-20 02:02:04 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 02:02:02 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.059 |  |
| 2026-10-20 02:01:55 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:42 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:01:31 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:31 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-10-20 02:01:19 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:04 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.703 |  |
| 2026-10-20 02:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:00:37 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:40:51 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-10-20 01:37:59 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-20 01:34:36 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | -0.703 |  |
| 2026-10-20 01:27:26 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:24:11 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:22:19 | Panadugama (Nilwala Ganga) | 4.98 | 🟢 Normal | -0.027 |  |
| 2026-10-20 01:21:57 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.116 |  |
| 2026-10-20 01:21:39 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 02:01:04 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.703 |  |
| 2026-10-20 02:02:28 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-20 01:02:22 | Glencourse (Kelani Ganga) | 11.05 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-20 02:02:04 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 01:37:59 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-20 02:05:27 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:00:37 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:02:14 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:04:08 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:06:02 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-20 00:06:43 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:17:18 | Pitabeddara (Nilwala Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:06:17 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:19 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:07:01 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:08:07 | Badalgama (Maha Oya) | 2.63 | 🟢 Normal | 0.000 |  |
| 2026-10-19 18:03:27 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-20 02:01:55 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-20 01:21:39 | Norwood (Kelani Ganga) | 1.14 | 🟢 Normal | -0.009 |  |
| 2026-10-20 02:08:11 | Holombuwa (Kelani Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-10-20 01:27:26 | Urawa (Nilwala Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:04:29 | Thawalama (Gin Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:00:45 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-20 02:01:42 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-20 01:13:50 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.017 |  |
| 2026-10-20 02:04:39 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.019 |  |
| 2026-10-20 01:40:51 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.021 |  |
| 2026-10-20 02:01:31 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-10-20 02:04:42 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.024 |  |
| 2026-10-20 02:07:23 | Panadugama (Nilwala Ganga) | 4.96 | 🟢 Normal | -0.027 |  |
| 2026-10-20 00:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.40 | 🟢 Normal | -0.028 |  |
| 2026-10-20 02:03:21 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-10-20 00:06:26 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | -0.032 |  |
| 2026-10-20 01:14:52 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.039 |  |
| 2026-10-20 02:02:02 | Ellagawa (Kalu Ganga) | 6.35 | 🟢 Normal | -0.059 |  |
| 2026-10-19 18:01:22 | Weraganthota (Mahaweli Ganga) | -3.13 | 🟢 Normal | -0.070 |  |
| 2026-10-20 02:03:21 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.106 |  |
| 2026-10-20 02:03:28 | Deraniyagala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.116 |  |
| 2026-10-20 02:02:50 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.269 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)