# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_19:09:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,418 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 19:09:18 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 19:08:43 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.091 |  |
| 2026-03-02 19:08:16 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:07:46 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.118 |  |
| 2026-03-02 19:07:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:07:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:58 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:05:54 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:08 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-02 19:04:28 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-02 19:03:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-02 19:02:59 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:02:49 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-02 19:02:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:02:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-03-02 19:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:27 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 19:02:24 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.637 |  |
| 2026-03-02 19:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:06 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-02 19:01:51 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-03-02 19:01:43 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:20 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-02 19:01:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:12 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-03-02 19:00:58 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:00:38 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:00:10 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-02 18:29:13 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 19:02:30 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.438 | 🔺 Rising |
| 2026-03-02 19:02:49 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-02 19:04:28 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-02 19:00:10 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-02 19:01:20 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-02 19:05:08 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-02 19:02:27 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 19:02:59 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:05:58 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:02:48 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 19:09:18 | Manampitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-02 19:00:38 | Wellawaya (Kirindi Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:16 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:28 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:07:37 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:43 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:19 | Horowpothana (Yan Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:08:16 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:06 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:29:13 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:00:58 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:09 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:54 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:07:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:42 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:02:24 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:05:58 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-02 19:01:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-02 19:02:06 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-02 19:01:51 | Ellagawa (Kalu Ganga) | 3.90 | 🟢 Normal | -0.010 |  |
| 2026-03-02 18:03:14 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-03-02 19:01:12 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | -0.012 |  |
| 2026-03-02 19:03:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | -0.020 |  |
| 2026-03-02 19:08:43 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.091 |  |
| 2026-03-02 19:07:46 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.118 |  |
| 2026-03-02 19:02:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.637 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)