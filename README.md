# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_00:34:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 00:34:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:24:34 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:21:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:17:35 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-24 00:13:48 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:09:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-24 00:09:31 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-24 00:08:59 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 00:08:39 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 00:07:24 | Urawa (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-09-24 00:07:24 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-09-24 00:07:01 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-24 00:06:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:06:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:05:33 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:05:18 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-24 00:04:16 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 00:03:43 | Thawalama (Gin Ganga) | 4.03 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-24 00:03:33 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:26 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:09 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:03 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-09-24 00:02:36 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:22 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 00:02:19 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:17 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.040 |  |
| 2026-09-24 00:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:44 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 00:01:41 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 00:01:30 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 00:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:04 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 00:00:14 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-23 23:57:23 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 23:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.84 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 00:03:43 | Thawalama (Gin Ganga) | 4.03 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-24 00:07:24 | Baddegama (Gin Ganga) | 3.65 | 🟡 Alert | 0.000 |  |
| 2026-09-24 00:07:24 | Urawa (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.318 | 🔺 Rising |
| 2026-09-24 00:05:33 | Pitabeddara (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:13:48 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-24 00:07:01 | Peradeniya (Mahaweli Ganga) | 4.02 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-09-24 00:09:31 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-24 00:01:44 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 00:08:59 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 00:01:04 | Kithulgala (Kelani Ganga) | 2.40 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-24 00:01:32 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-24 00:02:22 | Glencourse (Kelani Ganga) | 12.68 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 00:08:39 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 00:17:35 | Rathnapura (Kalu Ganga) | 4.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-09-24 00:04:16 | Ellagawa (Kalu Ganga) | 7.80 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 00:09:49 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-24 00:01:30 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 00:01:41 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:06:41 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:26 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:34:25 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:21:17 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:05:18 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:19 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:06:40 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:03:09 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:32 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:24:34 | Putupaula (Kalu Ganga) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:36 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:00:14 | Thalgahagoda (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-09-24 00:02:16 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-24 00:03:03 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-09-24 00:04:45 | Nawalapitiya (Mahaweli Ganga) | 2.53 | 🟢 Normal | -0.010 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 00:02:17 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)