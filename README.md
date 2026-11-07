# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_04:03:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,866 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 04:03:15 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-11-08 04:03:12 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-08 04:02:59 | Baddegama (Gin Ganga) | 2.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-08 04:02:53 | Moragaswewa (Deduru Oya) | 2.03 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-08 04:02:46 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-11-08 04:02:36 | Giriulla (Maha Oya) | 3.49 | 🟢 Normal | -0.020 |  |
| 2026-11-08 04:02:12 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:01:46 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | 0.457 | 🔺 Rising |
| 2026-11-08 04:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.085 |  |
| 2026-11-08 04:01:06 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.020 |  |
| 2026-11-08 04:00:49 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.260 |  |
| 2026-11-08 03:37:37 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 03:34:25 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 04:01:46 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | 0.457 | 🔺 Rising |
| 2026-11-08 03:10:46 | Moraketiya (Walawe Ganga) | 4.60 | 🟡 Alert | 0.085 | 🔺 Rising |
| 2026-11-08 03:34:25 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |
| 2026-11-08 03:06:31 | Urawa (Nilwala Ganga) | 3.28 | 🟡 Alert | -0.136 |  |
| 2026-11-08 04:02:46 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-11-08 03:28:49 | Rathnapura (Kalu Ganga) | 4.75 | 🟢 Normal | 0.236 | 🔺 Rising |
| 2026-11-08 01:10:01 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-08 04:02:53 | Moragaswewa (Deduru Oya) | 2.03 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-08 04:03:12 | Ellagawa (Kalu Ganga) | 6.99 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-11-08 04:02:59 | Baddegama (Gin Ganga) | 2.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-08 04:02:12 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 03:03:44 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 03:08:32 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-08 03:37:37 | Putupaula (Kalu Ganga) | 1.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-08 03:07:30 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:07:10 | Horowpothana (Yan Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:03:10 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:01:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:03:21 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:07:25 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-08 03:05:31 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 03:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-11-08 03:03:10 | Hanwella (Kelani Ganga) | 3.29 | 🟢 Normal | -0.020 |  |
| 2026-11-08 04:02:36 | Giriulla (Maha Oya) | 3.49 | 🟢 Normal | -0.020 |  |
| 2026-11-08 04:01:06 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 04:03:15 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-11-08 03:05:05 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.058 |  |
| 2026-11-08 04:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.085 |  |
| 2026-11-08 03:04:01 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.089 |  |
| 2026-11-08 03:06:11 | Thawalama (Gin Ganga) | 3.43 | 🟢 Normal | -0.102 |  |
| 2026-11-08 03:01:24 | Nakkala (Kumbukkan Oya) | 1.63 | 🟢 Normal | -0.139 |  |
| 2026-11-08 03:05:34 | Thanamalwila (Kirindi Oya) | 2.56 | 🟢 Normal | -0.229 |  |
| 2026-11-08 03:05:25 | Wellawaya (Kirindi Oya) | 2.26 | 🟢 Normal | -0.244 |  |
| 2026-11-08 04:00:49 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.260 |  |
| 2026-11-08 02:36:30 | Pitabeddara (Nilwala Ganga) | 1.47 | 🟢 Normal | -0.371 |  |
| 2026-11-08 03:02:32 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)