# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--27_13:05:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **136,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 13:05:38 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:05:31 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-04-27 13:05:08 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:04:56 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-04-27 13:04:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-04-27 13:04:35 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:04:20 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:04:19 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-27 13:04:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:03:46 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-27 13:03:01 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 13:02:47 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-27 13:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2026-04-27 13:02:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 13:02:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 13:02:09 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:01:41 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.214 |  |
| 2026-04-27 13:01:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 13:01:32 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:01:31 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:01:30 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:01:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:01:23 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 13:00:58 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-27 12:12:40 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | 0.035 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-27 13:04:56 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-04-27 12:08:31 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-27 13:04:19 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-04-27 13:01:39 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-27 12:02:11 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 13:01:23 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-27 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-27 13:03:01 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-27 12:03:43 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 13:02:32 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 12:03:44 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-27 13:01:26 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:04:18 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:26 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:02:41 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:05:08 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:03:02 | Norwood (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:04:20 | Baddegama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:05:38 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:01:31 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:12:10 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-04-27 12:01:46 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:02:09 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-27 13:02:47 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-04-27 13:03:46 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-04-27 13:00:58 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-27 12:02:50 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-04-27 13:04:20 | Hanwella (Kelani Ganga) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:04:35 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:01:30 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:02:17 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.020 |  |
| 2026-04-27 12:05:16 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-04-27 13:05:31 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.028 |  |
| 2026-04-27 12:03:12 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-04-27 12:06:04 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.035 |  |
| 2026-04-27 13:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | -0.050 |  |
| 2026-04-27 13:04:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-04-27 12:08:01 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.093 |  |
| 2026-04-27 13:01:41 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)