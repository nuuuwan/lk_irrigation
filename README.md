# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_18:11:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,185 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 18:11:12 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:10:09 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.037 |  |
| 2026-04-22 18:09:31 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.036 |  |
| 2026-04-22 18:09:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:09:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:08:27 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-22 18:08:17 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:07:47 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:06:36 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:05:54 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.037 |  |
| 2026-04-22 18:05:44 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:04:59 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:04:16 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:03:49 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-04-22 18:03:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:03:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:03:12 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-04-22 18:03:09 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-22 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:59 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:46 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 18:02:22 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.013 |  |
| 2026-04-22 18:02:20 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-22 18:02:19 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.152 |  |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:02:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:01:59 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.071 |  |
| 2026-04-22 18:01:11 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-04-22 18:01:08 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:01:01 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-04-22 18:00:51 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 17:18:48 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 18:01:01 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | 0.541 | 🔺 Rising |
| 2026-04-22 17:00:52 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-22 17:05:06 | Kuda Oya (Kirindi Oya) | 1.68 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-22 18:02:46 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 18:00:51 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:01:08 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:00:09 | Nawalapitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:08:17 | Katharagama (Menik Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 18:02:07 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:11:12 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-22 17:11:05 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:59 | Hanwella (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:09:26 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:06:36 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:03:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:04:59 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:07:47 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:02:57 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:09:19 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-04-22 18:08:27 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-22 18:04:16 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:03:47 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 17:00:16 | Thalgahagoda (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.013 |  |
| 2026-04-22 18:02:22 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.013 |  |
| 2026-04-22 18:03:09 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-22 18:02:20 | Thanamalwila (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-04-22 18:03:49 | Badalgama (Maha Oya) | 2.44 | 🟢 Normal | -0.029 |  |
| 2026-04-22 18:03:12 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | -0.030 |  |
| 2026-04-22 18:09:31 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | -0.036 |  |
| 2026-04-22 18:05:54 | Ellagawa (Kalu Ganga) | 4.66 | 🟢 Normal | -0.037 |  |
| 2026-04-22 18:10:09 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.037 |  |
| 2026-04-22 18:01:11 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.042 |  |
| 2026-04-22 18:01:59 | Norwood (Kelani Ganga) | 1.30 | 🟢 Normal | -0.071 |  |
| 2026-04-22 18:02:19 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)