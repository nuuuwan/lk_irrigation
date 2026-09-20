# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_00:22:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,481 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Dunamale — Alert; 🟡 Baddegama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 00:22:56 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-09-21 00:20:23 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-21 00:20:09 | Magura (Kalu Ganga) | 5.62 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-09-21 00:19:04 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | -0.040 |  |
| 2026-09-21 00:17:01 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-09-21 00:12:02 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-09-21 00:11:14 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:10:53 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:07:10 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.076 |  |
| 2026-09-21 00:07:03 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-09-21 00:06:34 | Holombuwa (Kelani Ganga) | 2.24 | 🟢 Normal | -0.354 |  |
| 2026-09-21 00:06:12 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-21 00:06:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:05:45 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | -0.119 |  |
| 2026-09-21 00:05:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-21 00:05:14 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-21 00:05:00 | Hanwella (Kelani Ganga) | 6.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-21 00:04:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:04:47 | Glencourse (Kelani Ganga) | 15.55 | 🟡 Alert | -0.049 |  |
| 2026-09-21 00:04:46 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-21 00:04:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:03:38 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.052 |  |
| 2026-09-21 00:03:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 00:03:25 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.150 |  |
| 2026-09-21 00:03:19 | Thawalama (Gin Ganga) | 5.40 | 🟡 Alert | -0.049 |  |
| 2026-09-21 00:03:17 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.053 |  |
| 2026-09-21 00:03:07 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -0.081 |  |
| 2026-09-21 00:02:52 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | -0.119 |  |
| 2026-09-21 00:02:46 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:02:25 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.119 |  |
| 2026-09-21 00:02:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:01:47 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 00:01:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:01:38 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.150 |  |
| 2026-09-21 00:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-09-21 00:00:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:00:22 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.304 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 00:03:07 | Panadugama (Nilwala Ganga) | 6.17 | 🟠 Minor Flood | -0.081 |  |
| 2026-09-21 00:17:01 | Dunamale (Aththanagalu Oya) | 3.43 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-09-21 00:06:12 | Baddegama (Gin Ganga) | 3.71 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-09-21 00:01:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.10 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-09-21 00:20:09 | Magura (Kalu Ganga) | 5.62 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-09-21 00:07:03 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.014 | 🔺 Rising |
| 2026-09-21 00:19:04 | Rathnapura (Kalu Ganga) | 6.45 | 🟡 Alert | -0.040 |  |
| 2026-09-21 00:03:19 | Thawalama (Gin Ganga) | 5.40 | 🟡 Alert | -0.049 |  |
| 2026-09-21 00:04:47 | Glencourse (Kelani Ganga) | 15.55 | 🟡 Alert | -0.049 |  |
| 2026-09-21 00:03:38 | Norwood (Kelani Ganga) | 1.53 | 🟡 Alert | -0.052 |  |
| 2026-09-21 00:05:45 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | -0.119 |  |
| 2026-09-21 00:00:22 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | 0.304 | 🔺 Rising |
| 2026-09-21 00:05:14 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-09-21 00:05:00 | Hanwella (Kelani Ganga) | 6.79 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-21 00:05:43 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-21 00:04:46 | Ellagawa (Kalu Ganga) | 8.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-21 00:20:23 | Putupaula (Kalu Ganga) | 2.28 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 00:01:47 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 00:03:34 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 00:01:40 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:02:46 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:00:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:04:15 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:06:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:11:14 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:04:59 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:02:07 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-21 00:12:02 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-21 00:22:56 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.022 |  |
| 2026-09-21 00:03:17 | Urawa (Nilwala Ganga) | 1.44 | 🟢 Normal | -0.053 |  |
| 2026-09-21 00:07:10 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.076 |  |
| 2026-09-21 00:02:52 | Giriulla (Maha Oya) | 3.42 | 🟢 Normal | -0.119 |  |
| 2026-09-21 00:02:25 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.119 |  |
| 2026-09-21 00:01:38 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.150 |  |
| 2026-09-21 00:03:25 | Deraniyagala (Kelani Ganga) | 2.41 | 🟢 Normal | -0.150 |  |
| 2026-09-21 00:06:34 | Holombuwa (Kelani Ganga) | 2.24 | 🟢 Normal | -0.354 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)