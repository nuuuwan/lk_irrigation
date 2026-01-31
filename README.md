# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_11:37:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 11:37:47 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:15:10 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.034 |  |
| 2026-01-31 11:14:02 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 11:10:42 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 11:09:34 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:08:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:08:00 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-01-31 11:06:54 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:06:52 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:05:51 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:05:36 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-31 11:05:17 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.151 |  |
| 2026-01-31 11:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.031 |  |
| 2026-01-31 11:04:32 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:22 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:10 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:03:53 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:03:52 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-31 11:03:35 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:03:28 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:03:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:02:56 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-31 11:02:55 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:02:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-31 11:02:49 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:02:39 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-31 11:02:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.050 |  |
| 2026-01-31 11:02:18 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:02:17 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:02:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:02:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 11:01:58 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:01:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:01:23 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:01:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 11:00:58 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:00:56 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-01-31 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 11:00:56 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-01-31 11:02:50 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-01-31 11:02:11 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-31 11:02:56 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-31 11:03:52 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-31 11:10:42 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-31 11:02:39 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-31 11:01:22 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-31 11:02:18 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:03:14 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:01:31 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:02:14 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:01:58 | Weraganthota (Mahaweli Ganga) | -1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 11:14:02 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 11:02:17 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:09:34 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:06:54 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:03:35 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:03:28 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:06:52 | Ellagawa (Kalu Ganga) | 3.77 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:37:47 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:08:28 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:32 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:22 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:04:31 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:01:23 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-01-31 11:05:51 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:03:53 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:02:55 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:00:58 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:02:49 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-01-31 11:08:00 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-01-31 11:05:36 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-31 10:03:03 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | -0.021 |  |
| 2026-01-31 11:04:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.031 |  |
| 2026-01-31 11:15:10 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.034 |  |
| 2026-01-31 11:02:33 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.050 |  |
| 2026-01-31 11:05:17 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)