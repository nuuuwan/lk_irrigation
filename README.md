# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_23:02:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,546 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 23:02:48 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:02:25 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:02:25 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:02:16 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:46 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:37 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2026-03-02 23:01:18 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-02 23:00:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 23:00:20 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:00:10 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:44:01 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:19:44 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:15:12 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:14:27 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:14:16 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-02 22:13:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:13:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.012 |  |
| 2026-03-02 22:09:13 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-02 22:08:49 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-02 22:06:31 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-03-02 23:01:04 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-02 22:14:16 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-03-02 22:02:14 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-03-02 22:02:19 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-02 23:00:33 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 23:00:20 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:02:16 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:00:56 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:35 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:04:11 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:15:12 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:14:27 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:05:15 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:46 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:02:49 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:06:24 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:44:01 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:02:53 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:00:10 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:02:48 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:05:15 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:02:40 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:13:03 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 22:05:47 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 23:01:18 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:02:25 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:01:37 | Glencourse (Kelani Ganga) | 8.24 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:02:25 | Thalgahagoda (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-03-02 22:02:25 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.010 |  |
| 2026-03-02 23:01:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.36 | 🟢 Normal | -0.012 |  |
| 2026-03-02 20:04:40 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | -0.017 |  |
| 2026-03-02 22:09:13 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | -0.019 |  |
| 2026-03-02 22:02:03 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.233 |  |
| 2026-03-02 22:05:20 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)