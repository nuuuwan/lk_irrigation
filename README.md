# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--28_03:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **57,566 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 03:15:48 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:14:43 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.034 |  |
| 2026-01-28 03:14:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:14:26 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:13:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.008 |  |
| 2026-01-28 03:11:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:11:32 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-28 03:11:01 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:10:11 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:08:18 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:06:35 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 03:06:19 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:05:49 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:04:25 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:04:17 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.009 |  |
| 2026-01-28 03:04:05 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:03:56 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-28 03:03:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-28 03:02:58 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-01-28 03:02:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:46 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:32 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:03 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:01:34 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:01:30 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.258 |  |
| 2026-01-28 03:01:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:01:27 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:57 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:36 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-28 02:44:15 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-28 03:11:32 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-28 02:26:41 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-28 03:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-28 02:01:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-27 18:01:37 | Weraganthota (Mahaweli Ganga) | -2.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-28 03:06:35 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-28 02:08:56 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-28 03:01:30 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:01:34 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:47 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:57 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:03 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:04:05 | Giriulla (Maha Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:11:01 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:06:19 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:04:25 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:08:18 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:05:49 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:03:52 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:01:27 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:00:38 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:11:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:48 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:02:32 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:14:35 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:15:48 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:14:26 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-28 03:10:11 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-28 02:07:58 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.005 |  |
| 2026-01-28 03:13:16 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.008 |  |
| 2026-01-28 03:04:17 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.009 |  |
| 2026-01-28 01:04:06 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-27 17:06:09 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-28 03:03:56 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-01-27 18:02:53 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-01-28 03:02:58 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.029 |  |
| 2026-01-28 03:14:43 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.034 |  |
| 2026-01-28 03:01:30 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.258 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)