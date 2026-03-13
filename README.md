# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_17:09:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,414 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 17:09:41 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 17:08:12 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-03-13 17:08:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:07:39 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:07:09 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 17:06:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:06:56 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-03-13 17:06:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 17:06:12 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-03-13 17:06:05 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:05:58 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.202 |  |
| 2026-03-13 17:05:55 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.032 |  |
| 2026-03-13 17:05:06 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.033 |  |
| 2026-03-13 17:04:48 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:04:10 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 17:04:09 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:03:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 17:03:28 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 17:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-13 17:03:12 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.022 |  |
| 2026-03-13 17:03:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 17:03:06 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-03-13 17:02:59 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:20 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.127 |  |
| 2026-03-13 17:02:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-03-13 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:02:07 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:05 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:03 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:01:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:00:40 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 17:00:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.024 |  |
| 2026-03-13 17:00:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-13 16:16:16 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 17:03:14 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-13 17:00:18 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-13 17:06:51 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-13 17:07:09 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-13 17:03:28 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-03-13 17:03:33 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-13 16:06:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-03-13 17:00:40 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-13 17:03:09 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 17:04:10 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 17:09:41 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-13 17:02:03 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:04:48 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:38 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:08:18 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:59 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:07 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | 0.000 |  |
| 2026-03-13 16:12:34 | Baddegama (Gin Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:01:15 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:04:09 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:06:58 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:06:05 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:08:00 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:02:05 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-13 17:07:39 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:01:14 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-03-13 17:02:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -0.012 |  |
| 2026-03-13 17:08:12 | Pitabeddara (Nilwala Ganga) | 0.83 | 🟢 Normal | -0.018 |  |
| 2026-03-13 17:06:12 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-03-13 17:03:12 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.022 |  |
| 2026-03-13 16:02:46 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2026-03-13 17:00:31 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.024 |  |
| 2026-03-13 17:05:55 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.032 |  |
| 2026-03-13 17:05:06 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.033 |  |
| 2026-03-13 17:06:56 | Peradeniya (Mahaweli Ganga) | 1.14 | 🟢 Normal | -0.039 |  |
| 2026-03-13 17:03:06 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | -0.079 |  |
| 2026-03-13 17:02:20 | Weraganthota (Mahaweli Ganga) | -2.86 | 🟢 Normal | -0.127 |  |
| 2026-03-13 17:05:58 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)