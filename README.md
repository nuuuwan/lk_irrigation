# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_19:18:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,560 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 19:18:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.024 |  |
| 2026-01-05 19:15:22 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.016 |  |
| 2026-01-05 19:14:47 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:14:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:13:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-05 19:11:32 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:10:19 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:09:28 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:08:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:07:35 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:07:07 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-05 19:06:15 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-05 19:06:06 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:06:00 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:05:57 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 19:05:47 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2026-01-05 19:05:29 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:05:26 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-01-05 19:05:17 | Padiyathalawa (Maduru Oya) | 1.95 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-05 19:05:04 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:05:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 19:04:57 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:04:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.059 |  |
| 2026-01-05 19:03:56 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-01-05 19:03:46 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:03:31 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-01-05 19:02:52 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-05 19:02:48 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:02:00 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-05 19:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:01:13 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:01:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:00:52 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:00:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-01-05 19:00:37 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 19:00:27 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 19:05:26 | Peradeniya (Mahaweli Ganga) | 2.22 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 19:05:17 | Padiyathalawa (Maduru Oya) | 1.95 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-05 19:06:15 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-01-05 19:02:52 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-05 19:13:21 | Thaldena (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-01-05 19:05:03 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 19:05:57 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 19:00:37 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 19:00:27 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:14:47 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:05:04 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:00:52 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:06:00 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:14:02 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:06:06 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:04:57 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:11:32 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:07:35 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:01:11 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:02:48 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:05:29 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:08:42 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:09:28 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:01:13 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:10:19 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:03:46 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 19:07:07 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-05 19:02:00 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 19:15:22 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.016 |  |
| 2026-01-05 19:03:31 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.020 |  |
| 2026-01-05 19:00:47 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-01-05 19:18:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.024 |  |
| 2026-01-05 19:05:47 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.028 |  |
| 2026-01-05 19:03:56 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.031 |  |
| 2026-01-05 19:04:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)