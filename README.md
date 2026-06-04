# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_12:18:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 12:18:10 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:13:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:13:23 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 12:13:06 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 12:12:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-06-04 12:11:38 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:08:48 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:08:47 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:08:09 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:07:36 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:07:35 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:06:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:06:44 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:06:09 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 12:05:50 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-04 12:05:50 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 12:05:19 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 12:05:11 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 12:04:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-06-04 12:04:35 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-04 12:04:24 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:20 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 12:04:18 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:03:43 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.039 |  |
| 2026-06-04 12:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:03:23 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:03:16 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 12:02:42 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:48 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:38 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 12:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:31 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 12:01:27 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:09 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:00:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:00:18 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:00:17 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:00:08 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.112 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 12:04:45 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.347 | 🔺 Rising |
| 2026-06-04 12:00:08 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-06-04 12:01:31 | Ellagawa (Kalu Ganga) | 6.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-04 12:04:35 | Hanwella (Kelani Ganga) | 2.44 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-06-04 12:05:50 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-04 12:01:38 | Nawalapitiya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 12:03:16 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 12:05:19 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-04 12:06:09 | Rathnapura (Kalu Ganga) | 2.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 12:13:06 | Magura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 12:04:20 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 12:04:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 12:05:50 | Baddegama (Gin Ganga) | 1.83 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 12:13:23 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 12:00:18 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:08:09 | Moragaswewa (Deduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:27 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:05:11 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:24 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:18:10 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:07:35 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:09 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:38 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:02:42 | Dunamale (Aththanagalu Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:06:44 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:08:47 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:06:47 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:05 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:13:29 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:01:48 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:04:18 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | 0.000 |  |
| 2026-06-04 12:12:28 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-06-04 12:03:23 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:00:17 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:00:48 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-06-04 12:03:43 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.039 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)