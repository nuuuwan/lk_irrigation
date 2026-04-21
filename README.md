# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_02:18:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,559 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 02:18:49 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:14:31 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:11:50 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:10:34 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-22 02:08:12 | Thanamalwila (Kirindi Oya) | 2.99 | 🟢 Normal | -0.271 |  |
| 2026-04-22 02:08:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-22 02:07:32 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-22 02:06:57 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.080 |  |
| 2026-04-22 02:04:59 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-22 02:04:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-04-22 02:03:37 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-04-22 02:03:15 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:02:53 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.039 |  |
| 2026-04-22 02:02:49 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 02:02:32 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-22 02:02:26 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:02:25 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:02:07 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-04-22 02:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:01:04 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.118 |  |
| 2026-04-22 02:01:04 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-22 02:00:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 01:17:26 | Kuda Oya (Kirindi Oya) | 2.94 | 🟢 Normal | 0.692 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 01:00:54 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-04-22 02:08:01 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-22 02:02:49 | Glencourse (Kelani Ganga) | 8.83 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 02:10:34 | Pitabeddara (Nilwala Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 01:02:21 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:01:56 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:18:49 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:23 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:03:15 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-22 01:02:51 | Dunamale (Aththanagalu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:06:57 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:02:25 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-22 02:14:31 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-22 01:23:20 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.008 |  |
| 2026-04-22 02:04:59 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-22 02:07:32 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-04-22 01:31:48 | Nawalapitiya (Mahaweli Ganga) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-04-22 00:04:19 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-04-22 02:02:32 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.020 |  |
| 2026-04-21 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-04-22 02:02:07 | Moraketiya (Walawe Ganga) | 1.51 | 🟢 Normal | -0.030 |  |
| 2026-04-22 01:04:11 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | -0.030 |  |
| 2026-04-22 02:01:04 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.030 |  |
| 2026-04-22 02:02:53 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.039 |  |
| 2026-04-22 01:00:53 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.040 |  |
| 2026-04-22 02:00:54 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-04-22 00:05:33 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.060 |  |
| 2026-04-22 02:04:23 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | -0.061 |  |
| 2026-04-22 02:03:37 | Hanwella (Kelani Ganga) | 0.90 | 🟢 Normal | -0.069 |  |
| 2026-04-22 02:06:23 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | -0.080 |  |
| 2026-04-22 01:02:01 | Ellagawa (Kalu Ganga) | 5.45 | 🟢 Normal | -0.100 |  |
| 2026-04-22 02:01:04 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.118 |  |
| 2026-04-22 02:08:12 | Thanamalwila (Kirindi Oya) | 2.99 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)