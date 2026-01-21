# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_08:14:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,474 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 08:14:52 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:11:19 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-21 08:09:02 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:07:33 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.115 |  |
| 2026-01-21 08:06:48 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-01-21 08:06:12 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:05:12 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:04:37 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:04:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.069 |  |
| 2026-01-21 08:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-01-21 08:04:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.121 |  |
| 2026-01-21 08:04:06 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:54 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 08:03:49 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 08:03:45 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 08:03:30 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:21 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:19 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 08:03:08 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.147 |  |
| 2026-01-21 08:03:07 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:58 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:46 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.146 |  |
| 2026-01-21 08:02:27 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-01-21 08:02:12 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:11 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.061 |  |
| 2026-01-21 08:02:01 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-21 08:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-01-21 08:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:14 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 08:01:12 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:00:46 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 08:06:48 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.275 | 🔺 Rising |
| 2026-01-21 08:03:45 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-21 08:03:19 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 08:11:19 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-21 08:03:49 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-01-21 07:00:22 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 08:03:50 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 08:01:11 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:58 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:00:46 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:01 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:12 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:30 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:14:52 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:04:06 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:45 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:07 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:06:12 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:54 | Padiyathalawa (Maduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:03:21 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:09:02 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:04:37 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:02:11 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:54 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:05:12 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:12 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-21 07:16:20 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:01:17 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-21 08:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-01-21 08:01:14 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 08:01:37 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-01-21 08:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-01-21 08:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | -0.061 |  |
| 2026-01-21 08:04:35 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.069 |  |
| 2026-01-21 08:02:27 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-01-21 08:07:33 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.115 |  |
| 2026-01-21 08:04:11 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.121 |  |
| 2026-01-21 08:02:46 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | -0.146 |  |
| 2026-01-21 08:03:08 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)