# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_17:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 17:15:19 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | -0.045 |  |
| 2026-09-22 17:12:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:08:16 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-09-22 17:07:41 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:07:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-22 17:06:54 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.062 |  |
| 2026-09-22 17:06:52 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:06:46 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-09-22 17:06:30 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 17:05:58 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | -0.039 |  |
| 2026-09-22 17:05:07 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 17:04:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 17:04:56 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:04:34 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.019 |  |
| 2026-09-22 17:04:20 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:04:09 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:55 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-09-22 17:03:53 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 17:03:47 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | -0.039 |  |
| 2026-09-22 17:03:35 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:17 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 17:03:06 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-09-22 17:03:02 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.077 |  |
| 2026-09-22 17:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 17:02:54 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:02:41 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-09-22 17:02:25 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 17:02:16 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 17:01:49 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:40 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-22 17:01:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-22 17:00:44 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:00:38 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-09-22 17:00:32 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 17:06:30 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 17:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 17:02:16 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 17:04:34 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.019 |  |
| 2026-09-22 17:03:55 | Deraniyagala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.266 | 🔺 Rising |
| 2026-09-22 17:07:11 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-09-22 17:04:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 17:05:07 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 17:02:25 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 17:03:53 | Dunamale (Aththanagalu Oya) | 2.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 17:03:17 | Nawalapitiya (Mahaweli Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 17:00:32 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:12:40 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:42 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:00:44 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:35 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:04:09 | Hanwella (Kelani Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:07:41 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:04:20 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:02:54 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:34 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:03:06 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:06:52 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:49 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:04:56 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-09-22 17:01:12 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-22 17:01:40 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-09-22 17:08:16 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | -0.011 |  |
| 2026-09-22 17:06:46 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.020 |  |
| 2026-09-22 17:00:38 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-09-22 17:03:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.030 |  |
| 2026-09-22 17:05:58 | Ellagawa (Kalu Ganga) | 8.77 | 🟢 Normal | -0.039 |  |
| 2026-09-22 17:03:47 | Rathnapura (Kalu Ganga) | 4.16 | 🟢 Normal | -0.039 |  |
| 2026-09-22 17:02:41 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.044 |  |
| 2026-09-22 17:15:19 | Panadugama (Nilwala Ganga) | 4.82 | 🟢 Normal | -0.045 |  |
| 2026-09-22 17:06:54 | Glencourse (Kelani Ganga) | 12.52 | 🟢 Normal | -0.062 |  |
| 2026-09-22 17:03:02 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)