# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_17:11:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,308 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 17:11:49 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-02 17:11:27 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:09:24 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 17:07:41 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 17:07:06 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.055 |  |
| 2026-04-02 17:06:30 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-02 17:06:28 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:06:06 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 17:05:44 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:05:32 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-02 17:05:21 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.029 |  |
| 2026-04-02 17:04:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.116 |  |
| 2026-04-02 17:04:42 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:04:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:04:08 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:55 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-02 17:03:48 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:46 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 17:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-04-02 17:03:29 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:10 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-02 17:03:06 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-04-02 17:03:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-02 17:02:49 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:42 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:40 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:14 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:58 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:20 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-02 17:01:15 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:57 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-02 17:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-02 17:00:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 16:59:21 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 17:03:04 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.338 | 🔺 Rising |
| 2026-04-02 17:03:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-04-02 17:06:30 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-02 17:01:20 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-02 17:11:49 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-02 17:00:41 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-02 17:03:55 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-02 17:03:46 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 17:06:06 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 17:09:24 | Rathnapura (Kalu Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 17:07:41 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 17:02:08 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:01 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:40 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:05:44 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:06:28 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:42 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:04:08 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:58 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:49 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:06 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:11:27 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:00:21 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:29 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:04:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:04:42 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:01:15 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:48 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:02:14 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 17:03:35 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-04-02 17:03:10 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | -0.010 |  |
| 2026-04-02 17:05:32 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-04-02 17:05:21 | Glencourse (Kelani Ganga) | 8.20 | 🟢 Normal | -0.029 |  |
| 2026-04-02 17:07:06 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | -0.055 |  |
| 2026-04-02 17:00:57 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | -0.060 |  |
| 2026-04-02 17:04:50 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.116 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)