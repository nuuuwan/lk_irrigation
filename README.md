# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_12:10:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,379 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 12:10:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:09:54 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.035 |  |
| 2026-11-16 12:08:03 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:07:37 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:07:21 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.044 |  |
| 2026-11-16 12:06:46 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:06:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:06:05 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-11-16 12:05:59 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:05:44 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:05:36 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-11-16 12:05:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:05:15 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:04:40 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.089 |  |
| 2026-11-16 12:03:55 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:03:54 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:03:31 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-11-16 12:03:31 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:03:15 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 12:03:06 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.059 |  |
| 2026-11-16 12:02:59 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 12:02:49 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.039 |  |
| 2026-11-16 12:02:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:32 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.020 |  |
| 2026-11-16 12:02:24 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:02:23 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:14 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:14 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:02:04 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 12:01:57 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:51 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:49 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.021 |  |
| 2026-11-16 12:01:26 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:24 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:23 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-11-16 12:01:16 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:15 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 12:01:49 | Thalgahagoda (Nilwala Ganga) | 1.43 | 🟡 Alert | -0.021 |  |
| 2026-11-16 12:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 12:02:04 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 12:02:59 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 12:08:03 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:57 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:16 | Giriulla (Maha Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:51 | Horowpothana (Yan Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:03:55 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:26 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:06:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:03:54 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:33 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:10:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:05:44 | Badalgama (Maha Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:24 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:01:15 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:23 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:02:14 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 12:05:36 | Norwood (Kelani Ganga) | 1.00 | 🟢 Normal | -0.009 |  |
| 2026-11-16 12:05:15 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:03:31 | Ellagawa (Kalu Ganga) | 5.33 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:02:24 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:06:46 | Magura (Kalu Ganga) | 1.82 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:07:37 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:03:15 | Hanwella (Kelani Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:05:59 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:05:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:02:14 | Dunamale (Aththanagalu Oya) | 1.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 12:01:23 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | -0.020 |  |
| 2026-11-16 12:02:32 | Weraganthota (Mahaweli Ganga) | -1.94 | 🟢 Normal | -0.020 |  |
| 2026-11-16 12:03:31 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-11-16 12:06:05 | Panadugama (Nilwala Ganga) | 4.43 | 🟢 Normal | -0.021 |  |
| 2026-11-16 12:09:54 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.035 |  |
| 2026-11-16 12:02:49 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | -0.039 |  |
| 2026-11-16 12:07:21 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.044 |  |
| 2026-11-16 12:03:06 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | -0.059 |  |
| 2026-11-16 12:04:40 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)