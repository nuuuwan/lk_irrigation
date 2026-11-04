# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--04_15:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 15:13:25 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.088 |  |
| 2026-11-04 15:11:02 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-11-04 15:08:19 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.082 |  |
| 2026-11-04 15:07:52 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:07:07 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.146 |  |
| 2026-11-04 15:06:24 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-11-04 15:06:09 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:05:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-11-04 15:05:41 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:05:32 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 15:05:25 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 15:05:10 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:04:18 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-11-04 15:04:06 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-11-04 15:03:56 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-04 15:03:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.021 |  |
| 2026-11-04 15:03:18 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-11-04 15:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | -0.030 |  |
| 2026-11-04 15:03:14 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.039 |  |
| 2026-11-04 15:03:13 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.049 |  |
| 2026-11-04 15:03:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:02:56 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-04 15:02:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:02:38 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:02:36 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.083 |  |
| 2026-11-04 15:02:30 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:02:27 | Moragaswewa (Deduru Oya) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:02:12 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.160 |  |
| 2026-11-04 15:02:00 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:01:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:01:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:00 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-04 15:00:34 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.113 |  |
| 2026-11-04 15:00:18 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.060 |  |
| 2026-11-04 15:00:16 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-04 15:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.03 | 🟡 Alert | -0.030 |  |
| 2026-11-04 15:04:18 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-11-04 15:11:02 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-11-04 15:03:56 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-04 15:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-04 15:05:32 | Moraketiya (Walawe Ganga) | 1.93 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-04 15:05:25 | Manampitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-04 15:01:31 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:07:52 | Baddegama (Gin Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:03:10 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:05:10 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-11-04 14:00:43 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:07 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:02:30 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:01:00 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-11-04 15:06:24 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2026-11-04 15:02:38 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:02:00 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:00:16 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:01:45 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:02:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-04 15:02:56 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-04 15:05:41 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:02:27 | Moragaswewa (Deduru Oya) | 4.36 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:06:09 | Pitabeddara (Nilwala Ganga) | 1.78 | 🟢 Normal | -0.020 |  |
| 2026-11-04 15:03:22 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.021 |  |
| 2026-11-04 15:03:14 | Dunamale (Aththanagalu Oya) | 2.30 | 🟢 Normal | -0.039 |  |
| 2026-11-04 15:03:18 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | -0.041 |  |
| 2026-11-04 14:14:21 | Panadugama (Nilwala Ganga) | 4.33 | 🟢 Normal | -0.044 |  |
| 2026-11-04 15:03:13 | Ellagawa (Kalu Ganga) | 6.73 | 🟢 Normal | -0.049 |  |
| 2026-11-04 15:05:48 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.060 |  |
| 2026-11-04 15:00:18 | Horowpothana (Yan Oya) | 2.51 | 🟢 Normal | -0.060 |  |
| 2026-11-04 15:04:06 | Hanwella (Kelani Ganga) | 2.64 | 🟢 Normal | -0.069 |  |
| 2026-11-04 15:08:19 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | -0.082 |  |
| 2026-11-04 15:02:36 | Badalgama (Maha Oya) | 3.76 | 🟢 Normal | -0.083 |  |
| 2026-11-04 15:13:25 | Rathnapura (Kalu Ganga) | 2.75 | 🟢 Normal | -0.088 |  |
| 2026-11-04 15:00:34 | Weraganthota (Mahaweli Ganga) | -2.91 | 🟢 Normal | -0.113 |  |
| 2026-11-04 15:07:07 | Magura (Kalu Ganga) | 2.54 | 🟢 Normal | -0.146 |  |
| 2026-11-04 15:02:12 | Giriulla (Maha Oya) | 2.58 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)