# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_21:08:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 21:08:10 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-05 21:07:49 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:07:04 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:06:39 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-01-05 21:06:26 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 21:06:14 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:05:49 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:05:43 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:04:52 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-05 21:04:51 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:04:28 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-05 21:04:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:04:07 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-05 21:03:55 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:03:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 21:03:38 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-05 21:03:18 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:08 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 21:03:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 21:03:06 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |
| 2026-01-05 21:03:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:02:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 21:02:36 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:02:31 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:02:20 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:01:59 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-01-05 21:01:49 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:01:08 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:00:56 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 21:00:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-05 20:17:13 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-05 20:13:59 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-01-05 20:11:18 | Urawa (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.046 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 20:02:35 | Peradeniya (Mahaweli Ganga) | 2.43 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-01-05 21:08:10 | Padiyathalawa (Maduru Oya) | 3.00 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-01-05 21:04:28 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-05 18:04:03 | Weraganthota (Mahaweli Ganga) | -1.35 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-01-05 21:04:07 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-05 21:06:26 | Pitabeddara (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-05 21:03:38 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-05 21:03:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 21:03:08 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-05 21:00:56 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-05 21:04:52 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-05 21:03:08 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-05 21:02:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 21:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:02 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:02:31 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-05 18:12:56 | Galgamuwa (Mee Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:05:49 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:06:14 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:07:04 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:01:49 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:18 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:01:08 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:05:43 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:07:49 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 20:07:41 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:03:06 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:04:51 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-05 21:04:07 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:02:36 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:03:55 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:00:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-05 21:02:20 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-01-05 18:04:30 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-01-05 21:01:59 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-01-05 20:10:27 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.040 |  |
| 2026-01-05 20:11:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.045 |  |
| 2026-01-05 21:06:39 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.061 |  |
| 2026-01-05 21:03:05 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.062 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)