# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_13:16:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,151 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 13:16:29 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:15:36 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-02 13:12:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:12:01 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:11:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:09:53 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:09:18 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:08:54 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 13:07:49 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.139 |  |
| 2026-04-02 13:07:44 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-02 13:07:35 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-04-02 13:07:05 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-04-02 13:06:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:06:11 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:05:57 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 13:05:28 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:05:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:05:00 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.069 |  |
| 2026-04-02 13:04:20 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-02 13:04:15 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:57 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:52 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-02 13:03:33 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 13:03:30 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:08 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:02:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-02 13:02:13 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:02:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:58 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:12 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-02 13:01:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:00:53 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:00:47 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.251 |  |
| 2026-04-02 13:00:34 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:00:11 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 13:01:12 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-04-02 13:04:20 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-02 13:02:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-02 13:03:52 | Panadugama (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-04-02 13:15:36 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-02 13:07:44 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-04-02 13:05:57 | Moragaswewa (Deduru Oya) | -0.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 13:03:33 | Norwood (Kelani Ganga) | 0.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 13:08:54 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-02 13:02:49 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:30 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:02:09 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:33 | Giriulla (Maha Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:11:58 | Horowpothana (Yan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:57 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:11 | Hanwella (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:05:28 | Deraniyagala (Kelani Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:58 | Ellagawa (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:00:11 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:06:38 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:00:53 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:16:29 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:01:17 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:12:36 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:04:15 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:09:18 | Thanthirimale (Malwathu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:09:53 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:03:08 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:02:13 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 13:05:17 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:06:11 | Rathnapura (Kalu Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:02:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:00:34 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-02 13:07:05 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | -0.011 |  |
| 2026-04-02 13:07:35 | Peradeniya (Mahaweli Ganga) | 1.07 | 🟢 Normal | -0.027 |  |
| 2026-04-02 13:05:00 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.069 |  |
| 2026-04-02 13:07:49 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.139 |  |
| 2026-04-02 13:00:47 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)