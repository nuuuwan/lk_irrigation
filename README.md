# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_13:23:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,996 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 13:23:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-08 13:13:37 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.215 |  |
| 2026-01-08 13:12:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 13:11:32 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:10:54 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:10:23 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-01-08 13:09:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:08:02 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:06:06 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:05:41 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 13:05:06 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 13:05:01 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-01-08 13:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-08 13:04:26 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.049 |  |
| 2026-01-08 13:04:12 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:04:08 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-01-08 13:04:05 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:04:02 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:59 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:38 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 13:03:35 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-08 13:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:11 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:03:10 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:10 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:03:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.006 |  |
| 2026-01-08 13:02:45 | Manampitiya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 13:02:43 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:02:38 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:01:49 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:01:22 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-08 13:01:14 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.041 |  |
| 2026-01-08 13:00:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:00:25 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:00:11 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 13:01:22 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-08 13:05:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-08 13:03:33 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-08 13:05:06 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-08 13:23:21 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-08 13:12:46 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 13:00:11 | Weraganthota (Mahaweli Ganga) | -1.23 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-08 13:02:45 | Manampitiya (Mahaweli Ganga) | 2.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-08 13:03:38 | Kithulgala (Kelani Ganga) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 13:05:41 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 13:00:25 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:01:14 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:26 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:01:49 | Yaka Wewa (Ma Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:10 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:04:05 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:11:32 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:35 | Padiyathalawa (Maduru Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:06:06 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:00:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:59 | Thaldena (Mahaweli Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:02:38 | Katharagama (Menik Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:09:59 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:04:02 | Rathnapura (Kalu Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:04:12 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:02:43 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-08 13:03:01 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.006 |  |
| 2026-01-08 11:22:48 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.009 |  |
| 2026-01-08 13:04:08 | Horowpothana (Yan Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-01-08 13:08:02 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:10:54 | Dunamale (Aththanagalu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:03:10 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:03:11 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | -0.010 |  |
| 2026-01-08 13:10:23 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-01-08 13:05:01 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.019 |  |
| 2026-01-08 12:02:16 | Baddegama (Gin Ganga) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-01-08 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.041 |  |
| 2026-01-08 13:04:26 | Peradeniya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.049 |  |
| 2026-01-08 13:13:37 | Panadugama (Nilwala Ganga) | 3.41 | 🟢 Normal | -0.215 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)