# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_20:32:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **141,184 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 20:32:39 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:20:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:15:40 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:14:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 20:12:15 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.164 |  |
| 2026-05-02 20:11:54 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:10:00 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |
| 2026-05-02 20:08:33 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:08:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-05-02 20:08:10 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:08:07 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-05-02 20:07:16 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:06:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:05:51 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:04:41 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:04:41 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.036 |  |
| 2026-05-02 20:04:18 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:03:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-05-02 20:03:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-02 20:02:59 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 20:02:56 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-02 20:02:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 20:02:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:02:15 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-02 20:02:13 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.094 |  |
| 2026-05-02 20:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:01:37 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:01:29 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 20:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:01:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 20:01:12 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-02 20:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-02 20:00:53 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:00:27 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:00:25 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 20:02:56 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-02 18:01:54 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-02 20:02:59 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-02 20:01:29 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 20:01:13 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 20:14:27 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-02 20:02:21 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-02 20:02:17 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:00:25 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:00:53 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:01:37 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:08:10 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:32:39 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-02 18:01:42 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:08:33 | Magura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-02 19:08:29 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:04:18 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:11:54 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:15:40 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:00:27 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:07:16 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:02:11 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:04:41 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:10:00 | Holombuwa (Kelani Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:20:25 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:01:13 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:06:41 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-02 20:03:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-02 18:01:54 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-05-02 20:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-02 20:08:07 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.019 |  |
| 2026-05-02 20:01:12 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-05-02 20:08:28 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.028 |  |
| 2026-05-02 20:02:15 | Hanwella (Kelani Ganga) | 0.55 | 🟢 Normal | -0.030 |  |
| 2026-05-02 20:04:41 | Ellagawa (Kalu Ganga) | 4.47 | 🟢 Normal | -0.036 |  |
| 2026-05-02 20:03:45 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.066 |  |
| 2026-05-02 20:02:13 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.094 |  |
| 2026-05-02 20:09:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.141 |  |
| 2026-05-02 20:12:15 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)