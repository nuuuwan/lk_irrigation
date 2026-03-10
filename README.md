# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--10_09:11:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **94,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 09:11:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:10:23 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-03-10 09:08:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:08:18 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:08:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-03-10 09:06:21 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:05:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-10 09:04:55 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:04:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:04:51 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-10 09:04:28 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-10 09:04:11 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.290 |  |
| 2026-03-10 09:04:04 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:03:57 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:03:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:03:41 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:03:11 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.089 |  |
| 2026-03-10 09:03:08 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 09:03:02 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.070 |  |
| 2026-03-10 09:02:54 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:40 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:29 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.068 |  |
| 2026-03-10 09:02:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:25 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-03-10 09:02:22 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-03-10 09:02:18 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:18 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:05 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.109 |  |
| 2026-03-10 09:02:03 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-10 09:01:58 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-10 09:01:52 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-03-10 09:01:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.041 |  |
| 2026-03-10 09:01:07 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.041 |  |
| 2026-03-10 09:00:51 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-10 09:03:08 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-10 09:04:51 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-10 09:11:08 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:03:41 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:03:57 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-10 09:05:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-10 09:02:14 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:47 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:18 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:27 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:03:02 | Giriulla (Maha Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:40 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:08:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:04:55 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:03:57 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:18 | Padiyathalawa (Maduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:54 | Dunamale (Aththanagalu Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:02:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:01:52 | Badalgama (Maha Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:04:54 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:00:51 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:04:04 | Thawalama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:06:21 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-10 09:10:23 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | -0.009 |  |
| 2026-03-10 09:04:28 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-03-10 09:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-03-10 09:01:58 | Moraketiya (Walawe Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-03-10 09:02:03 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.011 |  |
| 2026-03-10 09:02:25 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.020 |  |
| 2026-03-10 09:02:22 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.020 |  |
| 2026-03-10 09:08:07 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.038 |  |
| 2026-03-10 09:01:07 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.041 |  |
| 2026-03-10 09:01:14 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.041 |  |
| 2026-03-10 09:01:39 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.064 |  |
| 2026-03-10 09:02:29 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.068 |  |
| 2026-03-10 09:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | -0.070 |  |
| 2026-03-10 09:03:11 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.089 |  |
| 2026-03-10 09:02:05 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.109 |  |
| 2026-03-10 09:04:11 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.290 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)