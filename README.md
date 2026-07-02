# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_10:17:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **195,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 10:17:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:15:19 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:12:34 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-02 10:12:03 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:11:53 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.018 |  |
| 2026-07-02 10:08:48 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:07:20 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:06:38 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:06:25 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-07-02 10:05:56 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-07-02 10:05:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:05:28 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:05:20 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:40 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:40 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.021 |  |
| 2026-07-02 10:04:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:03:02 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-07-02 10:02:49 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-02 10:02:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 10:02:42 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.044 |  |
| 2026-07-02 10:02:35 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-02 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-02 10:02:16 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:02:12 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:54 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.102 |  |
| 2026-07-02 10:01:54 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:43 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:01:32 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-07-02 10:01:24 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:14 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:01:08 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:00:50 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:00:42 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 10:00:40 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:00:33 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-02 10:00:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-02 10:00:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 10:00:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-07-02 10:02:35 | Nagalagam Street (Kelani Ganga) | 0.09 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-07-02 10:00:42 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 10:02:44 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-02 10:02:49 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-07-02 10:00:40 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:00:08 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:17:43 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:51 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:40 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:02:12 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:12:03 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:18 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:24 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:04:18 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:05:43 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:08:48 | Rathnapura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:05:20 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:07:20 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:00:50 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:01:54 | Thanamalwila (Kirindi Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 10:12:34 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-07-02 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-07-02 10:06:25 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-07-02 10:05:28 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:06:38 | Magura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:01:08 | Ellagawa (Kalu Ganga) | 5.18 | 🟢 Normal | -0.011 |  |
| 2026-07-02 10:11:53 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.018 |  |
| 2026-07-02 10:03:02 | Hanwella (Kelani Ganga) | 1.62 | 🟢 Normal | -0.020 |  |
| 2026-07-02 10:04:40 | Glencourse (Kelani Ganga) | 9.82 | 🟢 Normal | -0.021 |  |
| 2026-07-02 10:01:14 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:02:16 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:01:43 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.030 |  |
| 2026-07-02 10:00:33 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.031 |  |
| 2026-07-02 10:05:56 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.039 |  |
| 2026-07-02 10:02:42 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.044 |  |
| 2026-07-02 10:01:32 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.061 |  |
| 2026-07-02 10:01:54 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.102 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)