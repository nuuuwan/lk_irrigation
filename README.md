# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_23:31:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,789 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 23:31:37 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:22:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:19:06 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:09:50 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-21 23:07:56 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:07:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:06:33 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:06:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-21 23:05:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.013 |  |
| 2026-03-21 23:05:34 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-03-21 23:05:10 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:04:39 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:04:27 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 23:04:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:03:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-03-21 23:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:02:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-03-21 23:02:45 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:02:38 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.020 |  |
| 2026-03-21 23:02:36 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-03-21 23:02:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.120 |  |
| 2026-03-21 23:02:10 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:55 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:52 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:45 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:01:32 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2026-03-21 23:01:29 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-03-21 23:01:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:05 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:55:28 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.306 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 23:01:29 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-03-21 23:03:19 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-03-21 23:02:36 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-03-21 23:05:34 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-03-21 22:37:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-03-21 22:01:16 | Panadugama (Nilwala Ganga) | 2.05 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-21 23:04:27 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 23:01:52 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:05 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:01:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:03:03 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:31:37 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:19:06 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:02:45 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:26 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:22:23 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:07:47 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:01:23 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 23:02:10 | Thanamalwila (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-21 22:08:28 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-03-21 23:09:50 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.009 |  |
| 2026-03-21 23:07:56 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:05:10 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:04:39 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:01:45 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:04:22 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:06:33 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-21 23:05:39 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | -0.013 |  |
| 2026-03-21 23:06:09 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-21 23:02:38 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.020 |  |
| 2026-03-21 22:03:48 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.039 |  |
| 2026-03-21 23:01:32 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.041 |  |
| 2026-03-21 23:02:48 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | -0.065 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 23:02:12 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.120 |  |
| 2026-03-21 22:04:33 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.234 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)