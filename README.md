# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_02:03:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,104 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 02:03:03 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.055 |  |
| 2026-11-05 02:03:00 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.022 |  |
| 2026-11-05 02:02:51 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.029 |  |
| 2026-11-05 02:02:20 | Giriulla (Maha Oya) | 2.99 | 🟢 Normal | -0.041 |  |
| 2026-11-05 02:02:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 02:02:17 | Moragaswewa (Deduru Oya) | 3.99 | 🟢 Normal | -0.040 |  |
| 2026-11-05 02:02:12 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:01:50 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.026 |  |
| 2026-11-05 02:01:48 | Kuda Oya (Kirindi Oya) | 4.00 | 🟢 Normal | -0.119 |  |
| 2026-11-05 02:01:09 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-05 02:00:48 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.030 |  |
| 2026-11-05 02:00:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.169 |  |
| 2026-11-05 02:00:43 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-11-05 02:00:28 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:57:03 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.006 |  |
| 2026-11-05 01:38:37 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | -0.026 |  |
| 2026-11-05 01:22:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-11-05 01:18:55 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 01:17:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 01:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-11-05 00:09:03 | Urawa (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-11-05 01:03:33 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-05 01:09:37 | Thanamalwila (Kirindi Oya) | 3.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 02:02:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-05 01:09:36 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 00:02:01 | Magura (Kalu Ganga) | 2.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-11-05 01:03:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-05 01:05:26 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 01:18:55 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 02:02:12 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:01:55 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:01:57 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 00:10:03 | Panadugama (Nilwala Ganga) | 4.15 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:03:35 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:17:20 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:00:28 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 01:57:03 | Rathnapura (Kalu Ganga) | 2.23 | 🟢 Normal | -0.006 |  |
| 2026-11-05 02:01:09 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-11-05 01:03:19 | Badalgama (Maha Oya) | 3.44 | 🟢 Normal | -0.021 |  |
| 2026-11-05 02:03:00 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.022 |  |
| 2026-11-05 01:22:33 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.025 |  |
| 2026-11-05 02:01:50 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.026 |  |
| 2026-11-05 01:03:51 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-11-05 02:02:51 | Glencourse (Kelani Ganga) | 11.16 | 🟢 Normal | -0.029 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-05 02:00:48 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 02:02:17 | Moragaswewa (Deduru Oya) | 3.99 | 🟢 Normal | -0.040 |  |
| 2026-11-05 02:00:43 | Manampitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.040 |  |
| 2026-11-05 02:02:20 | Giriulla (Maha Oya) | 2.99 | 🟢 Normal | -0.041 |  |
| 2026-11-05 02:03:03 | Ellagawa (Kalu Ganga) | 6.30 | 🟢 Normal | -0.055 |  |
| 2026-11-05 01:04:28 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.086 |  |
| 2026-11-05 01:03:37 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.088 |  |
| 2026-11-05 02:01:48 | Kuda Oya (Kirindi Oya) | 4.00 | 🟢 Normal | -0.119 |  |
| 2026-11-05 02:00:46 | Wellawaya (Kirindi Oya) | 1.78 | 🟢 Normal | -0.169 |  |
| 2026-11-05 01:04:17 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -1.861 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)