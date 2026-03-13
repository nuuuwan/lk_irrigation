# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_22:17:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,606 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 22:17:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-03-13 22:17:41 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:13:35 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:10:12 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 22:09:58 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:09:54 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.037 |  |
| 2026-03-13 22:09:04 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:08:04 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-13 22:07:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-13 22:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-13 22:07:12 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 22:06:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-13 22:06:56 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:41 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:32 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-03-13 22:05:28 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:05:07 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:04:53 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:04:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:04:40 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-13 22:04:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:03:41 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:03:37 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-03-13 22:03:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:02:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.032 |  |
| 2026-03-13 22:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.088 |  |
| 2026-03-13 22:02:43 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 22:02:14 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:02:14 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:02:13 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:01:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.068 |  |
| 2026-03-13 22:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:01:31 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.031 |  |
| 2026-03-13 22:01:30 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:01:19 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 22:00:57 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.050 |  |
| 2026-03-13 22:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 22:06:32 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.602 | 🔺 Rising |
| 2026-03-13 22:08:04 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | 0.271 | 🔺 Rising |
| 2026-03-13 22:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-03-13 22:01:19 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 22:02:43 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 22:07:12 | Rathnapura (Kalu Ganga) | 1.09 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 22:10:12 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 22:03:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:01:30 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:41 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:17:41 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:01:50 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:05:28 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:13:35 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:06:56 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:05:07 | Padiyathalawa (Maduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:03:39 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:04:50 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:03:41 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:04:31 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:02:14 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:09:04 | Thawalama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:09:58 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:02:14 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 22:07:43 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-03-13 22:06:58 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-03-13 22:17:51 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.016 |  |
| 2026-03-13 22:04:40 | Deraniyagala (Kelani Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-03-13 22:03:37 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.029 |  |
| 2026-03-13 22:01:31 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.031 |  |
| 2026-03-13 22:02:52 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.032 |  |
| 2026-03-13 22:09:54 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | -0.037 |  |
| 2026-03-13 22:00:57 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.050 |  |
| 2026-03-13 22:01:58 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.068 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-13 22:02:50 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.088 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)