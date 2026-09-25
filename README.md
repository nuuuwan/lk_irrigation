# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_02:33:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,079 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 02:33:08 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-26 02:29:35 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-26 02:28:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:15:34 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:11:52 | Baddegama (Gin Ganga) | 4.78 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-26 02:10:41 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 02:08:36 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | -0.045 |  |
| 2026-09-26 02:06:05 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:06:04 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:05:06 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 02:04:21 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | -0.088 |  |
| 2026-09-26 02:04:20 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.043 |  |
| 2026-09-26 02:04:11 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:04:09 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-09-26 02:04:02 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:03:58 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:03:38 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.120 |  |
| 2026-09-26 02:03:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:02:56 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:42 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:21 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 02:02:07 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-26 02:01:27 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:01:24 | Glencourse (Kelani Ganga) | 13.90 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:01:13 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 02:00:50 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-26 02:00:32 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 02:11:52 | Baddegama (Gin Ganga) | 4.78 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-26 01:28:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.09 | 🟠 Minor Flood | 0.007 | 🔺 Rising |
| 2026-09-26 00:17:35 | Thalgahagoda (Nilwala Ganga) | 1.93 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 02:05:06 | Panadugama (Nilwala Ganga) | 6.19 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 00:03:21 | Magura (Kalu Ganga) | 4.72 | 🟡 Alert | -0.034 |  |
| 2026-09-26 01:02:47 | Rathnapura (Kalu Ganga) | 5.65 | 🟡 Alert | -0.083 |  |
| 2026-09-26 02:00:50 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-26 02:01:13 | Peradeniya (Mahaweli Ganga) | 4.38 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-26 02:29:35 | Nagalagam Street (Kelani Ganga) | 1.01 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-26 02:02:07 | Ellagawa (Kalu Ganga) | 8.98 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-26 02:02:09 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 02:10:41 | Putupaula (Kalu Ganga) | 2.85 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 01:00:21 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:00:32 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:28:49 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:13 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:04:02 | Hanwella (Kelani Ganga) | 5.88 | 🟢 Normal | 0.000 |  |
| 2026-09-26 00:58:56 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:01:24 | Glencourse (Kelani Ganga) | 13.90 | 🟢 Normal | 0.000 |  |
| 2026-09-26 01:02:18 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:03:32 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:15:34 | Dunamale (Aththanagalu Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:06:05 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:04:11 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 18:01:42 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 02:02:21 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:01:27 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:56 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:02:42 | Badalgama (Maha Oya) | 3.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:03:58 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-09-26 02:33:08 | Pitabeddara (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.011 |  |
| 2026-09-25 18:02:19 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.020 |  |
| 2026-09-26 02:04:09 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-09-26 02:04:20 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.043 |  |
| 2026-09-26 02:08:36 | Thawalama (Gin Ganga) | 3.31 | 🟢 Normal | -0.045 |  |
| 2026-09-26 02:04:21 | Kithulgala (Kelani Ganga) | 2.78 | 🟢 Normal | -0.088 |  |
| 2026-09-26 02:03:38 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.120 |  |
| 2026-09-26 01:05:38 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.923 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)