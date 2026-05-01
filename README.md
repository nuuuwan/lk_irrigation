# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_05:02:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,562 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 05:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 05:02:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 05:02:11 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:11 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-02 05:02:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.103 |  |
| 2026-05-02 05:02:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:01:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-02 05:01:48 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:44 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:41 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:41 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:01:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 04:47:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:25:51 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-02 04:23:12 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-02 04:21:10 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.103 |  |
| 2026-05-02 04:17:54 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 04:10:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-05-02 04:10:24 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 04:10:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 05:01:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-02 04:07:05 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-05-02 04:06:14 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-05-02 05:02:11 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-02 04:08:56 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-05-02 04:25:51 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-02 04:04:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-02 05:02:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 05:01:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 05:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 04:01:33 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 04:10:24 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-02 04:01:06 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:04:13 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:44 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:05:11 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:03:22 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:41 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:47:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:11 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:23:12 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-05-02 04:04:07 | Dunamale (Aththanagalu Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:01:41 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-02 04:04:17 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.012 |  |
| 2026-05-02 04:04:22 | Thawalama (Gin Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-05-02 04:03:17 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-05-02 04:02:09 | Moragaswewa (Deduru Oya) | 0.76 | 🟢 Normal | -0.022 |  |
| 2026-05-02 04:10:59 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 04:01:53 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.035 |  |
| 2026-05-02 04:06:02 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.037 |  |
| 2026-05-02 04:02:27 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | -0.040 |  |
| 2026-05-02 04:04:29 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | -0.046 |  |
| 2026-05-02 04:04:14 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.050 |  |
| 2026-05-02 04:10:13 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.068 |  |
| 2026-05-02 05:02:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)