# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_03:11:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,969 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 03:11:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-31 03:10:03 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:08:52 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-03-31 03:07:02 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.005 |  |
| 2026-03-31 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-03-31 03:06:05 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:05:53 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:05:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:04:06 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:03:45 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:03:42 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:03:14 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.114 |  |
| 2026-03-31 03:03:04 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-03-31 03:03:02 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:46 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:38 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-31 03:02:31 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.041 |  |
| 2026-03-31 03:01:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:38 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:20 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -36.000 |  |
| 2026-03-31 03:01:20 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:18 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -36.000 |  |
| 2026-03-31 03:01:08 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:46:36 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 03:02:38 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-03-31 03:11:10 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-31 02:06:00 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-31 03:03:42 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:05:53 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:31 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:46 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:34 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:03:03 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:21 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:38 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:08 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:06:05 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:20 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:20 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:03:45 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:01:38 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-31 01:01:17 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:02:40 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:04:06 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:05:41 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:05:26 | Thawalama (Gin Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-31 02:09:23 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:03:02 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:10:03 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-31 03:07:02 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.005 |  |
| 2026-03-31 03:08:52 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-03-31 03:03:04 | Manampitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.029 |  |
| 2026-03-31 02:02:27 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | -0.032 |  |
| 2026-03-31 03:02:13 | Deraniyagala (Kelani Ganga) | 0.06 | 🟢 Normal | -0.041 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |
| 2026-03-31 02:01:07 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.050 |  |
| 2026-03-31 03:06:17 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.062 |  |
| 2026-03-31 03:03:14 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.114 |  |
| 2026-03-31 03:01:20 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)