# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_05:24:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,193 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 05:24:57 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | -0.025 |  |
| 2026-09-26 05:24:00 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-26 05:23:52 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.007 |  |
| 2026-09-26 05:15:20 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:10:34 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.082 |  |
| 2026-09-26 05:10:23 | Kithulgala (Kelani Ganga) | 2.76 | 🟢 Normal | -0.232 |  |
| 2026-09-26 05:07:50 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:06:28 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.037 |  |
| 2026-09-26 05:05:43 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.094 |  |
| 2026-09-26 05:05:42 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.075 |  |
| 2026-09-26 05:05:20 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.07 | 🟠 Minor Flood | -0.015 |  |
| 2026-09-26 05:04:45 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-26 05:04:17 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-09-26 05:04:02 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:04:01 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-26 05:03:57 | Hanwella (Kelani Ganga) | 5.87 | 🟢 Normal | -0.012 |  |
| 2026-09-26 05:03:28 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-26 05:03:14 | Glencourse (Kelani Ganga) | 13.66 | 🟢 Normal | -0.080 |  |
| 2026-09-26 05:03:11 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.174 |  |
| 2026-09-26 05:03:06 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:02:50 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 05:04:01 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-09-26 05:24:00 | Baddegama (Gin Ganga) | 4.81 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-26 05:05:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.07 | 🟠 Minor Flood | -0.015 |  |
| 2026-09-26 05:24:57 | Panadugama (Nilwala Ganga) | 6.11 | 🟠 Minor Flood | -0.025 |  |
| 2026-09-26 05:01:44 | Rathnapura (Kalu Ganga) | 5.47 | 🟡 Alert | 0.000 |  |
| 2026-09-26 05:10:34 | Magura (Kalu Ganga) | 4.42 | 🟡 Alert | -0.082 |  |
| 2026-09-26 05:01:31 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-09-26 05:00:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-09-26 05:00:36 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:04:02 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:03:06 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:02:20 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.000 |  |
| 2026-09-26 03:19:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:15:20 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:02:25 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:05:20 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:07:50 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:01:08 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:02:07 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 05:23:52 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.007 |  |
| 2026-09-26 05:02:50 | Norwood (Kelani Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-09-26 05:04:45 | Giriulla (Maha Oya) | 1.81 | 🟢 Normal | -0.010 |  |
| 2026-09-26 05:03:28 | Nawalapitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.010 |  |
| 2026-09-26 05:02:35 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-09-26 05:03:57 | Hanwella (Kelani Ganga) | 5.87 | 🟢 Normal | -0.012 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 05:02:38 | Deraniyagala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.021 |  |
| 2026-09-26 04:08:49 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.028 |  |
| 2026-09-26 05:04:17 | Badalgama (Maha Oya) | 3.01 | 🟢 Normal | -0.029 |  |
| 2026-09-26 05:06:28 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | -0.037 |  |
| 2026-09-26 05:01:16 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | -0.060 |  |
| 2026-09-26 05:05:42 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.075 |  |
| 2026-09-26 05:03:14 | Glencourse (Kelani Ganga) | 13.66 | 🟢 Normal | -0.080 |  |
| 2026-09-26 05:05:43 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.094 |  |
| 2026-09-26 05:03:11 | Peradeniya (Mahaweli Ganga) | 3.82 | 🟢 Normal | -0.174 |  |
| 2026-09-26 05:10:23 | Kithulgala (Kelani Ganga) | 2.76 | 🟢 Normal | -0.232 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)