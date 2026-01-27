# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_11:09:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 11:09:36 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:08:15 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:07:23 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:07:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:07:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:35 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:06:18 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:10 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:08 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.012 |  |
| 2026-01-27 11:05:46 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-01-27 11:05:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-27 11:05:26 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:04:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:04:41 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:04:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:04:03 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-01-27 11:03:50 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-01-27 11:03:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.041 |  |
| 2026-01-27 11:02:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:02:16 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 11:02:16 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:02:12 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-27 11:02:07 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.107 |  |
| 2026-01-27 11:02:03 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-01-27 11:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-01-27 11:02:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:01:52 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:01:01 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:00:49 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-27 10:18:04 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 11:03:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-01-27 11:05:32 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-27 11:02:12 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-27 11:02:16 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 11:07:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:06:21 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:05:26 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:04:42 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 11:02:16 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:10 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:00:49 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:01:52 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:07:23 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:01:01 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:02 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:04:41 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-27 10:07:58 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:03:16 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:02:01 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:04:03 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:02:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:10 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:18 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:08 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:07:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:06:35 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 11:08:15 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:04:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:09:36 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-27 11:06:04 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.012 |  |
| 2026-01-27 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.017 |  |
| 2026-01-27 11:03:50 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.030 |  |
| 2026-01-27 11:02:03 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | -0.039 |  |
| 2026-01-27 11:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.43 | 🟢 Normal | -0.041 |  |
| 2026-01-27 11:05:46 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.093 |  |
| 2026-01-27 11:02:02 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.097 |  |
| 2026-01-27 11:02:07 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.107 |  |
| 2026-01-27 10:00:43 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | -2.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)