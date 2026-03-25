# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--26_05:09:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **107,558 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 05:09:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.174 |  |
| 2026-03-26 05:06:55 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -30.769 |  |
| 2026-03-26 05:06:51 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:06:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-03-26 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:50 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:46 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:27 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-03-26 05:05:26 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:04:58 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | -30.769 |  |
| 2026-03-26 05:04:42 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-26 05:04:04 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 05:03:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:03:07 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:03:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.013 |  |
| 2026-03-26 05:02:46 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:34 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-26 05:02:33 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.097 |  |
| 2026-03-26 05:02:25 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:24 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-26 05:02:20 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:43 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-26 05:01:29 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:10 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:07 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-26 05:01:03 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:00:24 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-26 05:00:09 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:57:40 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:56:55 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:40:53 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:22:05 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:20:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-03-26 04:20:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-03-26 04:19:16 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-26 04:20:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-03-26 05:02:34 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-03-26 05:00:24 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-03-26 05:01:07 | Manampitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-26 05:01:43 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-03-26 05:04:04 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-26 04:02:59 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:25 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:29 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:24 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:21 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:26 | Giriulla (Maha Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:03:07 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:00:29 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:56:55 | Magura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:46 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:46 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:05:50 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-26 03:03:23 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:03:05 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:01:09 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:02:20 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-26 04:02:44 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:03:39 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:06:51 | Holombuwa (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-25 18:02:01 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:01:10 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:00:09 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-26 05:04:42 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-26 05:02:24 | Thawalama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-03-26 05:05:27 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-03-26 05:06:41 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-03-26 05:02:57 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.013 |  |
| 2026-03-25 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.060 |  |
| 2026-03-26 00:06:33 | Putupaula (Kalu Ganga) | 0.22 | 🟢 Normal | -0.092 |  |
| 2026-03-26 05:02:33 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.097 |  |
| 2026-03-26 05:09:31 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.174 |  |
| 2026-03-26 05:06:55 | Badalgama (Maha Oya) | 1.74 | 🟢 Normal | -30.769 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)