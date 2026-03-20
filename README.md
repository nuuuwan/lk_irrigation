# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_03:30:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,025 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 03:30:03 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:27:32 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:27:12 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:25:19 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-21 03:13:00 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:12:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:12:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:10:40 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-21 03:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-21 03:06:49 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-21 03:05:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:05:30 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 03:05:13 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 03:04:37 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:04:37 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:04:28 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-21 03:04:27 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-21 03:04:25 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-21 03:04:12 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-03-21 03:04:01 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -36.000 |  |
| 2026-03-21 03:04:00 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -36.000 |  |
| 2026-03-21 03:03:59 | Magura (Kalu Ganga) | 0.80 | 🟢 Normal | -36.000 |  |
| 2026-03-21 03:03:51 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-03-21 03:03:39 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:03 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:03 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-03-21 03:02:19 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:58 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-21 03:01:36 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.218 |  |
| 2026-03-21 03:01:33 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:32 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:27 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:18 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:43 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:37 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:14 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 03:04:28 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 36.000 | 🔺 Rising |
| 2026-03-21 03:25:19 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-03-21 03:03:03 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-03-21 03:10:40 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 03:05:30 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 03:00:14 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 03:01:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-21 03:00:43 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:02:19 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:30 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:12:24 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:58 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:30:03 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-21 02:10:11 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:51 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:13:00 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:33 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:18 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:03 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:05:58 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:30 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:12:54 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:00:17 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:27 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:04:37 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:04:37 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:01:32 | Manampitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:27:32 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:03:39 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-03-21 03:06:49 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-03-21 03:05:13 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-21 03:03:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.011 |  |
| 2026-03-21 03:04:12 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-03-21 03:09:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.061 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-21 03:01:36 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.218 |  |
| 2026-03-21 03:04:01 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)