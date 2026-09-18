# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--19_05:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **264,824 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 05:02:53 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:49 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.081 |  |
| 2026-09-19 05:02:44 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:25 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:23 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.190 |  |
| 2026-09-19 05:02:18 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:17 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:32 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:30 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:29 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:16 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.249 |  |
| 2026-09-19 05:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-09-19 05:00:42 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 04:40:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.190 |  |
| 2026-09-19 04:34:46 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.014 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-19 04:03:51 | Magura (Kalu Ganga) | 4.08 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-19 04:08:21 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-19 04:02:06 | Hanwella (Kelani Ganga) | 1.78 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-09-19 04:02:18 | Putupaula (Kalu Ganga) | 0.96 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-19 04:00:56 | Ellagawa (Kalu Ganga) | 4.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-19 05:02:25 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-09-19 04:01:17 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:00:42 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:53 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:04:24 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:29 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:44 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:44 | Dunamale (Aththanagalu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:01:32 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-19 03:04:08 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:17 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-19 04:03:02 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 05:02:18 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-19 04:02:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-09-18 18:03:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-19 04:03:04 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-09-19 04:04:09 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2026-09-19 04:01:34 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-09-19 03:05:31 | Baddegama (Gin Ganga) | 2.70 | 🟢 Normal | -0.011 |  |
| 2026-09-19 04:34:46 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.014 |  |
| 2026-09-19 03:01:09 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-09-19 00:11:55 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.018 |  |
| 2026-09-19 04:06:08 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.019 |  |
| 2026-09-19 04:07:57 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-09-19 04:05:47 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | -0.030 |  |
| 2026-09-19 03:03:03 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.055 |  |
| 2026-09-19 04:03:16 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.055 |  |
| 2026-09-19 04:07:00 | Panadugama (Nilwala Ganga) | 3.17 | 🟢 Normal | -0.076 |  |
| 2026-09-19 05:02:49 | Glencourse (Kelani Ganga) | 10.19 | 🟢 Normal | -0.081 |  |
| 2026-09-19 05:00:56 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.115 |  |
| 2026-09-19 05:02:23 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | -0.190 |  |
| 2026-09-19 05:01:16 | Peradeniya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.249 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)