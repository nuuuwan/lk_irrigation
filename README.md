# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--03_03:34:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,703 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-03 03:34:51 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:34:37 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.113 |  |
| 2026-03-03 03:14:51 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:10:50 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:10:19 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:08:43 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:07:49 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:07:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:06:32 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-03 03:06:09 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-03 03:05:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-03-03 03:05:20 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 03:05:17 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | -0.084 |  |
| 2026-03-03 03:04:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:04:26 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 03:04:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -17.638 |  |
| 2026-03-03 03:03:43 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:42 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:23 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:16 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:14 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:08 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-03-03 03:02:53 | Dunamale (Aththanagalu Oya) | 1.40 | 🟢 Normal | -0.113 |  |
| 2026-03-03 03:02:42 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 03:02:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-03 03:02:11 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.006 |  |
| 2026-03-03 03:02:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2026-03-03 03:02:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-03 03:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 03:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:41 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-03 03:01:16 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:00:31 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-03 03:06:32 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-03-03 03:06:09 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-03 03:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-03 03:02:42 | Moraketiya (Walawe Ganga) | 0.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-03 03:04:26 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 03:05:20 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-03 03:03:23 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:00:31 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:14 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:04:54 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:16 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:35 | Horowpothana (Yan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:34:51 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:10:19 | Norwood (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:42 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:41 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:01:52 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:07:47 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:21 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:07:49 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:10:50 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:14:51 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:04:19 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:03:43 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:08:43 | Thanamalwila (Kirindi Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-03-03 03:02:11 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.006 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-03 03:02:00 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-03-03 03:01:25 | Ellagawa (Kalu Ganga) | 3.87 | 🟢 Normal | -0.010 |  |
| 2026-03-03 03:05:25 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | -0.011 |  |
| 2026-03-03 03:02:37 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.030 |  |
| 2026-03-03 03:03:08 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.049 |  |
| 2026-03-03 03:05:17 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | -0.084 |  |
| 2026-03-03 03:02:00 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.098 |  |
| 2026-03-03 03:34:37 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.113 |  |
| 2026-03-03 03:03:57 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | -17.638 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)