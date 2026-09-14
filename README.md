# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_02:35:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,152 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thawalama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 02:35:20 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 02:20:21 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-15 02:19:23 | Thawalama (Gin Ganga) | 4.27 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-15 02:19:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:14:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-15 02:14:24 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 02:10:45 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-15 02:08:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-09-15 02:07:11 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:06:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:05:17 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-09-15 02:05:03 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-09-15 02:04:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.037 |  |
| 2026-09-15 02:03:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 02:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:02:34 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.152 | 🔺 Rising |
| 2026-09-15 02:02:23 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 02:01:49 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.161 |  |
| 2026-09-15 02:01:48 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:36 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 02:00:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.062 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 02:19:23 | Thawalama (Gin Ganga) | 4.27 | 🟡 Alert | 0.167 | 🔺 Rising |
| 2026-09-15 02:02:34 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.152 | 🔺 Rising |
| 2026-09-15 01:03:05 | Panadugama (Nilwala Ganga) | 3.57 | 🟢 Normal | 0.727 | 🔺 Rising |
| 2026-09-15 02:05:03 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-09-15 02:05:17 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-09-15 02:02:23 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-09-15 02:35:20 | Holombuwa (Kelani Ganga) | 2.20 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-09-15 02:10:45 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-09-15 02:01:00 | Pitabeddara (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-15 02:14:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.30 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-15 02:14:24 | Ellagawa (Kalu Ganga) | 6.00 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-15 02:03:10 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-15 02:20:21 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-09-15 02:03:31 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-15 00:03:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:20 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:02:01 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:48 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-15 00:03:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:19:17 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:06:07 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:03:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:22 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:04:55 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:36 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 01:06:12 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:03:37 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:01:26 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-15 02:08:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-15 01:04:54 | Putupaula (Kalu Ganga) | 0.82 | 🟢 Normal | -0.022 |  |
| 2026-09-15 01:02:53 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.022 |  |
| 2026-09-15 02:04:46 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.037 |  |
| 2026-09-15 02:00:18 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | -0.062 |  |
| 2026-09-15 02:01:49 | Rathnapura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.161 |  |
| 2026-09-15 01:01:51 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.330 |  |
| 2026-09-14 23:40:18 | Wellawaya (Kirindi Oya) | 0.65 | 🟢 Normal | -0.347 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)