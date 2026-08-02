# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--02_11:18:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,842 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 11:18:09 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-02 11:11:13 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 11:10:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:09:45 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-02 11:07:29 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.083 |  |
| 2026-08-02 11:07:14 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:05:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-02 11:05:41 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 11:05:35 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:05:09 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.032 |  |
| 2026-08-02 11:04:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:04:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:59 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:55 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-02 11:03:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-08-02 11:03:31 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.164 |  |
| 2026-08-02 11:03:28 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:21 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-08-02 11:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:11 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.132 |  |
| 2026-08-02 11:03:08 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-08-02 11:02:41 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-08-02 11:02:40 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-08-02 11:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-08-02 11:02:28 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:18 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:11 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:11 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.198 |  |
| 2026-08-02 11:02:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-08-02 11:01:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-02 11:01:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-02 11:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:01:35 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-02 11:01:19 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:01:14 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-02 11:00:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-02 11:01:35 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-02 11:03:55 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-02 11:11:13 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-02 11:18:09 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-08-02 11:01:44 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-02 11:05:41 | Glencourse (Kelani Ganga) | 10.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-02 11:03:59 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:28 | Moragaswewa (Deduru Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:01:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:01:20 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:04:00 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:10:18 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:04:52 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:28 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:01:19 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:18 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:00:25 | Thanthirimale (Malwathu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:07:14 | Peradeniya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:05:35 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:39 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:02:11 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-02 10:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.49 | 🟢 Normal | 0.000 |  |
| 2026-08-02 11:09:45 | Magura (Kalu Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-08-02 11:01:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-02 11:01:14 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-02 11:05:57 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.011 |  |
| 2026-08-02 11:02:10 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-08-02 11:03:08 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-08-02 11:03:51 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.023 |  |
| 2026-08-02 11:03:21 | Rathnapura (Kalu Ganga) | 1.53 | 🟢 Normal | -0.030 |  |
| 2026-08-02 11:05:09 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.032 |  |
| 2026-08-02 11:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.040 |  |
| 2026-08-02 11:02:40 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.051 |  |
| 2026-08-02 11:02:41 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.063 |  |
| 2026-08-02 11:07:29 | Ellagawa (Kalu Ganga) | 5.79 | 🟢 Normal | -0.083 |  |
| 2026-08-02 11:03:11 | Hanwella (Kelani Ganga) | 2.17 | 🟢 Normal | -0.132 |  |
| 2026-08-02 11:03:31 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.164 |  |
| 2026-08-02 11:02:11 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.198 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)