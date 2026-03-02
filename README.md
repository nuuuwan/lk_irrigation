# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_09:04:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,015 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 09:04:41 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:12 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 09:03:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:03:21 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-02 09:02:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.056 |  |
| 2026-03-02 09:02:53 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-03-02 09:02:53 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 09:02:50 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.025 |  |
| 2026-03-02 09:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:02:28 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:02:28 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-03-02 09:01:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:43 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:32 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:14 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:13 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:12 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:57 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 09:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:20 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-02 09:00:15 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-02 08:43:07 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:41:46 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:36:14 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:31:57 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:31:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:15:36 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.090 |  |
| 2026-03-02 08:13:55 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.025 |  |
| 2026-03-02 08:12:14 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 08:11:08 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.012 |  |
| 2026-03-02 08:10:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:09:57 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 09:00:20 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-02 09:03:21 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-02 08:04:59 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-03-02 09:02:53 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 09:00:57 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 08:03:09 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 09:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 09:01:13 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:14 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:12 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:03:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:41 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:06:40 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:32 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:31:57 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:41:46 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:43 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:08:03 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:06:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:02:38 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:09:57 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:10:22 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:15 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-02 09:02:53 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-03-02 08:00:41 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-03-02 08:02:07 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-03-02 09:02:50 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.025 |  |
| 2026-03-02 09:02:28 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-03-02 08:03:56 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.046 |  |
| 2026-03-02 08:01:12 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | -0.053 |  |
| 2026-03-02 09:02:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.056 |  |
| 2026-03-02 08:04:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.062 |  |
| 2026-03-02 08:15:36 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.090 |  |
| 2026-03-02 08:04:54 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)