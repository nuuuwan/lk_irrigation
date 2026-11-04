# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_04:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,167 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 04:03:20 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 04:03:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-11-05 04:03:13 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | -0.063 |  |
| 2026-11-05 04:03:06 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.107 |  |
| 2026-11-05 04:03:03 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-05 04:02:52 | Dunamale (Aththanagalu Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 04:01:59 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:51 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:45 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:25 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | -0.010 |  |
| 2026-11-05 04:01:16 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-11-05 04:01:09 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.604 |  |
| 2026-11-05 04:00:14 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.023 |  |
| 2026-11-05 04:00:11 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.020 |  |
| 2026-11-05 03:59:57 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:50:54 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-05 03:31:15 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.016 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 04:01:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.17 | 🟡 Alert | -0.010 |  |
| 2026-11-05 04:01:16 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | 0.851 | 🔺 Rising |
| 2026-11-05 03:09:49 | Kithulgala (Kelani Ganga) | 2.07 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-11-05 03:04:47 | Badalgama (Maha Oya) | 3.70 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-11-05 03:50:54 | Rathnapura (Kalu Ganga) | 2.53 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-05 02:11:57 | Urawa (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-05 03:06:56 | Hanwella (Kelani Ganga) | 2.83 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-11-05 01:07:28 | Pitabeddara (Nilwala Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-05 03:21:12 | Panadugama (Nilwala Ganga) | 4.22 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-11-05 04:03:20 | Moraketiya (Walawe Ganga) | 2.10 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-05 04:02:52 | Dunamale (Aththanagalu Oya) | 3.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-05 03:31:15 | Putupaula (Kalu Ganga) | 1.45 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-11-05 03:03:38 | Thawalama (Gin Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 02:06:12 | Magura (Kalu Ganga) | 2.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 04:01:45 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 02:03:41 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:01 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:25 | Padiyathalawa (Maduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:02:11 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:04:56 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-04 18:00:12 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:59 | Peradeniya (Mahaweli Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-11-05 04:01:51 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-05 03:07:01 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-11-05 03:04:36 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-05 04:03:03 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-05 04:03:15 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-11-05 04:00:11 | Glencourse (Kelani Ganga) | 11.12 | 🟢 Normal | -0.020 |  |
| 2026-11-05 04:00:14 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.023 |  |
| 2026-11-04 18:02:29 | Galgamuwa (Mee Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-11-04 18:03:43 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.038 |  |
| 2026-11-05 04:03:13 | Ellagawa (Kalu Ganga) | 6.19 | 🟢 Normal | -0.063 |  |
| 2026-11-05 03:01:52 | Moragaswewa (Deduru Oya) | 3.92 | 🟢 Normal | -0.070 |  |
| 2026-11-05 03:04:02 | Holombuwa (Kelani Ganga) | 1.17 | 🟢 Normal | -0.077 |  |
| 2026-11-05 04:03:06 | Giriulla (Maha Oya) | 2.78 | 🟢 Normal | -0.107 |  |
| 2026-11-05 03:15:15 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.108 |  |
| 2026-11-05 03:13:38 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | -0.141 |  |
| 2026-11-05 03:08:13 | Thanamalwila (Kirindi Oya) | 2.91 | 🟢 Normal | -0.253 |  |
| 2026-11-05 04:01:09 | Kuda Oya (Kirindi Oya) | 3.10 | 🟢 Normal | -0.604 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)