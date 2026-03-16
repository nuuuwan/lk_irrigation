# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_06:16:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **98,661 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 06:16:13 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:13:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:12:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-03-16 06:09:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:07:27 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-16 06:07:16 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-16 06:07:04 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-16 06:06:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-03-16 06:06:25 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:06:21 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.012 |  |
| 2026-03-16 06:05:32 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:05:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:04:43 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-16 06:04:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:04:27 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.045 |  |
| 2026-03-16 06:04:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:40 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-16 06:03:07 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:04 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-03-16 06:02:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:50 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 06:02:42 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:02:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-03-16 06:02:37 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:18 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:56 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:55 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-03-16 06:01:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-03-16 06:01:47 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-16 06:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:35 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.050 |  |
| 2026-03-16 06:01:32 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-03-16 06:01:26 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-16 06:01:23 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-03-16 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.171 |  |
| 2026-03-16 06:00:21 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-16 05:47:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.171 |  |
| 2026-03-16 05:46:59 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 05:36:11 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.047 |  |
| 2026-03-16 05:32:43 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 05:32:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.171 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 06:02:46 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-03-16 06:07:16 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-03-16 06:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-16 06:01:26 | Weraganthota (Mahaweli Ganga) | -2.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-03-16 06:04:43 | Putupaula (Kalu Ganga) | 0.58 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-03-16 06:07:27 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-16 06:05:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:43 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:13:37 | Horowpothana (Yan Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:05:04 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:37 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:40 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:01:56 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:18 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:06:25 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:03:07 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:55 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:16:13 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:02:50 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-15 18:02:20 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:04:02 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-16 06:09:51 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:02:42 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:00:21 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:05:32 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-16 06:01:50 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-03-16 06:06:21 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | -0.012 |  |
| 2026-03-16 06:01:55 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.020 |  |
| 2026-03-16 06:01:47 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.020 |  |
| 2026-03-16 06:03:04 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.021 |  |
| 2026-03-16 06:01:23 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.022 |  |
| 2026-03-16 06:07:04 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.030 |  |
| 2026-03-16 06:12:59 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-03-16 06:02:39 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.041 |  |
| 2026-03-16 06:04:27 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | -0.045 |  |
| 2026-03-16 06:01:32 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.047 |  |
| 2026-03-16 06:01:35 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.050 |  |
| 2026-03-16 06:06:57 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.055 |  |
| 2026-03-16 06:01:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)