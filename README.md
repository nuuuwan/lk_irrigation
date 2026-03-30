# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--30_23:31:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **111,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 23:31:08 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:29:17 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-30 23:16:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:12:22 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-03-30 23:09:21 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 23:06:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-03-30 23:06:50 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:06:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.019 |  |
| 2026-03-30 23:06:02 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:05:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 23:05:08 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:04:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:04:16 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:31 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:28 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-03-30 23:03:21 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:20 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:06 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 23:02:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:29 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:22 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:21 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 23:02:18 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-30 23:01:57 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-30 23:01:46 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-03-30 23:01:11 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:01:10 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:00:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-30 22:52:58 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-30 23:29:17 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-03-30 23:06:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-03-30 23:01:57 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-03-30 23:02:21 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-30 22:15:07 | Thawalama (Gin Ganga) | 1.04 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-30 23:05:55 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 23:03:06 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-30 23:09:21 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 18:07:18 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-30 23:06:02 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:34 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:31 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:31:08 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:21 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:01:11 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:06:50 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:16:10 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:47 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:01:10 | Panadugama (Nilwala Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:03:20 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:00:56 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:34 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:04:45 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:04:16 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:45 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:22 | Badalgama (Maha Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:05:08 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-30 18:00:31 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-03-30 22:08:42 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:02:29 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-30 21:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-03-30 23:01:46 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-03-30 23:02:18 | Hanwella (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-03-30 22:08:13 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.012 |  |
| 2026-03-30 23:03:28 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | -0.013 |  |
| 2026-03-30 23:06:28 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.019 |  |
| 2026-03-30 23:12:22 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | -0.037 |  |
| 2026-03-30 22:04:22 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.042 |  |
| 2026-03-30 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)