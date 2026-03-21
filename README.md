# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--21_20:21:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **103,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 20:21:43 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-03-21 20:19:49 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-21 20:15:39 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:14:54 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.147 |  |
| 2026-03-21 20:14:41 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:12:59 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:08:21 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 20:06:37 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 20:06:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.087 |  |
| 2026-03-21 20:06:24 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-03-21 20:05:21 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-03-21 20:05:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:04:22 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:03:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:03:52 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 20:03:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:03:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:03:23 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 20:02:53 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:47 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:43 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:30 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:26 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:25 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:23 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-21 20:02:10 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-03-21 20:02:07 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:01:40 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-21 20:01:14 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:00:57 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:47 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:16 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-21 20:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 19:33:19 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 19:31:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-21 19:30:33 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-21 20:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-03-21 20:01:40 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-03-21 20:08:21 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-21 20:06:37 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-21 20:03:23 | Hanwella (Kelani Ganga) | 0.43 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-21 20:03:52 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-21 20:19:49 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-03-21 20:02:26 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:25 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:09 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:05:20 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:31 | Nawalapitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:03:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:14:41 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:57 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-21 18:01:02 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:53 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:47 | Ellagawa (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:04:22 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:00:47 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:30 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:15:39 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:12:59 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:03:27 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:23 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:02:07 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-21 20:06:24 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-03-21 20:03:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:02:43 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-03-21 18:01:35 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:01:14 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-03-21 20:02:10 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.011 |  |
| 2026-03-21 20:00:16 | Manampitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.030 |  |
| 2026-03-21 20:21:43 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.035 |  |
| 2026-03-21 20:05:21 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.061 |  |
| 2026-03-21 18:00:19 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.082 |  |
| 2026-03-21 20:06:26 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.087 |  |
| 2026-03-21 20:14:54 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)