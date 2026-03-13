# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_03:49:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,770 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 03:49:45 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 03:40:01 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-14 03:20:51 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:17:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:12:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-14 03:10:17 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.005 |  |
| 2026-03-14 03:07:47 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:07:14 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:06:44 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.153 |  |
| 2026-03-14 03:06:33 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 03:05:19 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.062 |  |
| 2026-03-14 03:05:16 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:05:12 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.058 |  |
| 2026-03-14 03:04:43 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:04:32 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:04:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:04:11 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-03-14 03:04:01 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:03:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-03-14 03:03:38 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:03:36 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 03:03:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:03:03 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:02:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:02:16 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.020 |  |
| 2026-03-14 03:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-14 03:01:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:01:07 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:00:59 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.070 |  |
| 2026-03-14 03:00:30 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 03:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-14 03:03:36 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-14 03:12:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-03-14 03:49:45 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-03-14 03:06:33 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-14 03:40:01 | Putupaula (Kalu Ganga) | 0.48 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-14 03:01:21 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:03:03 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:07:14 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:01:07 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-14 03:00:30 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:03:35 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:17:43 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:05:12 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-14 02:57:59 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:04:01 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:02:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:20:51 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:04:20 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:03:38 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:05:16 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:07:47 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 03:10:17 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.005 |  |
| 2026-03-14 00:27:36 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.007 |  |
| 2026-03-14 03:04:43 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:03:51 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:04:32 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-03-14 03:04:11 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-03-14 03:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.019 |  |
| 2026-03-14 03:02:16 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | -0.020 |  |
| 2026-03-14 01:02:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-03-14 03:04:54 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | -0.058 |  |
| 2026-03-14 03:05:19 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.062 |  |
| 2026-03-14 03:00:59 | Glencourse (Kelani Ganga) | 8.90 | 🟢 Normal | -0.070 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 03:06:44 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.153 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)