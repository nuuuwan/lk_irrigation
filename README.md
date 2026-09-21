# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_19:32:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,207 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 19:32:00 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-21 19:15:03 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-21 19:12:15 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-21 19:11:00 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.055 |  |
| 2026-09-21 19:07:20 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-09-21 19:06:57 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-21 19:06:34 | Rathnapura (Kalu Ganga) | 5.57 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2026-09-21 19:05:56 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 19:05:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:05:38 | Glencourse (Kelani Ganga) | 12.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-21 19:05:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-09-21 19:05:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:04:59 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:04:33 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 19:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.09 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 19:04:04 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-09-21 19:04:04 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-21 19:04:00 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 19:03:23 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-21 19:03:15 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.227 |  |
| 2026-09-21 19:03:12 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:03:09 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-21 19:03:00 | Panadugama (Nilwala Ganga) | 5.45 | 🟡 Alert | -0.030 |  |
| 2026-09-21 19:02:35 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:02:31 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:02:22 | Nawalapitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.080 |  |
| 2026-09-21 19:02:11 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-21 19:02:09 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | -0.061 |  |
| 2026-09-21 19:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:17 | Magura (Kalu Ganga) | 5.26 | 🟡 Alert | -0.019 |  |
| 2026-09-21 19:01:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:15 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:14 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.061 |  |
| 2026-09-21 19:01:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.039 |  |
| 2026-09-21 19:00:42 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 19:00:34 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 19:04:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.09 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 19:05:56 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | 0.029 | 🔺 Rising |
| 2026-09-21 19:06:34 | Rathnapura (Kalu Ganga) | 5.57 | 🟡 Alert | 0.056 | 🔺 Rising |
| 2026-09-21 19:01:17 | Magura (Kalu Ganga) | 5.26 | 🟡 Alert | -0.019 |  |
| 2026-09-21 19:03:00 | Panadugama (Nilwala Ganga) | 5.45 | 🟡 Alert | -0.030 |  |
| 2026-09-21 19:01:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.039 |  |
| 2026-09-21 19:03:23 | Holombuwa (Kelani Ganga) | 1.62 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-09-21 19:03:09 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-21 19:04:04 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-21 19:05:38 | Glencourse (Kelani Ganga) | 12.97 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-21 19:12:15 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-09-21 19:00:42 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-21 19:06:57 | Putupaula (Kalu Ganga) | 2.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-09-21 19:15:03 | Urawa (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-09-21 19:04:00 | Giriulla (Maha Oya) | 1.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 19:04:33 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 19:32:00 | Pitabeddara (Nilwala Ganga) | 1.46 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-09-21 19:02:35 | Kithulgala (Kelani Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:15 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:00:34 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:05:09 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:03:12 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:05:43 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:04:59 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:02:31 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:01:15 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-21 19:02:11 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-09-21 19:07:20 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-09-21 18:02:28 | Weraganthota (Mahaweli Ganga) | -2.92 | 🟢 Normal | -0.020 |  |
| 2026-09-21 18:04:00 | Galgamuwa (Mee Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-09-21 19:04:04 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.029 |  |
| 2026-09-21 19:05:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-09-21 19:11:00 | Badalgama (Maha Oya) | 3.06 | 🟢 Normal | -0.055 |  |
| 2026-09-21 19:01:14 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.061 |  |
| 2026-09-21 19:02:09 | Hanwella (Kelani Ganga) | 5.42 | 🟢 Normal | -0.061 |  |
| 2026-09-21 19:02:22 | Nawalapitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.080 |  |
| 2026-09-21 19:03:15 | Deraniyagala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)