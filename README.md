# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--19_13:16:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **101,628 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 13:16:41 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:15:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:13:11 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:10:22 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-19 13:09:34 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:09:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-19 13:09:19 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-19 13:09:07 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:09:02 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.144 |  |
| 2026-03-19 13:07:33 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.018 |  |
| 2026-03-19 13:07:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.037 |  |
| 2026-03-19 13:06:59 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:06:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-19 13:06:36 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.113 |  |
| 2026-03-19 13:06:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:05:26 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:05:14 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-03-19 13:04:41 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2026-03-19 13:04:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:49 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-19 13:03:39 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:39 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:36 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.059 |  |
| 2026-03-19 13:03:28 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:22 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 13:03:21 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 13:03:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 13:02:44 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 13:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-03-19 13:02:38 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-03-19 13:02:24 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:22 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-03-19 13:02:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-19 13:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 13:01:54 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 12:59:39 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-19 13:02:38 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-03-19 13:06:50 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-19 13:09:20 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-03-19 13:09:19 | Manampitiya (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-19 13:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-19 13:03:22 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-19 13:02:07 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-19 13:03:21 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 13:03:05 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-19 12:01:46 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:24 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:05:26 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:01:48 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:39 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:01:54 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:13:11 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:16:41 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:28 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:03:39 | Glencourse (Kelani Ganga) | 8.68 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:04:15 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:09:07 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:06:33 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:15:26 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:09:34 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-19 13:10:22 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-03-19 13:02:44 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-19 13:07:33 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.018 |  |
| 2026-03-19 13:02:41 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | -0.020 |  |
| 2026-03-19 13:03:49 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-03-19 13:02:22 | Thanamalwila (Kirindi Oya) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-03-19 12:59:39 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.021 |  |
| 2026-03-19 13:05:14 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.021 |  |
| 2026-03-19 13:07:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | -0.037 |  |
| 2026-03-19 13:04:41 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.041 |  |
| 2026-03-19 13:03:36 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.059 |  |
| 2026-03-19 13:06:36 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.113 |  |
| 2026-03-19 13:09:02 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)