# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_04:29:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,803 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 04:29:42 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.003 |  |
| 2026-01-26 04:26:39 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:22:24 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:18:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-26 04:11:47 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-01-26 04:10:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:10:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-26 04:07:51 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:07:37 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:07:16 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:06:47 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:05:58 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-26 04:05:42 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-26 04:05:10 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 04:03:49 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-26 04:02:49 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-26 04:02:35 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:02:03 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:01:59 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.138 |  |
| 2026-01-26 04:01:25 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-26 04:01:06 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-26 04:00:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.054 |  |
| 2026-01-26 04:00:35 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 03:11:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | 0.277 | 🔺 Rising |
| 2026-01-26 04:05:58 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-01-26 04:01:06 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-26 04:10:37 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-26 00:04:17 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-25 18:00:27 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-26 04:05:42 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-01-26 03:00:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-26 04:05:10 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 04:18:28 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-26 04:22:24 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:10:53 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:02:03 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:06:47 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-25 18:04:15 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 03:24:44 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 03:16:03 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 03:02:18 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:02:35 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:02:49 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:07:51 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 03:07:08 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:07:37 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 03:01:47 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-26 02:10:49 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:37 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:07:16 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:26:39 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:00:35 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 04:29:42 | Horowpothana (Yan Oya) | 1.38 | 🟢 Normal | -0.003 |  |
| 2026-01-26 03:05:40 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | -0.007 |  |
| 2026-01-26 04:11:47 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.009 |  |
| 2026-01-26 04:03:49 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-01-26 04:02:43 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-01-26 04:01:25 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-26 02:02:14 | Thanamalwila (Kirindi Oya) | 0.59 | 🟢 Normal | -0.012 |  |
| 2026-01-25 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.020 |  |
| 2026-01-26 04:00:41 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.054 |  |
| 2026-01-26 04:01:59 | Peradeniya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)