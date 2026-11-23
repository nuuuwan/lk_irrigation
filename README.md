# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--23_08:32:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **323,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 08:32:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-23 08:16:12 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:09:19 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:08:36 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-11-23 08:08:26 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:07:14 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:05:59 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-23 08:05:26 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-23 08:05:23 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.071 |  |
| 2026-11-23 08:05:04 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-23 08:04:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:03:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:03:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:03:45 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-11-23 08:03:41 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.052 |  |
| 2026-11-23 08:03:18 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:03:11 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-23 08:03:10 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-23 08:03:06 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.289 |  |
| 2026-11-23 08:03:02 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.058 |  |
| 2026-11-23 08:02:52 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:02:47 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:02:19 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.254 |  |
| 2026-11-23 08:02:18 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 08:02:18 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.031 |  |
| 2026-11-23 08:02:13 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:02:13 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-23 08:01:55 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:34 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.401 |  |
| 2026-11-23 08:01:30 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-23 08:01:28 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 08:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:01:27 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:23 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:00:54 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:00:38 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-11-23 08:00:10 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-23 08:02:13 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-11-23 08:01:28 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-23 08:05:26 | Deraniyagala (Kelani Ganga) | 0.54 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-23 08:05:59 | Glencourse (Kelani Ganga) | 9.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-11-23 08:32:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-23 08:02:18 | Baddegama (Gin Ganga) | 1.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-23 08:00:10 | Weraganthota (Mahaweli Ganga) | -2.04 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:27 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:37 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:03:18 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:23 | Horowpothana (Yan Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:04:30 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:01:55 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:02:52 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:03:57 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:08:26 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:16:12 | Urawa (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:07:14 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:00:54 | Thanamalwila (Kirindi Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-11-23 08:08:36 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-11-23 08:02:13 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:09:19 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:02:47 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:03:55 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-11-23 08:01:30 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-23 08:05:04 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.011 |  |
| 2026-11-23 08:00:38 | Nagalagam Street (Kelani Ganga) | 0.29 | 🟢 Normal | -0.016 |  |
| 2026-11-23 08:03:11 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.020 |  |
| 2026-11-23 08:03:10 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-23 08:02:18 | Moragaswewa (Deduru Oya) | 1.38 | 🟢 Normal | -0.031 |  |
| 2026-11-23 08:03:45 | Panadugama (Nilwala Ganga) | 4.01 | 🟢 Normal | -0.034 |  |
| 2026-11-23 08:03:41 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.052 |  |
| 2026-11-23 08:03:02 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.058 |  |
| 2026-11-23 08:05:23 | Rathnapura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.071 |  |
| 2026-11-23 08:02:19 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | -0.254 |  |
| 2026-11-23 08:03:06 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.289 |  |
| 2026-11-23 08:01:34 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | -0.401 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)