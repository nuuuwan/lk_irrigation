# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_19:30:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,861 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 19:30:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:30:38 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:25:23 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:24:53 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-02 19:14:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:11:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:10:49 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:10:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:09:05 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-01-02 19:08:18 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-02 19:07:27 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-01-02 19:06:21 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-02 19:06:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 19:06:16 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 19:05:58 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-02 19:05:42 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:05:18 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-01-02 19:05:01 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-01-02 19:04:58 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 19:04:36 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:12 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:08 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-01-02 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:27 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:26 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:09 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:09 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-02 19:03:01 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:00 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-01-02 19:02:56 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:02:45 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:01:55 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-02 19:00:26 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:00:24 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:55:10 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 19:09:05 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | 0.310 | 🔺 Rising |
| 2026-01-02 19:06:21 | Pitabeddara (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-01-02 19:05:58 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-02 19:08:18 | Panadugama (Nilwala Ganga) | 2.36 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-01-02 18:00:30 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-01-02 19:06:20 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-02 19:24:53 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-02 19:06:16 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 19:04:58 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 19:05:42 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:30:38 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:38 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:27 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:12 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:30:54 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:14:00 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:26 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:02:56 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:20 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:10:39 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:01 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:02:45 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:03:09 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:00:26 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:00:24 | Manampitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:04:36 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:11:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:10:49 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:25:23 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.009 |  |
| 2026-01-02 19:03:09 | Padiyathalawa (Maduru Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-02 19:07:27 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.019 |  |
| 2026-01-02 19:05:18 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.019 |  |
| 2026-01-02 19:05:01 | Katharagama (Menik Ganga) | 0.35 | 🟢 Normal | -0.019 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 19:03:00 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | -0.029 |  |
| 2026-01-02 19:04:08 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | -0.030 |  |
| 2026-01-02 19:01:55 | Siyambalanduwa (Heda Oya) | 1.20 | 🟢 Normal | -0.031 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)