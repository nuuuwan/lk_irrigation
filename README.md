# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_00:03:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 00:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-05 00:02:58 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-05 00:02:22 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.070 |  |
| 2026-11-05 00:02:18 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-05 00:02:07 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-11-05 00:02:01 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 00:02:01 | Moragaswewa (Deduru Oya) | 4.06 | 🟢 Normal | -0.050 |  |
| 2026-11-05 00:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:01:42 | Kuda Oya (Kirindi Oya) | 4.26 | 🟢 Normal | 3.014 | 🔺 Rising |
| 2026-11-05 00:01:21 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | -0.023 |  |
| 2026-11-05 00:01:09 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-11-05 00:00:49 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:26 | Moraketiya (Walawe Ganga) | 4.04 | 🟡 Alert | 1.978 | 🔺 Rising |
| 2026-11-05 00:00:24 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:32:22 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.007 |  |
| 2026-11-04 23:28:15 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 00:00:26 | Moraketiya (Walawe Ganga) | 4.04 | 🟡 Alert | 1.978 | 🔺 Rising |
| 2026-11-04 23:05:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-05 00:01:42 | Kuda Oya (Kirindi Oya) | 4.26 | 🟢 Normal | 3.014 | 🔺 Rising |
| 2026-11-04 23:08:52 | Thanamalwila (Kirindi Oya) | 3.21 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-11-05 00:02:58 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-05 00:02:18 | Giriulla (Maha Oya) | 2.98 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-11-04 23:08:43 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-04 23:04:44 | Urawa (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-04 23:02:55 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-11-04 23:02:13 | Glencourse (Kelani Ganga) | 10.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-05 00:02:01 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-04 22:02:45 | Pitabeddara (Nilwala Ganga) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-04 23:08:01 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 23:02:43 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 00:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:28:15 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:49 | Padiyathalawa (Maduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:40 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 22:02:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:15:00 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:00:24 | Thalgahagoda (Nilwala Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-04 23:32:22 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | -0.007 |  |
| 2026-11-04 23:01:49 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:02:37 | Peradeniya (Mahaweli Ganga) | 3.04 | 🟢 Normal | -0.010 |  |
| 2026-11-04 23:05:10 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.011 |  |
| 2026-11-04 23:01:34 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-11-05 00:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-11-04 23:08:54 | Baddegama (Gin Ganga) | 2.17 | 🟢 Normal | -0.021 |  |
| 2026-11-05 00:01:21 | Holombuwa (Kelani Ganga) | 1.39 | 🟢 Normal | -0.023 |  |
| 2026-11-05 00:01:09 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.023 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 23:03:12 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 00:02:07 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.041 |  |
| 2026-11-04 23:07:04 | Rathnapura (Kalu Ganga) | 2.28 | 🟢 Normal | -0.046 |  |
| 2026-11-04 22:00:22 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.050 |  |
| 2026-11-05 00:02:01 | Moragaswewa (Deduru Oya) | 4.06 | 🟢 Normal | -0.050 |  |
| 2026-11-05 00:02:22 | Ellagawa (Kalu Ganga) | 6.40 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)