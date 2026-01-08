# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_21:12:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,307 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 21:12:49 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-08 21:09:36 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:07:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.098 |  |
| 2026-01-08 21:07:37 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-08 21:06:48 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.051 |  |
| 2026-01-08 21:06:33 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.134 |  |
| 2026-01-08 21:06:01 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:05:57 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 21:05:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:05:09 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:44 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-01-08 21:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:25 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:58 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:57 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-01-08 21:03:44 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.227 |  |
| 2026-01-08 21:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:03:24 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:18 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-08 21:03:13 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:07 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.078 |  |
| 2026-01-08 21:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:02:25 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:02:21 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:02:17 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:02:07 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-08 21:01:52 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:46 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:33 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-01-08 21:01:33 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:33 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:32 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:30 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:01:22 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-08 21:01:06 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:00:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.053 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 21:01:22 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-08 21:02:07 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-01-08 21:05:57 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 18:00:51 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-08 21:03:24 | Nakkala (Kumbukkan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:33 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:33 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:02:17 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:02:25 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:13 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:03:58 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:52 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:06:01 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:32 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:25 | Katharagama (Menik Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-08 20:05:24 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:05:09 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:09:36 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:01:46 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:05:29 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:04:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-01-08 21:12:49 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-01-08 21:02:21 | Wellawaya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-01-08 18:02:13 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:03:35 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:01:30 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:02:35 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-08 21:03:57 | Padiyathalawa (Maduru Oya) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-01-08 21:01:33 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.012 |  |
| 2026-01-08 21:03:18 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-08 21:07:37 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-01-08 18:07:05 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | -0.038 |  |
| 2026-01-08 21:06:48 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | -0.051 |  |
| 2026-01-08 21:00:52 | Dunamale (Aththanagalu Oya) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-01-08 21:04:44 | Panadugama (Nilwala Ganga) | 2.83 | 🟢 Normal | -0.075 |  |
| 2026-01-08 21:03:07 | Manampitiya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.078 |  |
| 2026-01-08 21:07:54 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.098 |  |
| 2026-01-08 21:06:33 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | -0.134 |  |
| 2026-01-08 21:03:44 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.227 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)