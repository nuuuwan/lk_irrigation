# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_10:19:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,034 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.095 |  |
| 2026-04-02 10:10:33 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:09:13 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2026-04-02 10:08:28 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:07:20 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-04-02 10:07:09 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.214 |  |
| 2026-04-02 10:07:08 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:06:59 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-04-02 10:06:39 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:06:24 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:05:54 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:05:51 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:05:26 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:05:05 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 10:04:50 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 10:04:47 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:04:29 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-04-02 10:04:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:04:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:03:30 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-02 10:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:03:16 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:14 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:09 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-02 10:03:08 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:02:43 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:02:08 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.022 |  |
| 2026-04-02 10:02:08 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:02:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-02 10:01:55 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:29 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-02 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:00:50 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:00:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:00:28 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.040 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 10:06:59 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.442 | 🔺 Rising |
| 2026-04-02 10:03:30 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-04-02 10:02:06 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-02 10:03:09 | Hanwella (Kelani Ganga) | 0.27 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-02 10:05:05 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-02 10:04:50 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-02 10:07:08 | Magura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:02:43 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:04:00 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 10:00:50 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:04:10 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:00:46 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:08:28 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 09:14:53 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:08 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:55 | Deraniyagala (Kelani Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:04:47 | Ellagawa (Kalu Ganga) | 3.66 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:05:51 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:06:24 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:01:23 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:05:26 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:10:33 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:14 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:16 | Badalgama (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:00:28 | Thanthirimale (Malwathu Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:06:39 | Urawa (Nilwala Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:02:08 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-02 10:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:05:54 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:01:13 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-04-02 10:07:20 | Peradeniya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.018 |  |
| 2026-04-02 10:02:08 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.022 |  |
| 2026-04-02 10:04:29 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-04-02 10:09:13 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.029 |  |
| 2026-04-02 10:01:29 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-04-02 10:00:14 | Weraganthota (Mahaweli Ganga) | -1.84 | 🟢 Normal | -0.040 |  |
| 2026-04-02 10:19:49 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.095 |  |
| 2026-04-02 10:07:09 | Kithulgala (Kelani Ganga) | 1.17 | 🟢 Normal | -0.214 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)