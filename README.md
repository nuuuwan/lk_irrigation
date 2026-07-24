# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--24_23:11:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **215,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 23:11:51 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:10:24 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-07-24 23:10:12 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:08:31 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-07-24 23:08:18 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-24 23:07:56 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-24 23:06:50 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:06:32 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-07-24 23:05:20 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.072 |  |
| 2026-07-24 23:05:19 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:13 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:06 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:04:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-07-24 23:04:23 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:04:14 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-07-24 23:04:10 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-07-24 23:03:47 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:03:23 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.039 |  |
| 2026-07-24 23:03:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:03:09 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-24 23:02:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 23:02:42 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:26 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-07-24 23:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:01:12 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-24 23:01:09 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:00:53 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:00:41 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-24 22:52:35 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.070 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-24 23:01:12 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-07-24 23:03:09 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-07-24 23:07:56 | Putupaula (Kalu Ganga) | 0.51 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-07-24 23:08:18 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-07-24 23:02:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-24 23:00:53 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:42 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:01:52 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:03:16 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:03 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:08:47 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:04:23 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-24 22:07:59 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:06:50 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:11:51 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 22:03:15 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:06 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:03:47 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:00:41 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:13 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-24 18:03:00 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:10:12 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:05:19 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:01:09 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:02:26 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-24 21:10:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-24 23:06:32 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.009 |  |
| 2026-07-24 23:04:14 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-07-24 18:00:12 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.011 |  |
| 2026-07-24 23:02:00 | Nawalapitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-07-24 23:08:31 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-07-24 22:15:07 | Thalgahagoda (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.017 |  |
| 2026-07-24 23:04:10 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-07-24 23:10:24 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.038 |  |
| 2026-07-24 23:03:23 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.039 |  |
| 2026-07-24 23:04:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.061 |  |
| 2026-07-24 23:05:20 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)