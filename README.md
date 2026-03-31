# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--31_12:09:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **112,315 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 12:09:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-03-31 12:06:42 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:06:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:05:59 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-31 12:05:48 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:05:28 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:57 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:37 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-31 12:04:35 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:34 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:19 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:09 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:04 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:03:43 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:03:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:03:25 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:03:07 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 12:02:58 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:49 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:02:37 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.042 |  |
| 2026-03-31 12:02:37 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:02:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-03-31 12:02:13 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:11 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 12:01:59 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:48 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:33 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-31 12:01:28 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:25 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-03-31 12:01:24 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:01:20 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-31 12:01:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:00 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | -0.099 |  |
| 2026-03-31 12:00:46 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:00:26 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:00:24 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 1.035 | 🔺 Rising |
| 2026-03-31 11:23:39 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-03-31 11:23:17 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-31 12:00:24 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 1.035 | 🔺 Rising |
| 2026-03-31 12:09:48 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-03-31 12:01:33 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-03-31 12:03:07 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-31 12:04:37 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-03-31 12:05:59 | Ellagawa (Kalu Ganga) | 3.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-31 12:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-31 12:03:43 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:00:26 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:13 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:34 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:05:48 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:11 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:35 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:59 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:19 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:06:42 | Panadugama (Nilwala Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:03:29 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:28 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:21 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:01:48 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:57 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:58 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:09 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:00:46 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:05:28 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:06:20 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:02:13 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-31 12:04:04 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:02:37 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:02:49 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:01:24 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-31 12:01:20 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.011 |  |
| 2026-03-31 11:08:31 | Baddegama (Gin Ganga) | 0.66 | 🟢 Normal | -0.019 |  |
| 2026-03-31 12:01:25 | Peradeniya (Mahaweli Ganga) | 1.00 | 🟢 Normal | -0.021 |  |
| 2026-03-31 11:23:39 | Thawalama (Gin Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-03-31 12:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-03-31 12:02:37 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.042 |  |
| 2026-03-31 12:01:00 | Weraganthota (Mahaweli Ganga) | -2.20 | 🟢 Normal | -0.099 |  |

## River Water Level Charts by Station

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)