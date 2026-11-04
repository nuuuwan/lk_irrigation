# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_12:17:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 12:17:17 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:12:15 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:10:11 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.074 |  |
| 2026-11-04 12:09:41 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.042 |  |
| 2026-11-04 12:09:23 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 12:09:04 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:07:09 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 12:06:46 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-11-04 12:06:41 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-11-04 12:06:00 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.070 |  |
| 2026-11-04 12:05:52 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-04 12:05:32 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-11-04 12:05:16 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-11-04 12:04:45 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.072 |  |
| 2026-11-04 12:04:44 | Giriulla (Maha Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-11-04 12:04:03 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.077 |  |
| 2026-11-04 12:03:32 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-11-04 12:03:32 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:03:22 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:03:18 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.128 |  |
| 2026-11-04 12:03:17 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 12:03:16 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.112 |  |
| 2026-11-04 12:03:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-11-04 12:02:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-11-04 12:02:44 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.061 |  |
| 2026-11-04 12:02:28 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-04 12:02:25 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:02:21 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.033 |  |
| 2026-11-04 12:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:02:07 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-11-04 12:02:07 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.056 |  |
| 2026-11-04 12:01:59 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.091 |  |
| 2026-11-04 12:01:43 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:01:26 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.069 |  |
| 2026-11-04 12:01:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:01:14 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:01:06 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 12:00:51 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:00:14 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:00:08 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:59:45 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 12:04:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.08 | 🟡 Alert | 0.000 |  |
| 2026-11-04 12:02:28 | Putupaula (Kalu Ganga) | 1.36 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-04 12:09:23 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-04 12:01:06 | Moragaswewa (Deduru Oya) | 4.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-04 12:03:17 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-04 12:07:09 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-04 12:05:52 | Ellagawa (Kalu Ganga) | 6.82 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-04 12:01:25 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:04:44 | Giriulla (Maha Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:03:22 | Moraketiya (Walawe Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:02:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:01:14 | Manampitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:17:17 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:12:15 | Kuda Oya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-04 12:06:46 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-11-04 12:05:32 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-11-04 12:02:25 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:03:32 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:00:08 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-11-04 12:00:14 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 11:59:45 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.011 |  |
| 2026-11-04 12:03:32 | Thanamalwila (Kirindi Oya) | 1.55 | 🟢 Normal | -0.011 |  |
| 2026-11-04 12:06:41 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | -0.019 |  |
| 2026-11-04 12:03:10 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | -0.019 |  |
| 2026-11-04 12:05:16 | Holombuwa (Kelani Ganga) | 1.11 | 🟢 Normal | -0.029 |  |
| 2026-11-04 12:02:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.030 |  |
| 2026-11-04 12:02:21 | Galgamuwa (Mee Oya) | 0.98 | 🟢 Normal | -0.033 |  |
| 2026-11-04 12:09:41 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.042 |  |
| 2026-11-04 12:02:07 | Pitabeddara (Nilwala Ganga) | 1.85 | 🟢 Normal | -0.050 |  |
| 2026-11-04 12:02:07 | Peradeniya (Mahaweli Ganga) | 2.93 | 🟢 Normal | -0.056 |  |
| 2026-11-04 12:02:44 | Hanwella (Kelani Ganga) | 2.85 | 🟢 Normal | -0.061 |  |
| 2026-11-04 12:01:26 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | -0.069 |  |
| 2026-11-04 12:06:00 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.070 |  |
| 2026-11-04 12:04:45 | Thawalama (Gin Ganga) | 2.27 | 🟢 Normal | -0.072 |  |
| 2026-11-04 12:10:11 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.074 |  |
| 2026-11-04 12:04:03 | Glencourse (Kelani Ganga) | 10.61 | 🟢 Normal | -0.077 |  |
| 2026-11-04 12:01:59 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.091 |  |
| 2026-11-04 12:03:16 | Rathnapura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.112 |  |
| 2026-11-04 12:03:18 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | -0.128 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)