# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--25_04:08:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **106,630 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 04:08:26 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:08:25 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:08:23 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:08:22 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:08:19 | Putupaula (Kalu Ganga) | 0.24 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:07:02 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:06:17 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:06:10 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:06:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-25 04:05:54 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-25 04:05:35 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-03-25 04:05:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:05:07 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:04:37 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:04:10 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-25 04:03:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:52 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:25 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:21 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-25 04:02:13 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-25 04:01:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-25 04:01:44 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-03-25 04:01:41 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:01:33 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.135 |  |
| 2026-03-25 04:01:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-03-25 04:01:29 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 04:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:00:33 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-25 03:24:34 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-25 04:08:26 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 360.000 | 🔺 Rising |
| 2026-03-25 04:04:10 | Glencourse (Kelani Ganga) | 8.45 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-03-25 03:04:31 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-03-25 04:00:33 | Kithulgala (Kelani Ganga) | 1.59 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-25 04:06:07 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-03-25 04:02:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-25 04:01:29 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-25 04:05:29 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:13 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 03:24:34 | Nawalapitiya (Mahaweli Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:01:22 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:04:37 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-03-25 01:14:52 | Horowpothana (Yan Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:02:47 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:52 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:06:17 | Pitabeddara (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:03:14 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:01:41 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-03-25 02:08:39 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-03-25 03:00:12 | Padiyathalawa (Maduru Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:02:25 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-25 03:05:06 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-25 03:07:20 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:07:02 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:06:10 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-24 18:00:33 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-25 04:05:07 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-25 01:03:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.34 | 🟢 Normal | -0.008 |  |
| 2026-03-25 04:02:21 | Thanamalwila (Kirindi Oya) | 0.24 | 🟢 Normal | -0.010 |  |
| 2026-03-25 04:01:55 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-03-25 04:01:44 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-03-25 04:05:35 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.019 |  |
| 2026-03-25 04:05:54 | Wellawaya (Kirindi Oya) | 0.62 | 🟢 Normal | -0.020 |  |
| 2026-03-25 04:01:30 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-03-25 03:02:14 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.023 |  |
| 2026-03-25 03:00:59 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.040 |  |
| 2026-03-24 18:00:42 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.120 |  |
| 2026-03-25 04:01:33 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.135 |  |
| 2026-03-25 03:11:32 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -3.130 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)