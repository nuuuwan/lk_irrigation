# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_13:37:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 13:37:07 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:33:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 13:33:29 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:14:06 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.008 |  |
| 2026-05-02 13:13:21 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:12:43 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.015 |  |
| 2026-05-02 13:11:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-02 13:10:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-02 13:10:01 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-02 13:09:30 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:08:39 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.056 |  |
| 2026-05-02 13:08:31 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:07:49 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.028 |  |
| 2026-05-02 13:07:40 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:05:38 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:05:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-02 13:05:17 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:04:22 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-05-02 13:04:02 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.048 |  |
| 2026-05-02 13:03:25 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-02 13:03:24 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-02 13:03:18 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-02 13:03:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:02:44 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.126 |  |
| 2026-05-02 13:02:31 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 13:02:24 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:02:23 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:02:00 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 13:01:53 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:47 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:17 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:14 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:01:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 13:01:06 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-05-02 13:00:37 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:00:15 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 13:03:18 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | 0.152 | 🔺 Rising |
| 2026-05-02 13:05:29 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-05-02 13:11:54 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-02 13:03:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-05-02 13:02:31 | Thanamalwila (Kirindi Oya) | 0.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 13:10:30 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-02 13:33:35 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 13:01:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 13:02:00 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 13:00:15 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:53 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:00:37 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:37:07 | Moragaswewa (Deduru Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:48 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:33:29 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:47 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:08:31 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:17 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:03:24 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:03:00 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:01:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:05:38 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:02:23 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:07:40 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 13:14:06 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | -0.008 |  |
| 2026-05-02 13:10:01 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-05-02 13:09:30 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:01:14 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:01:39 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:02:24 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-02 13:03:25 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.011 |  |
| 2026-05-02 13:01:06 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.012 |  |
| 2026-05-02 13:12:43 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.015 |  |
| 2026-05-02 13:04:22 | Thanthirimale (Malwathu Oya) | 1.95 | 🟢 Normal | -0.019 |  |
| 2026-05-02 13:07:49 | Rathnapura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.028 |  |
| 2026-05-02 13:04:02 | Ellagawa (Kalu Ganga) | 4.70 | 🟢 Normal | -0.048 |  |
| 2026-05-02 13:08:39 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.056 |  |
| 2026-05-02 13:02:44 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)