# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_04:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,266 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 04:10:34 | Nakkala (Kumbukkan Oya) | 1.87 | 🟢 Normal | -0.037 |  |
| 2026-01-02 04:09:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-01-02 04:09:21 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:54 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:52 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:51 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:45 | Siyambalanduwa (Heda Oya) | 1.96 | 🟢 Normal | -0.210 |  |
| 2026-01-02 04:07:43 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:07:12 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.096 |  |
| 2026-01-02 04:05:58 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:05:37 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:04:18 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 04:04:13 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:04:00 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-02 04:03:57 | Padiyathalawa (Maduru Oya) | 3.63 | 🟢 Normal | -0.380 |  |
| 2026-01-02 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 04:03:34 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-01-02 04:03:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | -0.701 |  |
| 2026-01-02 04:03:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 04:03:05 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.276 |  |
| 2026-01-02 04:02:41 | Horowpothana (Yan Oya) | 3.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 04:02:09 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:01:08 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 04:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-02 04:00:15 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-01-02 04:00:10 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-01-02 03:26:24 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:21:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 04:03:08 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-02 04:00:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.94 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-02 03:11:19 | Glencourse (Kelani Ganga) | 8.91 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-02 04:02:41 | Horowpothana (Yan Oya) | 3.85 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-02 04:01:08 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 03:05:29 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 04:04:18 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 04:03:42 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-02 03:03:21 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 03:01:06 | Thaldena (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-02 04:04:00 | Giriulla (Maha Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-01 17:09:46 | Galgamuwa (Mee Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:06:06 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:05:37 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:17:35 | Deraniyagala (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:09:21 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:01:22 | Moraketiya (Walawe Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:05:58 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:26:24 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-02 04:08:54 | Urawa (Nilwala Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-01-02 03:21:01 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.003 |  |
| 2026-01-02 04:04:13 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:07:43 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:02:09 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-02 04:03:34 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-01-02 04:03:58 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-01-01 18:02:09 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | -0.020 |  |
| 2026-01-02 04:00:15 | Kuda Oya (Kirindi Oya) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-01-02 04:00:10 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-01-02 04:10:34 | Nakkala (Kumbukkan Oya) | 1.87 | 🟢 Normal | -0.037 |  |
| 2026-01-02 00:11:06 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.038 |  |
| 2026-01-01 18:00:31 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.040 |  |
| 2026-01-02 04:09:46 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.058 |  |
| 2026-01-02 04:07:12 | Thanamalwila (Kirindi Oya) | 1.73 | 🟢 Normal | -0.096 |  |
| 2026-01-02 03:05:41 | Katharagama (Menik Ganga) | 1.04 | 🟢 Normal | -0.120 |  |
| 2026-01-02 04:08:45 | Siyambalanduwa (Heda Oya) | 1.96 | 🟢 Normal | -0.210 |  |
| 2026-01-02 04:03:05 | Peradeniya (Mahaweli Ganga) | 1.85 | 🟢 Normal | -0.276 |  |
| 2026-01-02 04:03:57 | Padiyathalawa (Maduru Oya) | 3.63 | 🟢 Normal | -0.380 |  |
| 2026-01-02 04:03:25 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | -0.701 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)