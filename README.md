# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--22_14:28:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **52,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 14:28:30 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:22:58 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:22:47 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:18:31 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:17:54 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:17:04 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:14:39 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:14:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-01-22 14:10:39 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:10:35 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:07:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:07:02 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:06:25 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:05:07 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:04:40 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:51 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-22 14:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:36 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-22 14:03:34 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:29 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:03:23 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:02 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-22 14:02:54 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:02:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.058 |  |
| 2026-01-22 14:02:50 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:02:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.048 |  |
| 2026-01-22 14:02:33 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:02:29 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:02:27 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:02:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-22 14:01:53 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:50 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:01:49 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:45 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:39 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:17 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 14:01:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:53 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:48 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:06 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-22 14:03:02 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-01-22 14:02:06 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-01-22 14:01:17 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-22 14:01:39 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:06 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:14:39 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:00 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:45 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:10:39 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:48 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:10:35 | Magura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:07:02 | Pitabeddara (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:23 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:42 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:10 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:01:53 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:00:53 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:02:54 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:17:04 | Siyambalanduwa (Heda Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:04:40 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:05:07 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:15 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:06:25 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:02:33 | Thanthirimale (Malwathu Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:22:47 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:18:31 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:22:58 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:03:12 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:28:30 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-22 14:14:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.009 |  |
| 2026-01-22 14:07:11 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:02:50 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:01:50 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:03:29 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:02:27 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-01-22 14:03:51 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-01-22 14:03:36 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-22 14:02:40 | Weraganthota (Mahaweli Ganga) | -1.87 | 🟢 Normal | -0.048 |  |
| 2026-01-22 14:02:54 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.058 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)