# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--02_02:24:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **194,839 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 02:24:52 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.007 |  |
| 2026-07-02 02:20:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-07-02 02:12:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-07-02 02:09:05 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.013 |  |
| 2026-07-02 02:07:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:07:33 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-07-02 02:07:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-07-02 02:07:24 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-02 02:07:17 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:06:26 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-07-02 02:06:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-02 02:05:34 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:04:43 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:04:10 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:04:07 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-07-02 02:03:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:03:05 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:59 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:46 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:42 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:27 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:38 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:53:44 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-02 02:20:53 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-07-02 02:06:22 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-07-02 02:07:24 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-07-02 01:04:49 | Thawalama (Gin Ganga) | 1.66 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-07-02 01:04:33 | Kithulgala (Kelani Ganga) | 1.65 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-07-01 18:02:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:27 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:38 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:03:05 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:17 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:55 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:01:20 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:06:53 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:07 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:46 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:13:53 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:03:52 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:01:41 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:59 | Dunamale (Aththanagalu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:05:14 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:05:34 | Badalgama (Maha Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:07:47 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-07-02 00:04:07 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:04:43 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-07-01 18:02:02 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:04:10 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:02:27 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-02 01:03:00 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-02 02:24:52 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | -0.007 |  |
| 2026-07-02 02:07:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | -0.009 |  |
| 2026-07-02 02:04:07 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-07-02 02:07:33 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-07-02 02:09:05 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.013 |  |
| 2026-07-02 01:28:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.80 | 🟢 Normal | -0.018 |  |
| 2026-07-02 02:06:26 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.020 |  |
| 2026-07-02 02:12:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.027 |  |
| 2026-07-02 00:43:49 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-07-02 01:02:57 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.053 |  |
| 2026-07-02 01:01:45 | Peradeniya (Mahaweli Ganga) | 2.29 | 🟢 Normal | -0.074 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)