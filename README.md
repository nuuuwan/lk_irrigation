# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_20:19:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,708 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 20:19:05 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-02 20:18:55 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:12:13 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-02 20:12:10 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-02 20:11:17 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:10:51 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.027 |  |
| 2026-06-02 20:09:29 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.094 |  |
| 2026-06-02 20:08:44 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:07:32 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:06:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:06:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.121 |  |
| 2026-06-02 20:05:48 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:05:46 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 20:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:05:16 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-02 20:04:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:04:40 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:04:34 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.004 |  |
| 2026-06-02 20:04:25 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:44 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:36 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 20:03:25 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:23 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-02 20:03:18 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-06-02 20:02:40 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 20:02:04 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:02:03 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-02 20:01:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.109 |  |
| 2026-06-02 20:01:40 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:51 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:17 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:54:13 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 19:44:37 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.032 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 20:12:10 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-06-02 20:12:13 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-06-02 20:02:03 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-02 20:03:23 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-02 20:19:05 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-02 20:05:46 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-02 20:02:04 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-02 20:03:34 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-02 20:04:34 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.004 |  |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:17 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:02:04 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:07:32 | Moragaswewa (Deduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:01:36 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:06:37 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:04:25 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:18:55 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:04:40 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:02:40 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:05:48 | Baddegama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:25 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:08:44 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:38 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:04:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:11:17 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:36 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:03:44 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:01:13 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:00:51 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-06-02 20:05:16 | Badalgama (Maha Oya) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-06-02 19:03:22 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-06-02 20:10:51 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.027 |  |
| 2026-06-02 20:03:18 | Hanwella (Kelani Ganga) | 1.57 | 🟢 Normal | -0.041 |  |
| 2026-06-02 20:09:29 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.094 |  |
| 2026-06-02 20:01:41 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.109 |  |
| 2026-06-02 20:06:23 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)