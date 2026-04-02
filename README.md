# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_14:11:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,189 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 14:11:18 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:10:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 14:09:45 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-04-02 14:08:46 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:08:39 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-02 14:07:46 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:06:47 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 14:06:05 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:51 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:16 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:07 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:04:25 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:59 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:57 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-02 14:03:55 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:53 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:08 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.052 |  |
| 2026-04-02 14:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:12 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:06 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:46 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-04-02 14:01:36 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:27 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 14:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:25 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-02 14:01:14 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:09 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.050 |  |
| 2026-04-02 14:01:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-02 14:00:56 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | -0.209 |  |
| 2026-04-02 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 14:00:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 13:57:57 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 14:01:25 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-04-02 14:03:57 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-02 14:06:47 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-04-02 13:15:36 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-02 14:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-02 14:00:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 14:01:27 | Ellagawa (Kalu Ganga) | 3.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 14:10:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 14:01:36 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:15 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:14 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:26 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:12 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:11:18 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:04:25 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:55 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:30 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:59 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:07 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:06:05 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:28 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:07:46 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:51 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:05:16 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:53 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:09:18 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:08:46 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:03:31 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:06 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 14:01:08 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-04-02 14:08:39 | Thawalama (Gin Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-04-02 14:01:46 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.022 |  |
| 2026-04-02 14:09:45 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.029 |  |
| 2026-04-02 14:01:09 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.050 |  |
| 2026-04-02 14:03:08 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.052 |  |
| 2026-04-02 14:00:56 | Weraganthota (Mahaweli Ganga) | -2.71 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)