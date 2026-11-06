# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--07_05:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,009 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 05:02:50 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.402 |  |
| 2026-11-07 05:02:44 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-11-07 05:02:36 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-07 05:02:12 | Giriulla (Maha Oya) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:02:01 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 05:01:49 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.800 |  |
| 2026-11-07 05:01:14 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 05:01:02 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-07 04:57:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-07 04:57:32 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-07 04:26:00 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.016 |  |
| 2026-11-07 04:25:43 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-07 04:23:20 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-07 04:05:26 | Dunamale (Aththanagalu Oya) | 3.82 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-11-07 05:01:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.30 | 🟡 Alert | 0.000 |  |
| 2026-11-07 04:04:07 | Hanwella (Kelani Ganga) | 3.87 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-11-07 05:01:14 | Moragaswewa (Deduru Oya) | 1.81 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-07 04:02:15 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-11-07 05:02:36 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-06 18:00:25 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-07 04:08:35 | Baddegama (Gin Ganga) | 2.15 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-11-07 04:14:19 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-07 04:25:43 | Moraketiya (Walawe Ganga) | 1.95 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-07 04:23:20 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-07 04:02:57 | Horowpothana (Yan Oya) | 2.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-07 03:05:10 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-11-07 05:02:12 | Giriulla (Maha Oya) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:05:00 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-11-07 03:03:20 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-07 04:03:14 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-07 04:04:07 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:49 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-06 18:00:51 | Thanthirimale (Malwathu Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:02:50 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-07 04:57:34 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-07 05:01:02 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-07 05:02:44 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | -0.015 |  |
| 2026-11-07 04:26:00 | Putupaula (Kalu Ganga) | 1.23 | 🟢 Normal | -0.016 |  |
| 2026-11-07 04:00:25 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.021 |  |
| 2026-11-07 04:06:37 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.025 |  |
| 2026-11-07 05:02:01 | Thawalama (Gin Ganga) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-11-07 04:02:51 | Rathnapura (Kalu Ganga) | 3.24 | 🟢 Normal | -0.050 |  |
| 2026-11-07 04:03:28 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.052 |  |
| 2026-11-07 04:03:33 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.075 |  |
| 2026-11-07 04:00:47 | Nakkala (Kumbukkan Oya) | 1.36 | 🟢 Normal | -0.079 |  |
| 2026-11-07 04:00:41 | Peradeniya (Mahaweli Ganga) | 3.72 | 🟢 Normal | -0.151 |  |
| 2026-11-07 04:01:18 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.157 |  |
| 2026-11-07 04:13:33 | Holombuwa (Kelani Ganga) | 2.28 | 🟢 Normal | -0.177 |  |
| 2026-11-07 05:02:44 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.402 |  |
| 2026-11-07 05:01:29 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.800 |  |
| 2026-11-07 04:02:51 | Ellagawa (Kalu Ganga) | 0.62 | 🟢 Normal | -5.921 |  |
| 2026-11-07 04:14:14 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | -216.000 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)