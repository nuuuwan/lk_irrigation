# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_19:22:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,392 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 19:22:06 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:12:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:08:34 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:08:31 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.100 |  |
| 2026-01-26 19:08:09 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:07:53 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-01-26 19:07:47 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-26 19:07:22 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 19:07:13 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:06:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-26 19:06:20 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2026-01-26 19:06:06 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:06:00 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.020 |  |
| 2026-01-26 19:05:22 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-26 19:04:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:04:22 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:03:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:26 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:16 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:14 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-01-26 19:03:10 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 19:02:24 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:02:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:08 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:01:58 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 19:01:41 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-01-26 19:01:39 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:01:16 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:00:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:00:25 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 19:00:22 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:00:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 19:01:41 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-01-26 19:05:22 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-26 19:01:58 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-26 19:07:47 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-26 19:02:29 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 19:00:25 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 19:07:22 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:00:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:00:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:22:06 | Moragaswewa (Deduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:04:34 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:07:13 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:00:22 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:08 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:17 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:06:06 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:16 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:08:09 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:08:34 | Dunamale (Aththanagalu Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:10 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:52 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:01:39 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:12:24 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:02:47 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:03:26 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-26 19:07:53 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2026-01-26 19:04:22 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:01:16 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:02:24 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:08:31 | Ellagawa (Kalu Ganga) | 4.10 | 🟢 Normal | -0.010 |  |
| 2026-01-26 19:06:46 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-01-26 19:06:00 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.020 |  |
| 2026-01-26 19:03:14 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-01-26 19:06:20 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.036 |  |
| 2026-01-26 19:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)