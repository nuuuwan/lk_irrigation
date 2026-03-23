# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--23_18:26:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,396 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **47** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 18:26:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-23 18:26:02 | Thawalama (Gin Ganga) | 1.11 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-23 18:26:00 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-23 18:25:59 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-23 18:25:40 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-03-23 18:23:41 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:19:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-23 18:16:35 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-03-23 18:11:16 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:11:13 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:11:09 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:11:01 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:10:56 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:08:31 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:07:12 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-23 18:06:45 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:06:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:05:42 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 18:04:53 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:04:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-03-23 18:04:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:04:05 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:46 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:20 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:19 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 18:03:09 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:00 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:52 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:43 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-23 18:02:40 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:36 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:05 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-23 18:01:52 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:01:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-03-23 18:01:28 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-23 18:01:26 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-03-23 18:01:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 18:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |
| 2026-03-23 18:00:33 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-23 18:26:03 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-23 18:02:36 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-03-23 18:02:41 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-03-23 18:02:05 | Manampitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-23 18:07:12 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-23 18:19:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-23 18:03:19 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 18:01:08 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-23 18:05:42 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-23 18:00:33 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:36 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:01:05 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:08:31 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:43 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:20 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:00 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:01:52 | Norwood (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:06:26 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:23:41 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:52 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:11:16 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:02:49 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:04:16 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:06:45 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:04:05 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:00:55 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:03:09 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-03-23 18:16:35 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.008 |  |
| 2026-03-23 18:25:40 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.009 |  |
| 2026-03-23 18:02:17 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:04:53 | Moragaswewa (Deduru Oya) | -0.07 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:02:40 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:01:26 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-03-23 18:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-03-23 18:01:28 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | -0.031 |  |
| 2026-03-23 18:04:20 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.031 |  |
| 2026-03-23 18:01:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.091 |  |
| 2026-03-23 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | -0.101 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)