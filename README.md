# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--23_11:18:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 11:18:14 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-09-23 11:09:28 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.011 |  |
| 2026-09-23 11:08:53 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:08:32 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.010 |  |
| 2026-09-23 11:07:10 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 11:06:53 | Baddegama (Gin Ganga) | 3.79 | 🟡 Alert | -0.020 |  |
| 2026-09-23 11:06:31 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.032 |  |
| 2026-09-23 11:06:00 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.012 |  |
| 2026-09-23 11:05:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:05:50 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-23 11:05:31 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.023 |  |
| 2026-09-23 11:05:20 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-23 11:05:15 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:05:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:04:31 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.178 |  |
| 2026-09-23 11:04:27 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:04:20 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:04:01 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:03:56 | Ellagawa (Kalu Ganga) | 8.09 | 🟢 Normal | -0.062 |  |
| 2026-09-23 11:03:22 | Hanwella (Kelani Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:03:05 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 11:02:53 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.313 |  |
| 2026-09-23 11:02:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:31 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:02:26 | Glencourse (Kelani Ganga) | 12.82 | 🟢 Normal | -0.021 |  |
| 2026-09-23 11:02:24 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 11:02:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:12 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:51 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:38 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 11:01:36 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:26 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-23 11:01:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:00:28 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:00:12 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 10:59:30 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-23 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-23 11:08:32 | Magura (Kalu Ganga) | 4.04 | 🟡 Alert | -0.010 |  |
| 2026-09-23 11:06:53 | Baddegama (Gin Ganga) | 3.79 | 🟡 Alert | -0.020 |  |
| 2026-09-23 11:01:26 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-23 11:05:50 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-23 11:05:20 | Urawa (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-23 11:03:05 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 11:01:38 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-23 11:07:10 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-23 11:00:12 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:31 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:05:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:08:53 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:35 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:24 | Giriulla (Maha Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:53 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:36 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:12 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:51 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:01:18 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:52 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:04:27 | Thanthirimale (Malwathu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:00:28 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:02:12 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-23 11:18:14 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.009 |  |
| 2026-09-23 11:03:22 | Hanwella (Kelani Ganga) | 4.82 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:05:13 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:02:31 | Putupaula (Kalu Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-09-23 11:09:28 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.011 |  |
| 2026-09-23 11:06:00 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.012 |  |
| 2026-09-23 11:05:15 | Badalgama (Maha Oya) | 2.69 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:04:01 | Deraniyagala (Kelani Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:04:20 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.020 |  |
| 2026-09-23 11:02:26 | Glencourse (Kelani Ganga) | 12.82 | 🟢 Normal | -0.021 |  |
| 2026-09-23 11:05:31 | Thalgahagoda (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.023 |  |
| 2026-09-23 11:06:31 | Rathnapura (Kalu Ganga) | 3.84 | 🟢 Normal | -0.032 |  |
| 2026-09-23 11:03:56 | Ellagawa (Kalu Ganga) | 8.09 | 🟢 Normal | -0.062 |  |
| 2026-09-23 11:04:31 | Kithulgala (Kelani Ganga) | 2.14 | 🟢 Normal | -0.178 |  |
| 2026-09-23 11:02:53 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | -0.313 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)