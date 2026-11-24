# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_01:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,887 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 01:02:52 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-25 01:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-25 01:02:19 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-25 01:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.095 |  |
| 2026-11-25 01:01:44 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 01:01:38 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:01:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:01:30 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:01:04 | Siyambalanduwa (Heda Oya) | 2.83 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-25 01:01:02 | Peradeniya (Mahaweli Ganga) | 4.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 01:00:26 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.080 |  |
| 2026-11-25 00:44:51 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 00:20:10 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 01:02:52 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-25 00:00:55 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.000 |  |
| 2026-11-25 00:02:32 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | 0.531 | 🔺 Rising |
| 2026-11-25 00:05:03 | Thaldena (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-11-25 00:02:41 | Hanwella (Kelani Ganga) | 3.83 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-11-25 00:05:42 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-25 00:00:38 | Magura (Kalu Ganga) | 3.70 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-11-25 01:01:04 | Siyambalanduwa (Heda Oya) | 2.83 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-11-25 00:04:57 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-25 00:10:27 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-25 00:14:29 | Ellagawa (Kalu Ganga) | 6.06 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-25 00:05:24 | Baddegama (Gin Ganga) | 2.21 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-25 01:02:19 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-25 00:03:12 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-25 00:09:35 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-25 01:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-25 00:03:15 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-25 00:03:14 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-25 00:44:51 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 01:01:02 | Peradeniya (Mahaweli Ganga) | 4.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 01:01:44 | Kuda Oya (Kirindi Oya) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 01:01:30 | Moragaswewa (Deduru Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:01:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-25 01:01:38 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-25 00:02:37 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 00:03:58 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.030 |  |
| 2026-11-25 00:03:13 | Thawalama (Gin Ganga) | 2.64 | 🟢 Normal | -0.063 |  |
| 2026-11-25 00:05:40 | Glencourse (Kelani Ganga) | 12.60 | 🟢 Normal | -0.080 |  |
| 2026-11-25 01:00:26 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.080 |  |
| 2026-11-25 00:02:50 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-11-25 01:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.095 |  |
| 2026-11-25 00:05:19 | Holombuwa (Kelani Ganga) | 1.56 | 🟢 Normal | -0.300 |  |
| 2026-11-24 22:30:21 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -1.256 |  |
| 2026-11-25 00:10:50 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -1.849 |  |
| 2026-11-25 00:04:27 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | -30.857 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)