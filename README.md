# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_09:10:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 09:10:18 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:08:49 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.045 |  |
| 2026-03-02 09:08:06 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:08:04 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:07:56 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:07:01 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:06:25 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-03-02 09:05:33 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.025 |  |
| 2026-03-02 09:05:25 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.037 |  |
| 2026-03-02 09:05:20 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.367 |  |
| 2026-03-02 09:05:10 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:05:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:05:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.070 |  |
| 2026-03-02 09:04:57 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 09:00:20 | Weraganthota (Mahaweli Ganga) | -1.72 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-03-02 09:03:21 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-02 09:02:53 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 09:00:57 | Thaldena (Mahaweli Ganga) | 0.41 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 09:04:08 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-02 09:01:13 | Wellawaya (Kirindi Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:14 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:12 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:53 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:03:56 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:10:18 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:41 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:07:56 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:32 | Ellagawa (Kalu Ganga) | 3.94 | 🟢 Normal | 0.000 |  |
| 2026-03-02 08:31:57 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:43 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:29 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:05:10 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:08:06 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:08:04 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:02:47 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:05:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:04:57 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:07:01 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:01:45 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-03-02 09:00:15 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-03-02 09:02:53 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.012 |  |
| 2026-03-02 08:00:41 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | -0.019 |  |
| 2026-03-02 09:06:25 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-03-02 09:02:50 | Thawalama (Gin Ganga) | 1.01 | 🟢 Normal | -0.025 |  |
| 2026-03-02 09:05:33 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | -0.025 |  |
| 2026-03-02 09:02:28 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-03-02 09:05:25 | Glencourse (Kelani Ganga) | 8.46 | 🟢 Normal | -0.037 |  |
| 2026-03-02 09:08:49 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.045 |  |
| 2026-03-02 08:03:56 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.046 |  |
| 2026-03-02 09:02:56 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.056 |  |
| 2026-03-02 09:05:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.62 | 🟢 Normal | -0.070 |  |
| 2026-03-02 09:05:20 | Kithulgala (Kelani Ganga) | 1.18 | 🟢 Normal | -0.367 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)