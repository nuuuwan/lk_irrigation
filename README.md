# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_03:15:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **71,569 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **49** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 03:15:09 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:15:08 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:15:06 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:14:41 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:14:40 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:14:38 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:14:37 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:11:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-13 03:11:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:11:14 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-02-13 03:11:00 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-02-13 03:10:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:09:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:08:22 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-02-13 03:07:55 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:07:53 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:07:52 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:07:51 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:07:50 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-13 03:07:18 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:06:28 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:06:03 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 03:06:02 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -180.000 |  |
| 2026-02-13 03:06:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:06:00 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | -180.000 |  |
| 2026-02-13 03:05:59 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | -180.000 |  |
| 2026-02-13 03:05:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:04:54 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.115 |  |
| 2026-02-13 03:04:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:04:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.078 |  |
| 2026-02-13 03:04:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-13 03:03:22 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:10 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:06 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:02:50 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.184 |  |
| 2026-02-13 03:02:42 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-13 03:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:01:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:01:27 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.041 |  |
| 2026-02-13 03:00:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:51 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:47 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:15 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 02:59:36 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-02-13 02:46:41 | Manampitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.041 |  |
| 2026-02-13 02:40:32 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 02:36:39 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 02:35:07 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.049 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 03:15:09 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:14:41 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-02-13 03:07:55 | Magura (Kalu Ganga) | 0.94 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-02-13 02:15:21 | Nawalapitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 3.789 | 🔺 Rising |
| 2026-02-13 03:11:00 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-02-13 03:08:22 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-02-13 03:07:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-02-13 03:04:08 | Ellagawa (Kalu Ganga) | 4.20 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-02-13 03:11:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-12 23:05:18 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-12 18:00:26 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-13 03:02:42 | Hanwella (Kelani Ganga) | 0.35 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-12 18:02:36 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 02:02:08 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-13 03:07:18 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:01:59 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:47 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:04:31 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:51 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:15 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:06 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:11:45 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-13 02:40:32 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:06:01 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:00:56 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:01:39 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:10 | Dunamale (Aththanagalu Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:05:34 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:03:22 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:09:00 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-12 18:01:34 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:10:09 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-13 03:11:14 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.025 |  |
| 2026-02-13 03:01:27 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.041 |  |
| 2026-02-13 01:35:21 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.044 |  |
| 2026-02-13 03:04:11 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.078 |  |
| 2026-02-13 03:04:54 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | -0.115 |  |
| 2026-02-13 03:02:50 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.184 |  |
| 2026-02-13 03:06:02 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)