# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--02_20:24:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **34,899 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 20:24:08 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:17:13 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-02 20:10:32 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:09:40 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:09:30 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-02 20:07:34 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-02 20:06:47 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:05:55 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-01-02 20:05:53 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 20:05:25 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.061 |  |
| 2026-01-02 20:04:59 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-01-02 20:04:57 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 20:04:57 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:04:53 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-02 20:04:31 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:04:15 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.067 |  |
| 2026-01-02 20:03:06 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:03:01 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:55 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:55 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:50 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:42 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-02 20:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-01-02 20:02:16 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-02 20:02:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 20:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:02:05 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.049 |  |
| 2026-01-02 20:01:58 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:55 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:43 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:01:11 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:00:21 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:00:11 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 19:59:48 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.032 |  |
| 2026-01-02 19:55:59 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.089 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-02 20:04:59 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | 0.408 | 🔺 Rising |
| 2026-01-02 20:09:30 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-01-02 20:07:34 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-02 20:02:16 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-02 20:04:57 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-02 20:17:13 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-01-02 20:04:53 | Panadugama (Nilwala Ganga) | 2.40 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-01-02 20:02:15 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-02 20:05:53 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-02 20:02:35 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-02 20:03:06 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:58 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:29 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:43 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:04:57 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-02 18:02:12 | Galgamuwa (Mee Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:24:08 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:06:47 | Hanwella (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:03:01 | Ellagawa (Kalu Ganga) | 4.28 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:50 | Baddegama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:00:11 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:00:21 | Dunamale (Aththanagalu Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:55 | Thaldena (Mahaweli Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:04:31 | Badalgama (Maha Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:55 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:10:32 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:02:55 | Kuda Oya (Kirindi Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-02 20:01:43 | Siyambalanduwa (Heda Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:01:11 | Nakkala (Kumbukkan Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:02:42 | Thanamalwila (Kirindi Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:02:10 | Katharagama (Menik Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-01-02 20:05:55 | Padiyathalawa (Maduru Oya) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-01-02 20:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.023 |  |
| 2026-01-02 18:03:09 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | -0.029 |  |
| 2026-01-02 19:59:48 | Horowpothana (Yan Oya) | 2.75 | 🟢 Normal | -0.032 |  |
| 2026-01-02 20:02:05 | Manampitiya (Mahaweli Ganga) | 2.13 | 🟢 Normal | -0.049 |  |
| 2026-01-02 18:03:09 | Weraganthota (Mahaweli Ganga) | -1.33 | 🟢 Normal | -0.049 |  |
| 2026-01-02 20:05:25 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.061 |  |
| 2026-01-02 20:04:15 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)