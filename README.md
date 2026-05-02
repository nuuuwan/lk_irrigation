# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_05:22:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,588 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 05:22:29 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-02 05:21:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:18:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:13:08 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 14.500 | 🔺 Rising |
| 2026-05-02 05:10:44 | Baddegama (Gin Ganga) | 0.50 | 🟢 Normal | 14.500 | 🔺 Rising |
| 2026-05-02 05:10:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.013 |  |
| 2026-05-02 05:09:45 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-02 05:08:47 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.036 |  |
| 2026-05-02 05:07:16 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:06:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.022 |  |
| 2026-05-02 05:05:53 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-02 05:05:13 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-02 05:04:33 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-05-02 05:04:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.136 |  |
| 2026-05-02 05:04:10 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-02 05:04:07 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.093 |  |
| 2026-05-02 05:03:53 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:03:47 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-02 05:03:16 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:03:09 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:50 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-02 05:02:26 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-02 05:02:26 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:18 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
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

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 05:13:08 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 14.500 | 🔺 Rising |
| 2026-05-02 05:05:53 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | 0.195 | 🔺 Rising |
| 2026-05-02 05:02:50 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-05-02 05:01:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-05-02 05:02:11 | Ellagawa (Kalu Ganga) | 4.89 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-05-02 05:09:45 | Magura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-05-02 05:22:29 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-02 05:05:13 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-05-02 05:02:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-02 05:01:07 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-02 05:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-02 05:02:57 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:20 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:44 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:03:53 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:01:41 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-02 04:47:00 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:02:11 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:03:16 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:21:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 05:07:16 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:26 | Moragaswewa (Deduru Oya) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:03:09 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:18 | Dunamale (Aththanagalu Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:01:41 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:02:01 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-05-02 05:10:03 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.013 |  |
| 2026-05-02 05:02:26 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-05-02 05:06:43 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.022 |  |
| 2026-05-02 05:03:47 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.029 |  |
| 2026-05-02 05:04:33 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-05-02 05:04:10 | Thawalama (Gin Ganga) | 1.62 | 🟢 Normal | -0.030 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 05:08:47 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.036 |  |
| 2026-05-02 05:04:07 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.093 |  |
| 2026-05-02 05:02:06 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.103 |  |
| 2026-05-02 05:04:10 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.136 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)