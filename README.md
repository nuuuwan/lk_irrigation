# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_22:12:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 22:12:30 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:11:53 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.017 |  |
| 2026-03-16 22:11:19 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-03-16 22:09:54 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-16 22:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-03-16 22:08:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:08:14 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:06:53 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:05:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:05:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-16 22:05:12 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:04:59 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:04:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:04:02 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.097 |  |
| 2026-03-16 22:04:00 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:03:43 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:31 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:03:25 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:20 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 22:03:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-16 22:02:58 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:02:58 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 22:02:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.038 |  |
| 2026-03-16 22:02:18 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:02:15 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-16 22:01:50 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-03-16 22:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:01:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-03-16 22:01:17 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 22:01:27 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | 0.522 | 🔺 Rising |
| 2026-03-16 22:05:13 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-03-16 22:03:19 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-03-16 22:09:54 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-16 22:02:15 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-16 22:03:20 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 22:02:58 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 22:00:53 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:05:44 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:01:42 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:12:30 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:05:12 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 21:20:19 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:08:14 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:25 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:04:05 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-16 21:03:34 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:03:43 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:08:21 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:01:17 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-03-16 21:00:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-03-16 22:06:53 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:03:31 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:02:18 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:04:59 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:02:58 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:06:25 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:04:00 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-03-16 22:01:50 | Ellagawa (Kalu Ganga) | 3.86 | 🟢 Normal | -0.011 |  |
| 2026-03-16 22:11:53 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.017 |  |
| 2026-03-16 22:11:19 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.018 |  |
| 2026-03-16 22:02:51 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.038 |  |
| 2026-03-16 22:08:47 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-03-16 22:04:02 | Deraniyagala (Kelani Ganga) | 0.14 | 🟢 Normal | -0.097 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)