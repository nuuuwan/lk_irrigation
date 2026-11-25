# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--25_11:03:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **325,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 11:03:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 11:03:27 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-25 11:03:17 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-11-25 11:03:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 11:02:58 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-25 11:02:53 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:43 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.081 |  |
| 2026-11-25 11:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:32 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.139 |  |
| 2026-11-25 11:02:22 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.084 |  |
| 2026-11-25 11:02:14 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.137 |  |
| 2026-11-25 11:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-25 11:02:03 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-25 11:01:55 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 11:01:48 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | -0.106 |  |
| 2026-11-25 11:01:47 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:01:45 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-11-25 11:01:28 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:00:31 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.411 |  |
| 2026-11-25 11:00:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 11:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-25 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-25 10:29:10 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.008 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-25 10:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-25 11:00:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-11-25 11:02:10 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-25 11:03:04 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-25 11:02:03 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-25 11:01:55 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-25 11:00:23 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-25 11:03:38 | Putupaula (Kalu Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-25 10:29:10 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-25 10:01:22 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Moragaswewa (Deduru Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:02:20 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:33 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:48 | Ellagawa (Kalu Ganga) | 6.78 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:02:53 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-25 11:01:28 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-25 10:01:06 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:01:47 | Thanamalwila (Kirindi Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-11-25 11:03:27 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-25 11:00:14 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.021 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-25 10:06:25 | Panadugama (Nilwala Ganga) | 4.74 | 🟢 Normal | -0.026 |  |
| 2026-11-25 11:02:58 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-11-25 10:06:05 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.038 |  |
| 2026-11-25 11:03:17 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.042 |  |
| 2026-11-25 11:01:45 | Nakkala (Kumbukkan Oya) | 1.07 | 🟢 Normal | -0.050 |  |
| 2026-11-25 10:09:46 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.080 |  |
| 2026-11-25 11:02:43 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.081 |  |
| 2026-11-25 10:12:07 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | -0.084 |  |
| 2026-11-25 11:02:22 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | -0.084 |  |
| 2026-11-25 11:01:48 | Dunamale (Aththanagalu Oya) | 3.13 | 🟢 Normal | -0.106 |  |
| 2026-11-25 10:06:40 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.130 |  |
| 2026-11-25 11:02:14 | Hanwella (Kelani Ganga) | 3.41 | 🟢 Normal | -0.137 |  |
| 2026-11-25 11:02:32 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.139 |  |
| 2026-11-25 10:04:27 | Rathnapura (Kalu Ganga) | 3.35 | 🟢 Normal | -0.164 |  |
| 2026-11-25 11:00:31 | Moraketiya (Walawe Ganga) | 2.24 | 🟢 Normal | -0.411 |  |
| 2026-11-25 10:01:13 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -1.150 |  |
| 2026-11-25 10:09:58 | Baddegama (Gin Ganga) | 2.28 | 🟢 Normal | -3.148 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)