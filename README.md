# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--21_16:14:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **51,795 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 16:14:10 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-21 16:11:38 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:08:48 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-01-21 16:07:43 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.005 |  |
| 2026-01-21 16:05:41 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:39 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:32 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:27 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:22 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |
| 2026-01-21 16:05:05 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:04:16 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-21 16:04:05 | Thawalama (Gin Ganga) | 0.81 | 🟢 Normal | -0.071 |  |
| 2026-01-21 16:04:04 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:59 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.069 |  |
| 2026-01-21 16:03:54 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:53 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:31 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:03:29 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:25 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-21 16:03:23 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:03:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:13 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-21 16:02:53 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 16:02:51 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-21 16:02:44 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:02:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-21 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 16:02:28 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:02:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-21 16:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:49 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:38 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:09 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-21 16:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:00:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:00:44 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 16:00:14 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-21 16:08:48 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.273 | 🔺 Rising |
| 2026-01-21 16:02:25 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-01-21 16:02:51 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-21 16:03:13 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-21 16:01:09 | Weraganthota (Mahaweli Ganga) | -1.90 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-01-21 16:02:37 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-01-21 16:02:53 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-21 16:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-21 16:00:44 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-21 16:14:10 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-21 16:07:43 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.005 |  |
| 2026-01-21 16:01:42 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:00:14 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:38 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:27 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:11:38 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:00:52 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:32 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:02:44 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:22 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:53 | Padiyathalawa (Maduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:54 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:02:28 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:29 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:39 | Badalgama (Maha Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:41 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:04:04 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:05:05 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:01:49 | Thanamalwila (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-21 16:03:23 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:01:09 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:03:31 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-21 16:04:16 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-01-21 16:03:25 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-21 16:03:59 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.069 |  |
| 2026-01-21 16:04:05 | Thawalama (Gin Ganga) | 0.81 | 🟢 Normal | -0.071 |  |
| 2026-01-21 16:05:22 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)