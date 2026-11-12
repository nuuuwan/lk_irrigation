# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_15:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,886 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 15:03:26 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:03:18 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:03:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-12 15:03:15 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.052 |  |
| 2026-11-12 15:02:58 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.026 |  |
| 2026-11-12 15:02:56 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 15:02:55 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:55 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.108 |  |
| 2026-11-12 15:02:52 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.110 |  |
| 2026-11-12 15:02:12 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-11-12 15:01:58 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-12 15:01:50 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-12 15:01:37 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-12 15:01:31 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.066 |  |
| 2026-11-12 15:01:29 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 15:01:25 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:01:22 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-11-12 15:01:21 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:01:19 | Thaldena (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-11-12 15:00:34 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 15:00:21 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-12 14:59:57 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 14:12:57 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-11-12 14:16:58 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 14:02:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 15:03:18 | Panadugama (Nilwala Ganga) | 5.86 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:55 | Moraketiya (Walawe Ganga) | 3.80 | 🟡 Alert | -0.010 |  |
| 2026-11-12 15:02:58 | Dunamale (Aththanagalu Oya) | 4.16 | 🟡 Alert | -0.026 |  |
| 2026-11-12 14:08:33 | Magura (Kalu Ganga) | 5.16 | 🟡 Alert | -0.054 |  |
| 2026-11-12 15:01:19 | Thaldena (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.745 | 🔺 Rising |
| 2026-11-12 15:01:22 | Wellawaya (Kirindi Oya) | 2.35 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-11-12 15:00:21 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | 0.344 | 🔺 Rising |
| 2026-11-12 15:03:17 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-11-12 15:01:37 | Thanamalwila (Kirindi Oya) | 2.48 | 🟢 Normal | 0.167 | 🔺 Rising |
| 2026-11-12 15:01:29 | Manampitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-11-12 15:02:56 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 15:00:34 | Thanthirimale (Malwathu Oya) | 1.94 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 14:06:35 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-12 14:59:57 | Horowpothana (Yan Oya) | 2.50 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-12 14:04:46 | Padiyathalawa (Maduru Oya) | 0.84 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-12 15:01:21 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:07:33 | Galgamuwa (Mee Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-12 15:03:26 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-11-12 14:10:23 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.009 |  |
| 2026-11-12 14:05:39 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:02:42 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-12 15:01:58 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-12 14:03:22 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-11-12 15:01:25 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-11-12 15:01:50 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-11-12 14:04:37 | Thawalama (Gin Ganga) | 2.96 | 🟢 Normal | -0.035 |  |
| 2026-11-12 14:07:33 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.046 |  |
| 2026-11-12 15:03:15 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.052 |  |
| 2026-11-12 14:07:56 | Badalgama (Maha Oya) | 4.18 | 🟢 Normal | -0.059 |  |
| 2026-11-12 15:02:12 | Deraniyagala (Kelani Ganga) | 1.20 | 🟢 Normal | -0.060 |  |
| 2026-11-12 15:01:31 | Giriulla (Maha Oya) | 2.63 | 🟢 Normal | -0.066 |  |
| 2026-11-12 14:06:59 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.081 |  |
| 2026-11-12 15:02:55 | Moragaswewa (Deduru Oya) | 2.98 | 🟢 Normal | -0.108 |  |
| 2026-11-12 14:00:38 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | -0.109 |  |
| 2026-11-12 15:02:52 | Hanwella (Kelani Ganga) | 5.15 | 🟢 Normal | -0.110 |  |
| 2026-11-12 14:07:35 | Glencourse (Kelani Ganga) | 12.58 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)