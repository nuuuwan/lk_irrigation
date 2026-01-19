# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--19_21:24:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,192 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 21:24:22 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:12:40 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:09:02 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-01-19 21:06:21 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:06:06 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:59 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:53 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:45 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-19 21:05:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:06 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:04:11 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:04:11 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 21:03:56 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:03:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:03:47 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:03:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-19 21:03:36 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.361 |  |
| 2026-01-19 21:03:12 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:53 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-01-19 21:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:02:33 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:26 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:15 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.051 |  |
| 2026-01-19 21:02:05 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-01-19 21:02:03 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:33 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-19 21:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:10 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:39 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:23 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-01-19 21:00:18 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 20:53:40 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-19 21:00:23 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.313 | 🔺 Rising |
| 2026-01-19 21:05:45 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-19 21:04:11 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-19 21:01:17 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:06:06 | Moragaswewa (Deduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:38 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:00 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:53 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:03 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:09:02 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:43 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:03:12 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:12:40 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:48 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:06:21 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:18 | Padiyathalawa (Maduru Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:02:33 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:38 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:00:39 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:03:56 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:59 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:05:42 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:10 | Manampitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:02:06 | Thanthirimale (Malwathu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:24:22 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:01:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-19 21:03:47 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-19 18:01:58 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:04:11 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-19 18:00:21 | Weraganthota (Mahaweli Ganga) | -1.89 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:02:35 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:03:54 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-19 21:02:05 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-01-19 21:07:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.019 |  |
| 2026-01-19 21:01:33 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.020 |  |
| 2026-01-19 21:03:43 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-01-19 21:02:53 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.041 |  |
| 2026-01-19 21:02:15 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.051 |  |
| 2026-01-19 21:03:36 | Kithulgala (Kelani Ganga) | 1.22 | 🟢 Normal | -0.361 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)