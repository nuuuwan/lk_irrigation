# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_11:03:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,894 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Moraketiya — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-11-28 11:03:27 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:03:20 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:02:59 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-28 11:02:56 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.020 |  |
| 2026-11-28 11:02:49 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.227 |  |
| 2026-11-28 11:02:45 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.100 |  |
| 2026-11-28 11:02:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | -0.010 |  |
| 2026-11-28 11:02:22 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-28 11:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-28 11:02:04 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:01 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:01:51 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-28 11:01:50 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.176 |  |
| 2026-11-28 11:01:29 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 11:01:10 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-28 11:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 11:00:11 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:43:27 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 11:01:29 | Dunamale (Aththanagalu Oya) | 3.99 | 🟡 Alert | 0.000 |  |
| 2026-11-28 11:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.20 | 🟡 Alert | -0.010 |  |
| 2026-11-28 11:02:56 | Moraketiya (Walawe Ganga) | 3.15 | 🟡 Alert | -0.020 |  |
| 2026-11-28 10:02:51 | Panadugama (Nilwala Ganga) | 5.43 | 🟡 Alert | -0.051 |  |
| 2026-11-28 11:02:59 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-28 11:00:43 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-28 11:02:01 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:33 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:04:06 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:41 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:00:11 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-28 11:02:04 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-28 10:12:21 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:03:20 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:03:27 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-11-28 11:01:50 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-28 10:01:13 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.011 |  |
| 2026-11-28 10:08:15 | Moragaswewa (Deduru Oya) | 2.28 | 🟢 Normal | -0.018 |  |
| 2026-11-28 11:03:29 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.022 |  |
| 2026-11-28 10:11:39 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-11-28 11:02:08 | Thanamalwila (Kirindi Oya) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-28 10:02:22 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.030 |  |
| 2026-11-28 11:01:10 | Kuda Oya (Kirindi Oya) | 2.45 | 🟢 Normal | -0.031 |  |
| 2026-11-28 10:13:53 | Holombuwa (Kelani Ganga) | 1.40 | 🟢 Normal | -0.037 |  |
| 2026-11-28 11:02:22 | Manampitiya (Mahaweli Ganga) | 1.84 | 🟢 Normal | -0.040 |  |
| 2026-11-28 10:03:53 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.049 |  |
| 2026-11-28 10:05:42 | Galgamuwa (Mee Oya) | 0.57 | 🟢 Normal | -0.052 |  |
| 2026-11-28 11:01:51 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.052 |  |
| 2026-11-28 10:04:37 | Giriulla (Maha Oya) | 2.87 | 🟢 Normal | -0.058 |  |
| 2026-11-28 10:05:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.059 |  |
| 2026-11-28 10:02:22 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.060 |  |
| 2026-11-28 10:04:44 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.062 |  |
| 2026-11-28 10:03:55 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.095 |  |
| 2026-11-28 11:02:45 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.100 |  |
| 2026-11-28 10:12:50 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.102 |  |
| 2026-11-28 10:12:19 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.109 |  |
| 2026-11-28 11:01:44 | Glencourse (Kelani Ganga) | 11.35 | 🟢 Normal | -0.176 |  |
| 2026-11-28 11:02:49 | Pitabeddara (Nilwala Ganga) | 2.07 | 🟢 Normal | -0.227 |  |

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)