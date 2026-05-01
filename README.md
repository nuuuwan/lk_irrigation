# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--02_00:37:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **140,422 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 00:37:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.006 |  |
| 2026-05-02 00:25:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:16:36 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:12:57 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:08:30 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:08:29 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:08:27 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:07:23 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-05-02 00:07:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:07:05 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.055 |  |
| 2026-05-02 00:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-02 00:05:44 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:04:27 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-02 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-02 00:04:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-05-02 00:04:01 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:04:00 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:03:43 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-05-02 00:03:16 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-05-02 00:03:14 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:03:00 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:57 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.613 |  |
| 2026-05-02 00:02:41 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:39 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:33 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:02:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:00 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.069 |  |
| 2026-05-02 00:01:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:34 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:27 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.100 |  |
| 2026-05-02 00:01:26 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:22 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:00:09 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-01 23:49:41 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-02 00:07:23 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-05-02 00:06:21 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-05-02 00:04:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.71 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-02 00:04:27 | Peradeniya (Mahaweli Ganga) | 1.42 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-05-02 00:01:51 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:08:30 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:37 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:16:36 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-01 18:05:08 | Galgamuwa (Mee Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 22:04:17 | Magura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-01 21:10:47 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:12:57 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:05:44 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:22 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:02:33 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:26 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:04:01 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:25:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:01:34 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-05-02 00:37:12 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | -0.006 |  |
| 2026-05-02 00:04:00 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:03:14 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:39 | Thanamalwila (Kirindi Oya) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:07:10 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:10 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:03:00 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-05-01 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:02:41 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-05-02 00:00:09 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.011 |  |
| 2026-05-01 23:00:34 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.012 |  |
| 2026-05-02 00:03:16 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | -0.020 |  |
| 2026-05-02 00:03:43 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-05-02 00:04:04 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-05-01 23:13:38 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.031 |  |
| 2026-05-01 18:00:26 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.031 |  |
| 2026-05-02 00:07:05 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | -0.055 |  |
| 2026-05-02 00:02:00 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.069 |  |
| 2026-05-02 00:01:27 | Siyambalanduwa (Heda Oya) | 0.78 | 🟢 Normal | -0.100 |  |
| 2026-05-02 00:02:57 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.613 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)