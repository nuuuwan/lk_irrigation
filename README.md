# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_10:13:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 10:13:53 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.037 |  |
| 2026-11-28 10:12:50 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.102 |  |
| 2026-11-28 10:12:21 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:12:19 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.109 |  |
| 2026-11-28 10:11:39 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-11-28 10:10:58 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-28 10:10:00 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.135 |  |
| 2026-11-28 10:08:22 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.054 |  |
| 2026-11-28 10:08:15 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-28 10:05:42 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.052 |  |
| 2026-11-28 10:05:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-11-28 10:04:44 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.062 |  |
| 2026-11-28 10:04:41 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-28 10:04:37 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | -0.058 |  |
| 2026-11-28 10:04:36 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:31 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-28 10:04:06 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:03:56 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.145 |  |
| 2026-11-28 10:03:55 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.095 |  |
| 2026-11-28 10:03:53 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-11-28 10:03:39 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.028 |  |
| 2026-11-28 10:03:27 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-28 10:03:00 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.050 |  |
| 2026-11-28 10:02:52 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:02:51 | Panadugama (Nilwala Ganga) | 5.43 | 🟡 Alert | -0.051 |  |
| 2026-11-28 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.010 |  |
| 2026-11-28 10:02:42 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 10:02:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:02:27 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 10:02:22 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-11-28 10:02:22 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.060 |  |
| 2026-11-28 10:01:59 | Moraketiya (Walawe Ganga) | 3.17 | 🟡 Alert | -0.010 |  |
| 2026-11-28 10:01:48 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-28 10:01:46 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 10:02:42 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 10:02:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.21 | 🟡 Alert | -0.010 |  |
| 2026-11-28 10:01:59 | Moraketiya (Walawe Ganga) | 3.17 | 🟡 Alert | -0.010 |  |
| 2026-11-28 10:02:51 | Panadugama (Nilwala Ganga) | 5.43 | 🟡 Alert | -0.051 |  |
| 2026-11-28 10:04:31 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-11-28 10:10:58 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-28 10:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:06 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:36 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:01:29 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:12:21 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:02:40 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:01:46 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:02:52 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:01:13 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-11-28 10:08:15 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-28 10:03:27 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.020 |  |
| 2026-11-28 10:01:48 | Thanamalwila (Kirindi Oya) | 2.18 | 🟢 Normal | -0.020 |  |
| 2026-11-28 10:02:27 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.022 |  |
| 2026-11-28 10:11:39 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-11-28 10:03:39 | Kuda Oya (Kirindi Oya) | 2.48 | 🟢 Normal | -0.028 |  |
| 2026-11-28 10:02:22 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-11-28 10:13:53 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.037 |  |
| 2026-11-28 10:00:20 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-11-28 10:04:41 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-28 10:03:53 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-11-28 10:03:00 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.050 |  |
| 2026-11-28 10:05:42 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.052 |  |
| 2026-11-28 10:08:22 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | -0.054 |  |
| 2026-11-28 10:04:37 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | -0.058 |  |
| 2026-11-28 10:05:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-11-28 10:02:22 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.060 |  |
| 2026-11-28 10:04:44 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.062 |  |
| 2026-11-28 10:03:55 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.095 |  |
| 2026-11-28 10:12:50 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.102 |  |
| 2026-11-28 10:12:19 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.109 |  |
| 2026-11-28 10:10:00 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.135 |  |
| 2026-11-28 10:03:56 | Glencourse (Kelani Ganga) | 11.52 | 🟢 Normal | -0.145 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)