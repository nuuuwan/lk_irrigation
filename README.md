# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--24_05:17:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,038 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 05:17:37 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.017 |  |
| 2026-01-24 05:12:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:10:41 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:10:18 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-01-24 05:08:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-24 05:07:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:07:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:07:12 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-24 05:06:42 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.013 |  |
| 2026-01-24 05:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-24 05:06:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 05:06:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -15.652 |  |
| 2026-01-24 05:05:58 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -15.652 |  |
| 2026-01-24 05:04:29 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:57 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:03:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:03:53 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-01-24 05:03:47 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:26 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:23 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-01-24 05:03:08 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:52 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-24 05:02:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:22 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:20 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-24 05:01:58 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-24 05:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:01:15 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:01:03 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:00:56 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.499 |  |
| 2026-01-24 05:00:13 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-24 05:03:53 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 2.400 | 🔺 Rising |
| 2026-01-24 05:02:11 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-24 05:07:12 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-24 05:06:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-01-24 05:02:52 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-24 05:08:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-24 04:11:48 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 05:06:26 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 04:02:59 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.002 |  |
| 2026-01-24 05:00:13 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-24 04:00:54 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:01:41 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:22 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:20 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:08 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-23 18:03:40 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:01:03 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:02:41 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:04:29 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:01:15 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:07:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:57 | Padiyathalawa (Maduru Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:07:58 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-24 04:04:33 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:03:47 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:12:37 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-01-24 03:15:28 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-24 05:10:18 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-01-24 05:03:53 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:10:41 | Magura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-24 05:03:56 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-01-23 18:01:34 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-01-24 04:08:51 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.012 |  |
| 2026-01-24 05:06:42 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | -0.013 |  |
| 2026-01-24 05:17:37 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | -0.017 |  |
| 2026-01-24 05:01:58 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-23 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.21 | 🟢 Normal | -0.081 |  |
| 2026-01-24 05:00:56 | Manampitiya (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.499 |  |
| 2026-01-24 05:06:21 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -15.652 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)