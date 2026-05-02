# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_12:19:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,867 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 12:19:18 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:10:30 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:09:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-02 12:09:08 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:07:58 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:07:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-02 12:07:27 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-05-02 12:05:37 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-05-02 12:05:08 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:05:00 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.037 |  |
| 2026-05-02 12:04:52 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.077 |  |
| 2026-05-02 12:04:51 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-02 12:04:36 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-05-02 12:04:17 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:04:14 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-02 12:04:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-02 12:03:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:03:45 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:03:26 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-02 12:03:06 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 12:03:03 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-05-02 12:02:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:02:46 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:32 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:02:31 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.055 |  |
| 2026-05-02 12:02:29 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:02:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:16 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-02 12:02:06 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:43 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-02 12:01:30 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:27 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:01:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:01:15 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.052 |  |
| 2026-05-02 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:00:44 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:00:38 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 12:04:09 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-05-02 12:07:45 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-05-02 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-05-02 12:04:51 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-02 12:01:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-02 12:09:56 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-05-02 12:04:14 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-05-02 12:03:06 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 12:02:29 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:03:45 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:02:58 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:00:38 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:19:18 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:00:58 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:30 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:07:58 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:43 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:55 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:02:32 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:03:51 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:10:30 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:04:17 | Holombuwa (Kelani Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:09:08 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:05:08 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-02 12:01:27 | Thanthirimale (Malwathu Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:16 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:26 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:01:19 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:02:46 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | -0.010 |  |
| 2026-05-02 12:07:27 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-05-02 12:03:26 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.029 |  |
| 2026-05-02 11:08:58 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.029 |  |
| 2026-05-02 12:05:00 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -0.037 |  |
| 2026-05-02 12:03:03 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | -0.042 |  |
| 2026-05-02 12:01:15 | Ellagawa (Kalu Ganga) | 4.75 | 🟢 Normal | -0.052 |  |
| 2026-05-02 12:02:31 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | -0.055 |  |
| 2026-05-02 12:04:36 | Deraniyagala (Kelani Ganga) | 0.31 | 🟢 Normal | -0.058 |  |
| 2026-05-02 12:05:37 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-05-02 12:04:52 | Glencourse (Kelani Ganga) | 8.78 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)