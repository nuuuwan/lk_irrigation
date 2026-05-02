# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_06:24:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,627 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 06:24:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-02 06:14:28 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-02 06:13:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-02 06:11:25 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-05-02 06:10:54 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-05-02 06:10:30 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-05-02 06:10:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-05-02 06:08:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:07:52 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-02 06:07:23 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-02 06:06:27 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.147 |  |
| 2026-05-02 06:06:11 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:05:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-02 06:04:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:04:22 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:04:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.023 |  |
| 2026-05-02 06:04:14 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-02 06:03:58 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:03:15 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-02 06:03:10 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-02 06:03:03 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:03:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-02 06:02:54 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-02 06:02:43 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:02:17 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-05-02 06:02:16 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 06:01:55 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-05-02 06:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:14 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-05-02 06:01:10 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:01 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-02 06:01:00 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.074 |  |
| 2026-05-02 06:00:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.033 |  |
| 2026-05-02 06:00:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:00:11 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:00:09 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 06:01:55 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-05-02 06:07:52 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-05-02 06:05:44 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-05-02 06:03:15 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-02 06:07:23 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-02 06:02:54 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-05-02 06:24:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.01 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-02 06:02:16 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-02 06:13:26 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-05-02 06:14:28 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-05-02 06:01:01 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-02 06:00:40 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:03:58 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:19 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:06:11 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:10 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:00:11 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:08:05 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:04:22 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:04:33 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:02:43 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:02:41 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:01:17 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 06:10:54 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.009 |  |
| 2026-05-02 06:04:14 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-02 06:10:30 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.019 |  |
| 2026-05-02 06:03:01 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.020 |  |
| 2026-05-02 06:03:10 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-02 06:00:09 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.021 |  |
| 2026-05-02 06:04:20 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | -0.023 |  |
| 2026-05-02 06:11:25 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.029 |  |
| 2026-05-02 06:02:17 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.029 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 06:00:50 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.033 |  |
| 2026-05-02 06:01:14 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.047 |  |
| 2026-05-02 06:01:00 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.074 |  |
| 2026-05-02 06:10:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.075 |  |
| 2026-05-02 06:06:27 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)