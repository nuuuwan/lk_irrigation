# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_09:09:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,624 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 09:09:37 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:08:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:07:41 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-23 09:07:22 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | -0.030 |  |
| 2026-09-23 09:07:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 09:07:05 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.013 |  |
| 2026-09-23 09:06:40 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.040 |  |
| 2026-09-23 09:06:20 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.038 |  |
| 2026-09-23 09:06:10 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-23 09:05:49 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:05:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:05:01 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.031 |  |
| 2026-09-23 09:04:38 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 09:04:17 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.060 |  |
| 2026-09-23 09:04:09 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:04:04 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-09-23 09:04:03 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:03:57 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:03:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:39 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:32 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-09-23 09:03:13 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.022 |  |
| 2026-09-23 09:03:12 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 09:03:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:09 | Ellagawa (Kalu Ganga) | 8.17 | 🟢 Normal | -0.033 |  |
| 2026-09-23 09:02:57 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:02:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:27 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.021 |  |
| 2026-09-23 09:02:23 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:01:32 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:00:30 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:00:26 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:00:23 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:00:19 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 08:28:56 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 08:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 08:06:15 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | 0.000 |  |
| 2026-09-23 09:03:13 | Magura (Kalu Ganga) | 4.05 | 🟡 Alert | -0.022 |  |
| 2026-09-23 09:07:22 | Baddegama (Gin Ganga) | 3.84 | 🟡 Alert | -0.030 |  |
| 2026-09-23 09:07:10 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-23 09:03:12 | Hanwella (Kelani Ganga) | 4.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-23 09:04:29 | Nawalapitiya (Mahaweli Ganga) | 2.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 09:02:23 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:08:20 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:39 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:39 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:04:09 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:05:37 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:09:37 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:12 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:03:56 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:00:23 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:00:30 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:05:49 | Rathnapura (Kalu Ganga) | 3.89 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:00:19 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:15 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 09:02:57 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:01:32 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:00:26 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:04:03 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:03:57 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-09-23 09:03:32 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.011 |  |
| 2026-09-23 09:07:05 | Urawa (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.013 |  |
| 2026-09-23 09:06:10 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-09-23 09:04:04 | Putupaula (Kalu Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-09-23 09:07:41 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-09-23 09:02:27 | Peradeniya (Mahaweli Ganga) | 3.52 | 🟢 Normal | -0.021 |  |
| 2026-09-23 08:07:00 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-09-23 09:05:01 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | -0.031 |  |
| 2026-09-23 09:03:09 | Ellagawa (Kalu Ganga) | 8.17 | 🟢 Normal | -0.033 |  |
| 2026-09-23 09:06:20 | Dunamale (Aththanagalu Oya) | 2.64 | 🟢 Normal | -0.038 |  |
| 2026-09-23 09:06:40 | Glencourse (Kelani Ganga) | 12.85 | 🟢 Normal | -0.040 |  |
| 2026-09-23 09:04:17 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)