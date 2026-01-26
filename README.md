# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--27_03:34:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **56,662 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 03:34:30 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-27 03:18:04 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.093 |  |
| 2026-01-27 03:16:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.828 | 🔺 Rising |
| 2026-01-27 03:13:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-01-27 03:12:50 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-01-27 03:12:27 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-01-27 03:09:58 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 03:07:33 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-27 03:07:31 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-27 03:07:14 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-01-27 03:07:03 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:06:50 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-01-27 03:06:39 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:06:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:05:23 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.388 |  |
| 2026-01-27 03:05:21 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:05:13 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.093 |  |
| 2026-01-27 03:05:02 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:04:28 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 03:03:28 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-27 03:03:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 03:02:58 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:02:33 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:02:32 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-27 03:02:05 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 03:01:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-27 03:01:10 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:09 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.070 |  |
| 2026-01-27 03:01:07 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:00:58 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:00:57 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:00:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-27 03:07:33 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | 252.000 | 🔺 Rising |
| 2026-01-27 03:12:50 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 7.826 | 🔺 Rising |
| 2026-01-27 03:16:57 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.828 | 🔺 Rising |
| 2026-01-27 03:03:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-27 03:34:30 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-27 03:01:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-27 03:02:05 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-27 03:04:28 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-27 03:09:58 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-27 03:00:48 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-27 03:03:20 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 18:00:09 | Weraganthota (Mahaweli Ganga) | -2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:07 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:00:58 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:00:57 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:42:39 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:26 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:06:33 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 18:03:30 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-01-27 00:04:48 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:02:58 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:03:28 | Padiyathalawa (Maduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:06:39 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:02:33 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:07:03 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:01:10 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:05:21 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:32 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-27 01:01:49 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-27 02:02:14 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-27 03:13:08 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | -0.005 |  |
| 2026-01-27 03:07:14 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-01-27 03:06:50 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.010 |  |
| 2026-01-27 03:02:32 | Manampitiya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-01-26 18:01:38 | Thanthirimale (Malwathu Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-01-27 03:01:09 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -0.070 |  |
| 2026-01-27 03:18:04 | Magura (Kalu Ganga) | 0.82 | 🟢 Normal | -0.093 |  |
| 2026-01-27 03:05:23 | Peradeniya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.388 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)