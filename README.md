# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--09_06:12:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **93,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 06:12:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:11:10 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-03-09 06:09:47 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:09:09 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:07:11 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:06:36 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-09 06:06:28 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:06:04 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-09 06:05:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.009 |  |
| 2026-03-09 06:05:28 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:05:05 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-09 06:05:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:05:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.126 |  |
| 2026-03-09 06:04:56 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:04:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 06:04:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-09 06:04:32 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:04:21 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:03:52 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:03:35 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-03-09 06:03:17 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.053 |  |
| 2026-03-09 06:02:53 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:02:49 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:02:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:02:26 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 06:02:17 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 06:02:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.057 |  |
| 2026-03-09 06:02:16 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:01:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-03-09 06:01:53 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-03-09 06:01:33 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:01:12 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:41 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:39 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:38 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-09 06:00:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-09 06:00:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-09 05:55:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-09 05:49:09 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-09 06:00:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.409 | 🔺 Rising |
| 2026-03-09 06:05:05 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-03-09 06:01:53 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-03-09 06:06:36 | Rathnapura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-09 06:02:26 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-09 06:02:17 | Manampitiya (Mahaweli Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-09 06:06:04 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-09 06:04:49 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-09 06:02:33 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:01:33 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:07:11 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:12:45 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:04:21 | Giriulla (Maha Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:06:28 | Horowpothana (Yan Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:31:40 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:02:53 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:09:47 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:05:28 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:04:56 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:41 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:03:52 | Moraketiya (Walawe Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:02:16 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:09:09 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:04:32 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-08 18:03:18 | Thanthirimale (Malwathu Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:05:00 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:00:48 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-09 06:01:12 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-09 05:26:10 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | -0.007 |  |
| 2026-03-09 06:11:10 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | -0.009 |  |
| 2026-03-09 06:05:42 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.009 |  |
| 2026-03-09 06:00:13 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-03-09 06:04:45 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-09 06:01:56 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-03-09 06:03:35 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-03-09 06:00:13 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.020 |  |
| 2026-03-09 06:03:17 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | -0.053 |  |
| 2026-03-09 06:02:16 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.057 |  |
| 2026-03-09 06:05:00 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)