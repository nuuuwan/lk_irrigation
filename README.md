# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_11:23:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,277 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 11:23:39 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-03-31 11:23:17 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:13:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:12:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-03-31 11:12:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-31 11:12:12 | Ellagawa (Kalu Ganga) | 3.69 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-31 11:11:50 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-31 11:10:55 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:09:09 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:08:31 | Baddegama (Gin Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-31 11:07:45 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:07:28 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:06:01 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.031 |  |
| 2026-03-31 11:05:21 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-03-31 11:05:11 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-03-31 11:05:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:04:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:04:21 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:04:04 | Kuda Oya (Kirindi Oya) | 0.11 | 🟢 Normal | -0.936 |  |
| 2026-03-31 11:03:50 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:03:44 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.013 |  |
| 2026-03-31 11:03:42 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:03:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:03:33 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-03-31 11:03:07 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 11:02:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:02:29 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:25 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:21 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-03-31 11:02:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:01:48 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-03-31 11:01:23 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-31 11:01:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:01:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:01:10 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:00:39 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.153 |  |
| 2026-03-31 11:00:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 11:12:14 | Ellagawa (Kalu Ganga) | 3.70 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-03-31 11:05:21 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.357 | 🔺 Rising |
| 2026-03-31 11:11:50 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-31 11:01:23 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-03-31 11:03:07 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 11:01:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:13:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:07:45 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:00:39 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:23:17 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:21 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:10:55 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:04:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:00:12 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:29 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:05:06 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:25 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:03:50 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:01:10 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:02:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 11:07:28 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:09:09 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:02:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:01:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:03:35 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:04:21 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:03:42 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-31 11:01:48 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | -0.011 |  |
| 2026-03-31 11:03:44 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.013 |  |
| 2026-03-31 11:12:24 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.019 |  |
| 2026-03-31 11:08:31 | Baddegama (Gin Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-31 11:03:33 | Rathnapura (Kalu Ganga) | 0.44 | 🟢 Normal | -0.021 |  |
| 2026-03-31 11:23:39 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-03-31 11:06:01 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.031 |  |
| 2026-03-31 11:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.040 |  |
| 2026-03-31 11:05:11 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-03-31 11:00:14 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.153 |  |
| 2026-03-31 11:04:04 | Kuda Oya (Kirindi Oya) | 0.11 | 🟢 Normal | -0.936 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)