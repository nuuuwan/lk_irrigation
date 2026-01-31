# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_19:50:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **60,884 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 19:50:11 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:18:33 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-31 19:16:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-31 19:10:46 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 19:10:40 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:08:21 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:06:18 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:06:04 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.046 |  |
| 2026-01-31 19:05:56 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.071 |  |
| 2026-01-31 19:05:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-01-31 19:05:31 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 19:05:11 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:05:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:04:43 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 19:04:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:04:08 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:03:54 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:03:47 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-01-31 19:03:34 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:02 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:53 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:51 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:31 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 19:02:24 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:20 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:02 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 19:01:54 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 19:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:01:49 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-31 19:01:45 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:01:26 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-31 19:01:09 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 19:16:00 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-31 19:01:49 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-31 19:01:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.28 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-31 19:05:31 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-31 19:18:33 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-31 19:02:27 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-31 19:01:26 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-31 19:01:54 | Manampitiya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 19:02:02 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 19:04:43 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 19:10:46 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 19:01:45 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:53 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:50:11 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:02 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:01:51 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:10:40 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:06 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:34 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:01:09 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:04:22 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:51 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:24 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:08:21 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:02:20 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:05:07 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:13:08 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:05:11 | Thanamalwila (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-31 19:03:54 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:06:18 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:04:08 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-31 19:05:38 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-01-31 19:03:47 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.040 |  |
| 2026-01-31 19:06:04 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.046 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-01-31 19:05:56 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)