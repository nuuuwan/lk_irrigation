# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_12:12:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,589 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 12:12:29 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:09:36 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:08:24 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | -0.027 |  |
| 2026-01-02 12:07:04 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:06:16 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-01-02 12:06:13 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:05:25 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.057 |  |
| 2026-01-02 12:05:20 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-02 12:05:10 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:04:36 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:04:01 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-02 12:03:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-02 12:03:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-01-02 12:03:25 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:03:24 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | -0.136 |  |
| 2026-01-02 12:03:20 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 12:03:19 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-01-02 12:03:14 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:02:49 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:02:48 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:02:43 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:02:43 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.074 |  |
| 2026-01-02 12:02:42 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.118 |  |
| 2026-01-02 12:02:33 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 12:02:23 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.055 |  |
| 2026-01-02 12:02:03 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 12:01:46 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:01:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 12:01:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:01:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:00:39 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:00:33 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:00:17 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-02 11:32:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-01-02 11:18:45 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:17:04 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 11:16:49 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 12:03:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.75 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-01-02 12:04:01 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-01-02 12:01:33 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 12:02:03 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 12:03:20 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 12:02:33 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 12:00:33 | Weraganthota (Mahaweli Ganga) | -1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:01:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-02 05:06:54 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:02:51 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:00:39 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:03:25 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:06:13 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:01:46 | Pitabeddara (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:02:49 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:12:29 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:04:36 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:03:14 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:05:10 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-01-02 09:18:58 | Manampitiya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:09:36 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:07:04 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-02 12:06:16 | Galgamuwa (Mee Oya) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-01-02 12:03:31 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:02:43 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:02:48 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:01:27 | Norwood (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-01-02 12:03:19 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.011 |  |
| 2026-01-02 12:03:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-01-02 11:05:47 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | -0.019 |  |
| 2026-01-02 12:00:17 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-02 11:32:11 | Thalgahagoda (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-01-02 12:08:24 | Katharagama (Menik Ganga) | 0.49 | 🟢 Normal | -0.027 |  |
| 2026-01-02 12:05:20 | Padiyathalawa (Maduru Oya) | 1.55 | 🟢 Normal | -0.050 |  |
| 2026-01-02 12:02:23 | Nakkala (Kumbukkan Oya) | 1.38 | 🟢 Normal | -0.055 |  |
| 2026-01-02 12:05:25 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | -0.057 |  |
| 2026-01-02 12:02:43 | Thaldena (Mahaweli Ganga) | 0.94 | 🟢 Normal | -0.074 |  |
| 2026-01-02 12:02:42 | Siyambalanduwa (Heda Oya) | 1.50 | 🟢 Normal | -0.118 |  |
| 2026-01-02 12:03:24 | Horowpothana (Yan Oya) | 3.18 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)