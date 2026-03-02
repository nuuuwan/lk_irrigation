# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_02:57:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,665 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 02:57:19 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | 2.157 | 🔺 Rising |
| 2026-03-03 02:43:11 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:26:55 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:26:54 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:14:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-03 02:11:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:08:08 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:06:29 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-03 02:06:00 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:05:56 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -36.000 |  |
| 2026-03-03 02:05:55 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -36.000 |  |
| 2026-03-03 02:05:53 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -36.000 |  |
| 2026-03-03 02:05:35 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:04:27 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-03 02:03:48 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-03 02:03:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 02:03:30 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:03:21 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 2.157 | 🔺 Rising |
| 2026-03-03 02:03:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.071 |  |
| 2026-03-03 02:02:50 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-03 02:02:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 02:57:19 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | 2.157 | 🔺 Rising |
| 2026-03-03 02:02:29 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-03 01:02:37 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-03-03 02:14:29 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-03-03 02:00:53 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 02:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.42 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-03 02:03:42 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-03-03 02:06:29 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-03-03 02:43:11 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:02:28 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:00:55 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:01:52 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:01:21 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:02:21 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:26:55 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:05:35 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:01:14 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:11:26 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-03 01:25:35 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-03 01:03:20 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:08:08 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-03 01:02:37 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:01:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:03:30 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 01:04:47 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:02:45 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 02:06:00 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-03 02:01:44 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-03-03 02:03:48 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-03 02:04:27 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-03 02:02:50 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-03-03 02:02:18 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-03-03 02:03:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.071 |  |
| 2026-03-03 02:00:59 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.109 |  |
| 2026-03-03 02:05:56 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)