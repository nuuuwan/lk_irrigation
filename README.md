# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_17:21:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,118 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 17:21:07 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:17:30 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:11:15 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:10:29 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:08:30 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:08:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 17:07:46 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-07-24 17:07:38 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:07:01 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:05:51 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.037 |  |
| 2026-07-24 17:05:29 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.041 |  |
| 2026-07-24 17:05:28 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:05:07 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:49 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:40 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:23 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:04:17 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:05 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:03:52 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:03:45 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:03:32 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-24 17:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:03:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:03:00 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:32 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:02:20 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:59 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.013 |  |
| 2026-07-24 17:01:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:01:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:28 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:13 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:00:38 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:00:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 16:41:20 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 17:01:58 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:01:13 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:03:13 | Deraniyagala (Kelani Ganga) | 0.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 16:02:42 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:04:05 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 17:08:07 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-24 17:00:38 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:00:30 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:03:52 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:48 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:32 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:05:28 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:11:15 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:17 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:17 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:47 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:40 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:01:28 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:28 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:02:20 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:07:38 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:07:01 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:21:07 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:08:30 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:05:07 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:10:29 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:17:30 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:49 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 17:04:23 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:03:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:02:21 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:03:45 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | -0.010 |  |
| 2026-07-24 17:03:32 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.011 |  |
| 2026-07-24 17:01:59 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | -0.013 |  |
| 2026-07-24 17:07:46 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.019 |  |
| 2026-07-24 17:05:51 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.037 |  |
| 2026-07-24 17:05:29 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.041 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)