# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_08:06:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,944 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 08:06:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-04-02 08:05:41 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 08:05:35 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:30 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:29 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:18 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-02 08:04:57 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:04:52 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.197 |  |
| 2026-04-02 08:04:07 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:03:16 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:03:11 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:03:11 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 08:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 08:02:44 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:02:37 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-02 08:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -10.667 |  |
| 2026-04-02 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-02 08:02:16 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:02:16 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:13 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -10.667 |  |
| 2026-04-02 08:01:09 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:08 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:05 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:00:59 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-04-02 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.102 |  |
| 2026-04-02 08:00:42 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-02 08:00:05 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-02 07:29:31 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.050 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 07:07:36 | Kithulgala (Kelani Ganga) | 1.66 | 🟢 Normal | 0.489 | 🔺 Rising |
| 2026-04-02 08:00:42 | Weraganthota (Mahaweli Ganga) | -1.83 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-02 08:05:18 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-02 06:01:11 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-02 07:02:06 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-02 08:03:11 | Hanwella (Kelani Ganga) | 0.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-02 07:04:19 | Magura (Kalu Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 08:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 08:05:41 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 08:01:09 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:02:44 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:42 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:04:07 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 06:00:51 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:35 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:03:16 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:08 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:29 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:04:57 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:06:09 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:03:04 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:00:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:02:16 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:08:07 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:05:30 | Rathnapura (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:01:05 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:06:41 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:03:11 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 08:02:16 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 07:06:24 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | -0.009 |  |
| 2026-04-02 08:02:37 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-02 08:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-04-02 08:00:05 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | -0.011 |  |
| 2026-04-02 07:07:20 | Peradeniya (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.019 |  |
| 2026-04-02 08:06:22 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | -0.020 |  |
| 2026-04-02 08:00:59 | Manampitiya (Mahaweli Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-04-02 08:00:58 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | -0.102 |  |
| 2026-04-02 08:04:52 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | -0.197 |  |
| 2026-04-02 08:02:34 | Nawalapitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -10.667 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)