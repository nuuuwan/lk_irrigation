# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_21:30:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,455 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 21:30:52 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:09:22 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:09:09 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-02 21:06:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-02 21:06:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:05:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:05:43 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-02 21:05:28 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-02 21:04:51 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-02 21:04:37 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 21:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-04-02 21:04:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:04:03 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-02 21:03:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-04-02 21:03:38 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:03:15 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:03:08 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-04-02 21:03:03 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:03:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-04-02 21:02:51 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:49 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-02 21:02:48 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:46 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-02 21:02:41 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 21:02:40 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-02 21:02:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-02 21:02:24 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.299 |  |
| 2026-04-02 21:02:17 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:12 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.161 |  |
| 2026-04-02 21:02:08 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:26 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:25 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-02 21:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:00:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:00:10 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 21:05:43 | Peradeniya (Mahaweli Ganga) | 2.41 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-04-02 21:05:28 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-02 21:02:49 | Glencourse (Kelani Ganga) | 8.29 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-02 21:02:40 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-02 21:09:09 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-02 21:04:37 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 21:04:51 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-02 21:02:41 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 18:02:18 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 21:03:03 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:03:38 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:03:15 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:00:52 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:00:30 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:26 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:51 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 18:08:10 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:08 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:17 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:00:10 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:04:13 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:48 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:30:52 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:05:52 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:09:22 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:01:24 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:06:08 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 21:02:35 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-02 21:03:00 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-04-02 21:04:03 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-02 21:04:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | -0.019 |  |
| 2026-04-02 21:02:46 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-04-02 21:06:19 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.021 |  |
| 2026-04-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.030 |  |
| 2026-04-02 21:03:08 | Thawalama (Gin Ganga) | 1.36 | 🟢 Normal | -0.032 |  |
| 2026-04-02 21:03:38 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.044 |  |
| 2026-04-02 21:01:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.066 |  |
| 2026-04-02 21:02:12 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.161 |  |
| 2026-04-02 21:02:24 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.299 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)