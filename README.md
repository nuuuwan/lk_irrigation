# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_01:11:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,947 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 01:11:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:09:38 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.018 |  |
| 2026-03-21 01:06:41 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-03-21 01:06:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-03-21 01:05:50 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.019 |  |
| 2026-03-21 01:05:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-03-21 01:04:29 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-03-21 01:04:09 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:03:48 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-03-21 01:03:32 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-21 01:03:31 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:18 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-21 01:03:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:02:53 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.005 |  |
| 2026-03-21 01:02:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:02:08 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 01:01:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:01:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:01:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:01:02 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:58 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:41 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-21 01:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:56:31 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.063 |  |
| 2026-03-21 00:50:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:40:34 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.071 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 00:01:57 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-03-21 01:00:41 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-03-21 00:00:13 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-21 01:02:08 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 00:10:56 | Baddegama (Gin Ganga) | 1.31 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 01:01:27 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:48 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:24 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:11:57 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:31 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:58 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:00:46 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:01:25 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:18 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:01:02 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 00:50:52 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:03:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-03-21 01:02:53 | Panadugama (Nilwala Ganga) | 2.12 | 🟢 Normal | -0.005 |  |
| 2026-03-21 00:08:43 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-03-21 01:01:26 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:02:18 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 00:06:33 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:04:09 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.010 |  |
| 2026-03-21 01:03:36 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.011 |  |
| 2026-03-21 01:03:32 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.011 |  |
| 2026-03-21 01:09:38 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | -0.018 |  |
| 2026-03-21 00:10:39 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | -0.018 |  |
| 2026-03-21 01:05:50 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.019 |  |
| 2026-03-21 01:06:41 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | -0.020 |  |
| 2026-03-21 01:03:12 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.020 |  |
| 2026-03-21 01:05:04 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.022 |  |
| 2026-03-20 21:08:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.039 |  |
| 2026-03-21 01:04:29 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.040 |  |
| 2026-03-21 01:06:05 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-03-21 00:40:34 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.071 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)