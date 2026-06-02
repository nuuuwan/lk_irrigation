# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--02_23:28:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **168,814 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 23:28:12 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.016 |  |
| 2026-06-02 23:27:29 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.014 |  |
| 2026-06-02 23:17:00 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.018 |  |
| 2026-06-02 23:15:29 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 23:14:26 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:13:22 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:12:10 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 23:10:28 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:09:01 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.019 |  |
| 2026-06-02 23:08:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-02 23:07:55 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.149 |  |
| 2026-06-02 23:05:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:05:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-02 23:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-02 23:05:16 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 23:04:54 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:04:47 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 23:04:43 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-02 23:04:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:03:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:03:25 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:54 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:39 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:22 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-06-02 23:02:17 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:15 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 23:02:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 23:01:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:43 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:02 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:00 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:00:48 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-06-02 23:00:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-02 23:00:48 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-06-02 23:05:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.94 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-06-02 23:04:43 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-02 20:03:23 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-06-02 23:05:16 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-02 23:02:15 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 23:04:47 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-02 23:08:42 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-06-02 23:15:29 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 23:02:15 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-02 23:12:10 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-02 18:00:11 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:57 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:43 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:14:26 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 22:01:24 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:03:25 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:00:42 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:00:09 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:13:22 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:10:28 | Ellagawa (Kalu Ganga) | 5.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:01:02 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:05:53 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:04:32 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:54 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:40 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:03:46 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:04:54 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-06-02 18:04:24 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:15 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:02:17 | Thanamalwila (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-02 23:05:42 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-06-02 23:27:29 | Wellawaya (Kirindi Oya) | 0.78 | 🟢 Normal | -0.014 |  |
| 2026-06-02 23:28:12 | Baddegama (Gin Ganga) | 1.52 | 🟢 Normal | -0.016 |  |
| 2026-06-02 23:17:00 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.018 |  |
| 2026-06-02 23:09:01 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | -0.019 |  |
| 2026-06-02 22:05:18 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-06-02 23:02:22 | Hanwella (Kelani Ganga) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-06-02 23:07:55 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)